"""
Sistema de Análisis y Predicción de Jobs de Backup
Autor: [Tu Nombre]
Descripción: Aplicación Flask para análisis exploratorio y predicción de jobs con error

Este módulo contiene las funciones para:
1. Análisis exploratorio de datos de backup jobs
2. Preprocesamiento de datos
3. Entrenamiento de modelos de Machine Learning
4. Visualizaciones con Plotly
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.offline as pyo
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import joblib
import warnings
warnings.filterwarnings('ignore')

class BackupJobAnalyzer:
    """
    Clase principal para el análisis de jobs de backup
    Maneja carga de datos, análisis exploratorio, entrenamiento de modelos y predicciones
    """
    
    def __init__(self, data_path='backup1.csv'):
        """
        Inicializa el analizador de jobs de backup
        
        Args:
            data_path (str): Ruta al archivo CSV con los datos de backup
                            Por defecto usa backup1.csv con códigos numéricos de status
        """
        self.data_path = data_path
        self.df = None
        self.df_processed = None
        self.model = None
        self.label_encoders = {}
        self.scaler = StandardScaler()
        self.features = None
        self.target = None
        self.dataset_type = 'backup1'  # Nuevo dataset con códigos numéricos
        
    def load_data(self):
        """
        Carga y realiza limpieza inicial de los datos
        Maneja tanto backup.csv (original) como backup1.csv (códigos numéricos)
        
        Returns:
            pd.DataFrame: DataFrame con los datos cargados
        """
        try:
            # Detectar el tipo de archivo y delimitador
            if 'backup1' in self.data_path:
                # Nuevo formato con códigos numéricos
                self.df = pd.read_csv(self.data_path, sep=';', encoding='utf-8', low_memory=False, on_bad_lines='skip')
                self.dataset_type = 'backup1'
            else:
                # Formato original
                self.df = pd.read_csv(self.data_path, sep=';', encoding='utf-8')
                self.dataset_type = 'backup'
            
            # Limpieza inicial de nombres de columnas
            self.df.columns = self.df.columns.str.strip()
            
            # Información básica del dataset
            print(f"Dataset cargado exitosamente: {self.df.shape[0]} filas, {self.df.shape[1]} columnas")
            print(f"Tipo de dataset: {self.dataset_type}")
            print(f"Columnas principales: {list(self.df.columns[:10])}")
            
            # Análisis específico por tipo de dataset
            if self.dataset_type == 'backup1':
                # Para backup1.csv, convertir Status a numérico
                if 'Status' in self.df.columns:
                    self.df['Status_Numeric'] = pd.to_numeric(self.df['Status'], errors='coerce')
                    # Crear variable target: 0 = éxito, >0 = error
                    self.df['Has_Error'] = (self.df['Status_Numeric'] > 0).astype(int)
                    print(f"Jobs exitosos (Status=0): {sum(self.df['Status_Numeric'] == 0):,}")
                    print(f"Jobs con error (Status>0): {sum(self.df['Status_Numeric'] > 0):,}")
            
            return self.df
            
        except Exception as e:
            print(f"Error cargando datos: {e}")
            return None
    
    def exploratory_analysis(self):
        """
        Realiza análisis exploratorio de datos adaptado al tipo de dataset
        
        Returns:
            dict: Diccionario con estadísticas y análisis
        """
        if self.df is None:
            print("Error: Debe cargar los datos primero")
            return None
            
        analysis = {}
        
        # Estadísticas básicas
        analysis['shape'] = self.df.shape
        analysis['missing_values'] = self.df.isnull().sum()
        analysis['data_types'] = self.df.dtypes
        
        # Análisis específico por tipo de dataset
        if self.dataset_type == 'backup1':
            # Para backup1.csv con códigos numéricos
            categorical_cols = ['Type', 'State', 'Job Policy', 'Media Server', 'Job Schedule']
            
            # Análisis de códigos de status
            if 'Status_Numeric' in self.df.columns:
                analysis['status_distribution'] = self.df['Status_Numeric'].value_counts().sort_index()
                analysis['error_rate'] = (self.df['Status_Numeric'] > 0).mean() * 100
                analysis['success_rate'] = (self.df['Status_Numeric'] == 0).mean() * 100
                
                # Códigos de error más frecuentes
                error_codes = self.df[self.df['Status_Numeric'] > 0]['Status_Numeric'].value_counts()
                analysis['top_error_codes'] = error_codes.head(10)
        else:
            # Para backup.csv original
            categorical_cols = ['Type', 'State', 'Status', 'Job Policy', 'Media Server', 'Job Schedule']
        
        # Análisis por columnas categóricas
        for col in categorical_cols:
            if col in self.df.columns:
                analysis[f'{col}_counts'] = self.df[col].value_counts()
        
        # Crear variable objetivo: Jobs con problema (si no son Active o Queued)
        self.df['has_error'] = ~self.df['State'].isin(['Active', 'Queued'])
        analysis['error_distribution'] = self.df['has_error'].value_counts()
        
        print("\\n=== ANÁLISIS EXPLORATORIO ===")
        print(f"Total de jobs: {analysis['shape'][0]}")
        print(f"Jobs con error: {analysis['error_distribution'].get(True, 0)}")
        print(f"Jobs sin error: {analysis['error_distribution'].get(False, 0)}")
        
        return analysis
    
    def create_features(self):
        """
        Crea features para el modelo de ML a partir de los datos originales
        
        Returns:
            pd.DataFrame: DataFrame con features procesadas
        """
        if self.df is None:
            print("Error: Debe cargar los datos primero")
            return None
            
        # Crear copia para procesamiento
        df_features = self.df.copy()
        
        # Procesar campo de tiempo
        if 'Start Time' in df_features.columns:
            # Extraer componentes de tiempo
            try:
                df_features['start_hour'] = pd.to_datetime(df_features['Start Time'], errors='coerce').dt.hour
                df_features['start_day_of_week'] = pd.to_datetime(df_features['Start Time'], errors='coerce').dt.dayofweek
            except:
                df_features['start_hour'] = 23  # Valor por defecto
                df_features['start_day_of_week'] = 1  # Valor por defecto
        
        # Procesar KB/Sec como feature numérica
        if 'KB/Sec' in df_features.columns:
            df_features['kb_sec_numeric'] = pd.to_numeric(df_features['KB/Sec'], errors='coerce').fillna(0)
            # Crear categorías de velocidad
            df_features['speed_category'] = pd.cut(df_features['kb_sec_numeric'], 
                                                 bins=[-1, 0, 10, 50, 100, np.inf], 
                                                 labels=['No_Speed', 'Low', 'Medium', 'High', 'Very_High'])
        
        # Procesar Kilobytes
        if 'Kilobytes' in df_features.columns:
            df_features['kilobytes_numeric'] = pd.to_numeric(df_features['Kilobytes'], errors='coerce').fillna(0)
            # Crear categorías de tamaño
            df_features['size_category'] = pd.cut(df_features['kilobytes_numeric'], 
                                                bins=[-1, 0, 1000000, 10000000, 100000000, np.inf], 
                                                labels=['No_Size', 'Small', 'Medium', 'Large', 'Very_Large'])
        
        # Variable objetivo
        df_features['has_error'] = ~df_features['State'].isin(['Active', 'Queued'])
        
        # Seleccionar features categóricas importantes
        categorical_features = ['Type', 'Job Policy', 'Media Server', 'Job Schedule', 'speed_category', 'size_category']
        numerical_features = ['start_hour', 'start_day_of_week', 'kb_sec_numeric', 'kilobytes_numeric']
        
        # Rellenar valores faltantes en categóricas
        for col in categorical_features:
            if col in df_features.columns:
                df_features[col] = df_features[col].fillna('Unknown')
        
        # Rellenar valores faltantes en numéricas
        for col in numerical_features:
            if col in df_features.columns:
                df_features[col] = df_features[col].fillna(0)
        
        self.df_processed = df_features
        return df_features
    
    def prepare_ml_data(self):
        """
        Prepara los datos para machine learning
        
        Returns:
            tuple: X, y para entrenamiento
        """
        if self.df_processed is None:
            self.create_features()
        
        # Seleccionar features
        feature_columns = ['Type', 'Job Policy', 'Media Server', 'Job Schedule', 
                          'speed_category', 'size_category', 'start_hour', 
                          'start_day_of_week', 'kb_sec_numeric', 'kilobytes_numeric']
        
        # Filtrar columnas que existen
        existing_features = [col for col in feature_columns if col in self.df_processed.columns]
        
        X = self.df_processed[existing_features].copy()
        y = self.df_processed['has_error']
        
        # Codificar variables categóricas
        categorical_columns = ['Type', 'Job Policy', 'Media Server', 'Job Schedule', 'speed_category', 'size_category']
        
        for col in categorical_columns:
            if col in X.columns:
                if col not in self.label_encoders:
                    self.label_encoders[col] = LabelEncoder()
                X[col] = self.label_encoders[col].fit_transform(X[col].astype(str))
        
        # Normalizar features numéricas
        numerical_columns = ['start_hour', 'start_day_of_week', 'kb_sec_numeric', 'kilobytes_numeric']
        numerical_columns = [col for col in numerical_columns if col in X.columns]
        
        if numerical_columns:
            X[numerical_columns] = self.scaler.fit_transform(X[numerical_columns])
        
        self.features = X
        self.target = y
        
        return X, y
    
    def train_models(self):
        """
        Entrena múltiples modelos de ML y selecciona el mejor
        
        Returns:
            dict: Resultados de evaluación de modelos
        """
        if self.features is None or self.target is None:
            X, y = self.prepare_ml_data()
        else:
            X, y = self.features, self.target
        
        # Dividir datos
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
        
        # Modelos a evaluar
        models = {
            'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42, max_depth=10),
            'Gradient Boosting': GradientBoostingClassifier(random_state=42, max_depth=5),
            'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000)
        }
        
        results = {}
        
        print("\\n=== ENTRENAMIENTO DE MODELOS ===")
        
        for name, model in models.items():
            print(f"\\nEntrenando {name}...")
            
            # Entrenar modelo
            model.fit(X_train, y_train)
            
            # Predecir
            y_pred = model.predict(X_test)
            
            # Evaluar
            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred, average='weighted')
            recall = recall_score(y_test, y_pred, average='weighted')
            f1 = f1_score(y_test, y_pred, average='weighted')
            
            results[name] = {
                'model': model,
                'accuracy': accuracy,
                'precision': precision,
                'recall': recall,
                'f1_score': f1,
                'y_test': y_test,
                'y_pred': y_pred
            }
            
            print(f"Accuracy: {accuracy:.4f}")
            print(f"Precision: {precision:.4f}")
            print(f"Recall: {recall:.4f}")
            print(f"F1-Score: {f1:.4f}")
        
        # Seleccionar mejor modelo (basado en F1-score)
        best_model_name = max(results.keys(), key=lambda k: results[k]['f1_score'])
        self.model = results[best_model_name]['model']
        
        print(f"\\n✅ Mejor modelo seleccionado: {best_model_name}")
        print(f"F1-Score: {results[best_model_name]['f1_score']:.4f}")
        
        # Guardar modelo
        self.save_model()
        
        return results
    
    def save_model(self):
        """Guarda el modelo entrenado y los encoders"""
        if self.model is not None:
            joblib.dump(self.model, 'models/backup_predictor_model.pkl')
            joblib.dump(self.label_encoders, 'models/label_encoders.pkl')
            joblib.dump(self.scaler, 'models/scaler.pkl')
            print("✅ Modelo guardado exitosamente")
    
    def load_model(self):
        """Carga un modelo previamente entrenado"""
        try:
            self.model = joblib.load('models/backup_predictor_model.pkl')
            self.label_encoders = joblib.load('models/label_encoders.pkl')
            self.scaler = joblib.load('models/scaler.pkl')
            print("✅ Modelo cargado exitosamente")
            return True
        except:
            print("❌ No se pudo cargar el modelo")
            return False
    
    def predict_job_error(self, job_data):
        """
        Predice si un job tendrá error
        
        Args:
            job_data (dict): Diccionario con datos del job
            
        Returns:
            dict: Predicción y probabilidad
        """
        if self.model is None:
            return {"error": "Modelo no entrenado"}
        
        # Crear DataFrame con los datos
        df_pred = pd.DataFrame([job_data])
        
        # Aplicar mismas transformaciones que en entrenamiento
        for col, encoder in self.label_encoders.items():
            if col in df_pred.columns:
                try:
                    df_pred[col] = encoder.transform(df_pred[col].astype(str))
                except:
                    df_pred[col] = 0  # Valor por defecto para categorías no vistas
        
        # Normalizar features numéricas
        numerical_columns = ['start_hour', 'start_day_of_week', 'kb_sec_numeric', 'kilobytes_numeric']
        numerical_columns = [col for col in numerical_columns if col in df_pred.columns]
        
        if numerical_columns:
            df_pred[numerical_columns] = self.scaler.transform(df_pred[numerical_columns])
        
        # Predecir
        prediction = self.model.predict(df_pred)[0]
        probability = self.model.predict_proba(df_pred)[0]
        
        return {
            "prediction": bool(prediction),
            "probability_error": probability[1] if len(probability) > 1 else 0,
            "probability_success": probability[0] if len(probability) > 1 else 1
        }
    
    def create_visualizations(self):
        """
        Crea visualizaciones con Plotly
        
        Returns:
            dict: Diccionario con las figuras de Plotly
        """
        if self.df is None:
            return {}
        
        figures = {}
        
        # 1. Distribución de estados de jobs
        fig1 = px.pie(
            self.df, 
            names='State', 
            title='Distribución de Estados de Jobs de Backup',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig1.update_layout(height=500)
        figures['state_distribution'] = fig1.to_html(full_html=False, include_plotlyjs='cdn')
        
        # 2. Jobs por tipo
        type_counts = self.df['Type'].value_counts()
        fig2 = px.bar(
            x=type_counts.index, 
            y=type_counts.values,
            title='Distribución de Tipos de Jobs',
            labels={'x': 'Tipo de Job', 'y': 'Cantidad'},
            color=type_counts.values,
            color_continuous_scale='viridis'
        )
        fig2.update_layout(height=500)
        figures['type_distribution'] = fig2.to_html(full_html=False, include_plotlyjs='cdn')
        
        # 3. Análisis temporal por hora
        if 'Start Time' in self.df.columns:
            try:
                self.df['start_hour'] = pd.to_datetime(self.df['Start Time'], errors='coerce').dt.hour
                hourly_counts = self.df.groupby('start_hour').size()
                
                fig3 = px.line(
                    x=hourly_counts.index, 
                    y=hourly_counts.values,
                    title='Distribución de Jobs por Hora del Día',
                    labels={'x': 'Hora', 'y': 'Número de Jobs'}
                )
                fig3.update_layout(height=500)
                figures['hourly_distribution'] = fig3.to_html(full_html=False, include_plotlyjs='cdn')
            except:
                pass
        
        # 4. Análisis de velocidad de backup (KB/Sec)
        if 'KB/Sec' in self.df.columns:
            kb_sec_numeric = pd.to_numeric(self.df['KB/Sec'], errors='coerce').dropna()
            if len(kb_sec_numeric) > 0:
                fig4 = px.histogram(
                    kb_sec_numeric,
                    nbins=50,
                    title='Distribución de Velocidad de Backup (KB/Sec)',
                    labels={'value': 'KB/Sec', 'count': 'Frecuencia'}
                )
                fig4.update_layout(height=500)
                figures['speed_distribution'] = fig4.to_html(full_html=False, include_plotlyjs='cdn')
        
        # 5. Jobs por Media Server
        if 'Media Server' in self.df.columns:
            server_counts = self.df['Media Server'].value_counts().head(10)
            fig5 = px.bar(
                x=server_counts.values,
                y=server_counts.index,
                orientation='h',
                title='Top 10 Media Servers por Número de Jobs',
                labels={'x': 'Número de Jobs', 'y': 'Media Server'}
            )
            fig5.update_layout(height=600)
            figures['server_distribution'] = fig5.to_html(full_html=False, include_plotlyjs='cdn')
        
        return figures

def main():
    """Función principal para testing"""
    analyzer = BackupJobAnalyzer()
    
    # Cargar y analizar datos
    analyzer.load_data()
    analysis = analyzer.exploratory_analysis()
    
    if analysis:
        # Crear features y entrenar modelos
        analyzer.create_features()
        results = analyzer.train_models()
        
        # Crear visualizaciones
        figures = analyzer.create_visualizations()
        
        print("\\n✅ Análisis completado exitosamente")
        print(f"Visualizaciones creadas: {len(figures)}")

if __name__ == "__main__":
    main()
