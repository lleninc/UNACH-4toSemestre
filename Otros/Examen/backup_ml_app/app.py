"""
Aplicación Flask para Análisis y Predicción de Jobs de Backup
Autor: [Tu Nombre]
Descripción: Sistema web para análisis exploratorio, entrenamiento de modelos ML y predicción de jobs con error

Funcionalidades:
- Análisis exploratorio de datos con visualizaciones interactivas
- Entrenamiento de modelos de Machine Learning
- Predicción de jobs con probabilidad de error
- Dashboard interactivo con métricas y gráficos
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import os
import json
from data_analysis import BackupJobAnalyzer
import pandas as pd
from chatbot_routes import register_chatbot_routes

# Configuración de la aplicación Flask
app = Flask(__name__)
app.secret_key = 'backup_ml_secret_key_2025'  # Cambiar en producción

# Instancia global del analizador
analyzer = BackupJobAnalyzer()

# Registrar rutas del chatbot
register_chatbot_routes(app)

@app.route('/')
def index():
    """
    Página principal con dashboard
    """
    return render_template('index.html')

@app.route('/analysis')
def analysis():
    """
    Página de análisis exploratorio
    """
    try:
        # Cargar datos si no están cargados
        if analyzer.df is None:
            analyzer.load_data()
        
        # Realizar análisis exploratorio
        analysis_results = analyzer.exploratory_analysis()
        
        # Crear visualizaciones
        figures = analyzer.create_visualizations()
        
        # Preparar estadísticas para la plantilla
        stats = {
            'total_jobs': analysis_results['shape'][0] if analysis_results else 0,
            'total_errors': analysis_results['error_distribution'].get(True, 0) if analysis_results else 0,
            'error_rate': round((analysis_results['error_distribution'].get(True, 0) / analysis_results['shape'][0]) * 100, 2) if analysis_results and analysis_results['shape'][0] > 0 else 0,
            'data_columns': len(analysis_results['shape']) if analysis_results else 0
        }
        
        return render_template('analysis.html', 
                             figures=figures, 
                             stats=stats,
                             analysis_results=analysis_results)
    
    except Exception as e:
        flash(f'Error en el análisis: {str(e)}', 'error')
        return render_template('analysis.html', figures={}, stats={}, analysis_results=None)

@app.route('/train')
def train():
    """
    Página de entrenamiento de modelos
    """
    return render_template('train.html')

@app.route('/train_models', methods=['POST'])
def train_models():
    """
    Endpoint para entrenar los modelos de ML
    """
    try:
        # Cargar datos si no están cargados
        if analyzer.df is None:
            analyzer.load_data()
        
        # Entrenar modelos
        results = analyzer.train_models()
        
        # Formatear resultados para JSON
        formatted_results = {}
        for model_name, result in results.items():
            formatted_results[model_name] = {
                'accuracy': round(result['accuracy'], 4),
                'precision': round(result['precision'], 4),
                'recall': round(result['recall'], 4),
                'f1_score': round(result['f1_score'], 4)
            }
        
        flash('Modelos entrenados exitosamente', 'success')
        return jsonify({
            'status': 'success',
            'message': 'Modelos entrenados exitosamente',
            'results': formatted_results
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Error entrenando modelos: {str(e)}'
        })

@app.route('/predict')
def predict():
    """
    Página de predicciones
    """
    return render_template('predict.html')

@app.route('/make_prediction', methods=['POST'])
def make_prediction():
    """
    Endpoint para hacer predicciones
    """
    try:
        # Obtener datos del formulario
        job_data = {
            'Type': request.form.get('type', 'Backup'),
            'Job Policy': request.form.get('job_policy', 'Unknown'),
            'Media Server': request.form.get('media_server', 'Unknown'),
            'Job Schedule': request.form.get('job_schedule', 'Unknown'),
            'start_hour': int(request.form.get('start_hour', 23)),
            'start_day_of_week': int(request.form.get('start_day_of_week', 1)),
            'kb_sec_numeric': float(request.form.get('kb_sec', 0)),
            'kilobytes_numeric': float(request.form.get('kilobytes', 0)),
            'speed_category': request.form.get('speed_category', 'No_Speed'),
            'size_category': request.form.get('size_category', 'No_Size')
        }
        
        # Cargar modelo si no está cargado
        if analyzer.model is None:
            model_loaded = analyzer.load_model()
            if not model_loaded:
                return jsonify({
                    'status': 'error',
                    'message': 'Modelo no disponible. Debe entrenar el modelo primero.'
                })
        
        # Hacer predicción
        prediction_result = analyzer.predict_job_error(job_data)
        
        return jsonify({
            'status': 'success',
            'prediction': prediction_result,
            'job_data': job_data
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Error en predicción: {str(e)}'
        })

@app.route('/api/data_summary')
def data_summary():
    """
    API endpoint para obtener resumen de datos
    """
    try:
        if analyzer.df is None:
            analyzer.load_data()
        
        summary = {
            'total_records': len(analyzer.df),
            'columns': list(analyzer.df.columns),
            'sample_data': analyzer.df.head().to_dict('records')
        }
        
        return jsonify(summary)
    
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/api/model_status')
def model_status():
    """
    API endpoint para verificar estado del modelo
    """
    try:
        model_exists = os.path.exists('models/backup_predictor_model.pkl')
        model_loaded = analyzer.model is not None
        
        return jsonify({
            'model_exists': model_exists,
            'model_loaded': model_loaded,
            'status': 'ready' if model_loaded else 'not_ready'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/documentation')
def documentation():
    """
    Página de documentación del proyecto
    """
    return render_template('documentation.html')

@app.errorhandler(404)
def not_found_error(error):
    """Manejo de errores 404"""
    return render_template('error.html', error_code=404, error_message="Página no encontrada"), 404

@app.errorhandler(500)
def internal_error(error):
    """Manejo de errores 500"""
    return render_template('error.html', error_code=500, error_message="Error interno del servidor"), 500

# Configuración para desarrollo
if __name__ == '__main__':
    # Crear directorio de modelos si no existe
    os.makedirs('models', exist_ok=True)
    
    print("🚀 Iniciando aplicación Flask...")
    print("📊 Sistema de Análisis de Jobs de Backup")
    print("🔗 Acceder en: http://localhost:5000")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
