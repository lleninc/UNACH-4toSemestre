#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ANÁLISIS MACHINE LEARNING COMPLETO PARA BACKUP1.CSV
Sistema de Predicción de Errores en Jobs de Backup
Universidad Nacional de Chimborazo

Este script realiza análisis completo de ML en backup1.csv:
- Status = 0: Job satisfactorio (éxito) 
- Status > 0: Diferentes códigos de error

Funcionalidades:
1. Análisis exploratorio de datos completo
2. Feature engineering avanzado
3. Entrenamiento de múltiples modelos ML
4. Evaluación y comparación de modelos
5. Predicciones y recomendaciones
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import joblib
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

class BackupJobMLAnalyzer:
    """
    Analizador ML completo para jobs de backup con códigos numéricos
    """
    
    def __init__(self, data_path='backup1.csv'):
        self.data_path = data_path
        self.df = None
        self.df_processed = None
        self.models = {}
        self.label_encoders = {}
        self.scaler = StandardScaler()
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.best_model = None
        
    def load_and_explore_data(self):
        """Carga y explora el dataset"""
        print("=" * 60)
        print("🔍 ANÁLISIS ML COMPLETO - BACKUP1.CSV")
        print("=" * 60)
        
        try:
            print("📂 Cargando dataset...")
            self.df = pd.read_csv(self.data_path, sep=';', encoding='utf-8', low_memory=False, on_bad_lines='skip')
            
            print(f"✅ Dataset cargado: {len(self.df)} registros, {len(self.df.columns)} columnas")
            
            # Limpieza de columnas
            self.df.columns = self.df.columns.str.strip()
            
            # Procesamiento específico para backup1.csv
            if 'Status' in self.df.columns:
                self.df['Status_Numeric'] = pd.to_numeric(self.df['Status'], errors='coerce')
                self.df['Has_Error'] = (self.df['Status_Numeric'] > 0).astype(int)
                
                # Estadísticas básicas
                valid_status = self.df['Status_Numeric'].dropna()
                success_jobs = sum(valid_status == 0)
                error_jobs = sum(valid_status > 0)
                
                print(f"\n📊 DISTRIBUCIÓN DE STATUS:")
                print(f"✅ Jobs exitosos (Status=0): {success_jobs:,} ({(success_jobs/len(valid_status))*100:.1f}%)")
                print(f"❌ Jobs con error (Status>0): {error_jobs:,} ({(error_jobs/len(valid_status))*100:.1f}%)")
                print(f"📈 Tasa de error: {(error_jobs/len(valid_status))*100:.2f}%")
                
                # Códigos de error más frecuentes
                if error_jobs > 0:
                    error_codes = self.df[self.df['Status_Numeric'] > 0]['Status_Numeric'].value_counts().head(10)
                    print(f"\n🔢 TOP 10 CÓDIGOS DE ERROR:")
                    for code, count in error_codes.items():
                        print(f"  Error {int(code)}: {count:,} jobs")
            
            # Análisis de columnas disponibles
            print(f"\n📋 COLUMNAS DISPONIBLES:")
            for i, col in enumerate(self.df.columns[:15]):  # Mostrar primeras 15
                print(f"  {i+1:2d}. {col}")
            if len(self.df.columns) > 15:
                print(f"  ... y {len(self.df.columns)-15} columnas más")
            
            return True
            
        except Exception as e:
            print(f"❌ Error cargando datos: {e}")
            return False
    
    def feature_engineering(self):
        """Ingeniería de características específica para backup jobs"""
        print(f"\n🔧 FEATURE ENGINEERING")
        print("-" * 30)
        
        # Crear copia para procesamiento
        self.df_processed = self.df.copy()
        
        # Features basadas en tiempo
        time_columns = ['Start Time', 'End Time']
        for col in time_columns:
            if col in self.df_processed.columns:
                try:
                    # Convertir a datetime
                    self.df_processed[f'{col}_dt'] = pd.to_datetime(self.df_processed[col], errors='coerce')
                    
                    # Extraer características temporales
                    self.df_processed[f'{col}_hour'] = self.df_processed[f'{col}_dt'].dt.hour
                    self.df_processed[f'{col}_day_of_week'] = self.df_processed[f'{col}_dt'].dt.dayofweek
                    self.df_processed[f'{col}_is_weekend'] = (self.df_processed[f'{col}_dt'].dt.dayofweek >= 5).astype(int)
                    
                    print(f"✅ Features temporales creados para {col}")
                except Exception as e:
                    print(f"⚠️ Error procesando {col}: {e}")
        
        # Features categóricas
        categorical_features = ['Type', 'State', 'Job Policy', 'Media Server', 'Job Schedule']
        for col in categorical_features:
            if col in self.df_processed.columns:
                # Limpiar y normalizar
                self.df_processed[col] = self.df_processed[col].astype(str).str.strip()
                self.df_processed[col] = self.df_processed[col].replace(['nan', 'NaN', ''], 'Unknown')
                
                # Label encoding
                le = LabelEncoder()
                self.df_processed[f'{col}_encoded'] = le.fit_transform(self.df_processed[col])
                self.label_encoders[col] = le
                
                print(f"✅ Encoding aplicado a {col} ({len(le.classes_)} categorías)")
        
        # Features numéricos
        numeric_features = ['KB/Sec', 'Kilobytes', '% Complete (Estimated)']
        for col in numeric_features:
            if col in self.df_processed.columns:
                # Convertir a numérico y manejar valores faltantes
                self.df_processed[f'{col}_numeric'] = pd.to_numeric(self.df_processed[col], errors='coerce')
                self.df_processed[f'{col}_numeric'] = self.df_processed[f'{col}_numeric'].fillna(0)
                
                print(f"✅ Feature numérico procesado: {col}")
        
        # Feature de duración del job (si disponible)
        if 'Start Time_dt' in self.df_processed.columns and 'End Time_dt' in self.df_processed.columns:
            self.df_processed['job_duration_minutes'] = (
                self.df_processed['End Time_dt'] - self.df_processed['Start Time_dt']
            ).dt.total_seconds() / 60
            self.df_processed['job_duration_minutes'] = self.df_processed['job_duration_minutes'].fillna(0)
            print(f"✅ Feature de duración creado")
        
        print(f"🔧 Feature engineering completado. Dataset procesado: {self.df_processed.shape}")
        
    def prepare_ml_dataset(self):
        """Prepara el dataset para Machine Learning"""
        print(f"\n🤖 PREPARACIÓN PARA MACHINE LEARNING")
        print("-" * 40)
        
        # Definir features para ML
        feature_columns = []
        
        # Features categóricas encodificadas
        categorical_features = ['Type', 'State', 'Job Policy', 'Media Server', 'Job Schedule']
        for col in categorical_features:
            if f'{col}_encoded' in self.df_processed.columns:
                feature_columns.append(f'{col}_encoded')
        
        # Features temporales
        time_features = [
            'Start Time_hour', 'Start Time_day_of_week', 'Start Time_is_weekend',
            'End Time_hour', 'End Time_day_of_week', 'End Time_is_weekend'
        ]
        for col in time_features:
            if col in self.df_processed.columns:
                feature_columns.append(col)
        
        # Features numéricos
        numeric_features = ['KB/Sec_numeric', 'Kilobytes_numeric', '% Complete (Estimated)_numeric', 'job_duration_minutes']
        for col in numeric_features:
            if col in self.df_processed.columns:
                feature_columns.append(col)
        
        # Variable target
        if 'Has_Error' not in self.df_processed.columns:
            print("❌ Error: Variable target 'Has_Error' no encontrada")
            return False
        
        # Filtrar datos válidos
        valid_data = self.df_processed.dropna(subset=['Has_Error'])
        
        if len(feature_columns) == 0:
            print("❌ Error: No se encontraron features válidos")
            return False
        
        print(f"📊 Features seleccionados: {len(feature_columns)}")
        for i, feat in enumerate(feature_columns):
            print(f"  {i+1:2d}. {feat}")
        
        # Crear matrices X e y
        X = valid_data[feature_columns].fillna(0)
        y = valid_data['Has_Error']
        
        print(f"\n📈 Dataset ML preparado:")
        print(f"  Samples: {len(X):,}")
        print(f"  Features: {len(feature_columns)}")
        print(f"  Clase 0 (éxito): {sum(y==0):,} ({(sum(y==0)/len(y))*100:.1f}%)")
        print(f"  Clase 1 (error): {sum(y==1):,} ({(sum(y==1)/len(y))*100:.1f}%)")
        
        # Split train/test
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Escalar features
        self.X_train_scaled = self.scaler.fit_transform(self.X_train)
        self.X_test_scaled = self.scaler.transform(self.X_test)
        
        print(f"✅ Train set: {len(self.X_train):,} samples")
        print(f"✅ Test set: {len(self.X_test):,} samples")
        
        return True
    
    def train_models(self):
        """Entrena múltiples modelos de Machine Learning"""
        print(f"\n🎯 ENTRENAMIENTO DE MODELOS")
        print("-" * 35)
        
        # Definir modelos
        models_config = {
            'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1),
            'Gradient Boosting': GradientBoostingClassifier(n_estimators=100, random_state=42),
            'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
            'SVM': SVC(random_state=42, probability=True)
        }
        
        results = {}
        
        for name, model in models_config.items():
            print(f"\n🔄 Entrenando {name}...")
            
            try:
                # Seleccionar datos apropiados para cada modelo
                if name in ['Logistic Regression', 'SVM']:
                    X_train_use = self.X_train_scaled
                    X_test_use = self.X_test_scaled
                else:
                    X_train_use = self.X_train
                    X_test_use = self.X_test
                
                # Entrenar modelo
                model.fit(X_train_use, self.y_train)
                
                # Predicciones
                y_pred = model.predict(X_test_use)
                y_pred_proba = model.predict_proba(X_test_use)[:, 1]
                
                # Métricas
                accuracy = accuracy_score(self.y_test, y_pred)
                precision = precision_score(self.y_test, y_pred)
                recall = recall_score(self.y_test, y_pred)
                f1 = f1_score(self.y_test, y_pred)
                auc = roc_auc_score(self.y_test, y_pred_proba)
                
                # Cross-validation
                cv_scores = cross_val_score(model, X_train_use, self.y_train, cv=5, scoring='f1')
                
                results[name] = {
                    'model': model,
                    'accuracy': accuracy,
                    'precision': precision,
                    'recall': recall,
                    'f1_score': f1,
                    'auc': auc,
                    'cv_mean': cv_scores.mean(),
                    'cv_std': cv_scores.std()
                }
                
                print(f"✅ {name}:")
                print(f"  Accuracy: {accuracy:.3f}")
                print(f"  Precision: {precision:.3f}")
                print(f"  Recall: {recall:.3f}")
                print(f"  F1-Score: {f1:.3f}")
                print(f"  AUC: {auc:.3f}")
                print(f"  CV F1: {cv_scores.mean():.3f} ± {cv_scores.std():.3f}")
                
            except Exception as e:
                print(f"❌ Error entrenando {name}: {e}")
        
        self.models = results
        
        # Seleccionar mejor modelo
        if results:
            best_model_name = max(results.keys(), key=lambda x: results[x]['f1_score'])
            self.best_model = results[best_model_name]['model']
            
            print(f"\n🏆 MEJOR MODELO: {best_model_name}")
            print(f"  F1-Score: {results[best_model_name]['f1_score']:.3f}")
            
            # Guardar mejor modelo
            joblib.dump(self.best_model, 'best_backup_model.pkl')
            joblib.dump(self.scaler, 'backup_scaler.pkl')
            print(f"💾 Modelo guardado como 'best_backup_model.pkl'")
        
        return results
    
    def generate_insights(self):
        """Genera insights y recomendaciones"""
        print(f"\n💡 INSIGHTS Y RECOMENDACIONES")
        print("-" * 40)
        
        if not self.models:
            print("❌ No hay modelos entrenados")
            return
        
        # Análisis de importancia de features (Random Forest)
        if 'Random Forest' in self.models:
            rf_model = self.models['Random Forest']['model']
            feature_importance = rf_model.feature_importances_
            feature_names = self.X_train.columns
            
            importance_df = pd.DataFrame({
                'feature': feature_names,
                'importance': feature_importance
            }).sort_values('importance', ascending=False)
            
            print("🔍 TOP 10 FEATURES MÁS IMPORTANTES:")
            for i, row in importance_df.head(10).iterrows():
                print(f"  {row['feature']}: {row['importance']:.3f}")
        
        # Recomendaciones basadas en análisis
        print(f"\n🎯 RECOMENDACIONES:")
        
        # Basado en tasa de error
        if hasattr(self, 'df_processed'):
            error_rate = self.df_processed['Has_Error'].mean() * 100
            
            if error_rate < 1:
                print("✅ Excelente tasa de éxito (>99%)")
                print("  → Mantener configuraciones actuales")
                print("  → Implementar monitoreo preventivo")
            elif error_rate < 5:
                print("⚠️ Tasa de error aceptable (<5%)")
                print("  → Revisar códigos de error más frecuentes")
                print("  → Optimizar jobs problemáticos")
            else:
                print("🚨 Alta tasa de error (≥5%)")
                print("  → Revisión urgente de configuraciones")
                print("  → Análisis detallado de causas raíz")
        
        # Mejor estrategia de predicción
        best_f1 = max([m['f1_score'] for m in self.models.values()])
        print(f"\n📈 CAPACIDAD PREDICTIVA:")
        print(f"  F1-Score del mejor modelo: {best_f1:.3f}")
        
        if best_f1 > 0.8:
            print("  → Excelente capacidad predictiva")
            print("  → Implementar sistema en producción")
        elif best_f1 > 0.6:
            print("  → Buena capacidad predictiva")
            print("  → Refinar modelo con más datos")
        else:
            print("  → Capacidad predictiva limitada")
            print("  → Recopilar más features relevantes")
    
    def run_complete_analysis(self):
        """Ejecuta análisis completo"""
        success = True
        
        success &= self.load_and_explore_data()
        if not success:
            return False
        
        self.feature_engineering()
        
        success &= self.prepare_ml_dataset()
        if not success:
            return False
        
        self.train_models()
        self.generate_insights()
        
        print(f"\n🎉 ANÁLISIS ML COMPLETADO EXITOSAMENTE")
        print("=" * 60)
        
        return True

def main():
    """Función principal"""
    analyzer = BackupJobMLAnalyzer('backup1.csv')
    analyzer.run_complete_analysis()

if __name__ == "__main__":
    main()
