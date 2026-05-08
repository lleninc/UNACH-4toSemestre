"""
Aplicación Flask simplificada para demostración
Esta versión funciona sin todas las dependencias de ML para testing inicial
"""

from flask import Flask, render_template, request, jsonify
import json
import csv
from collections import Counter
import os

app = Flask(__name__)
app.secret_key = 'backup_ml_demo_key'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'data', 'backup.csv')

# Datos globales (en memoria para demo)
backup_data = []
analysis_cache = {}

def load_data():
    """Carga los datos de backup"""
    global backup_data
    
    if backup_data:  # Ya cargados
        return backup_data
    
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            backup_data = list(reader)
        return backup_data
    except Exception as e:
        print(f"⚠️  No se pudo cargar el archivo de datos '{DATA_FILE}': {e}")
        return []

def analyze_data():
    """Análisis básico de datos"""
    global analysis_cache
    
    if analysis_cache:  # Ya analizado
        return analysis_cache
    
    data = load_data()
    
    if not data:
        return {}
    
    # Estados de jobs
    states = Counter(job['State'] for job in data)
    
    # Tipos de jobs
    types = Counter(job['Type'] for job in data)
    
    # Para este dataset, "Done" significa completado exitosamente
    # Los problemas serían otros estados como errores específicos
    error_states = ['Failed', 'Error', 'Terminated', 'Cancelled']
    problem_jobs = [job for job in data if job['State'] in error_states]
    
    # Media servers
    servers = Counter(job['Media Server'] for job in data if job['Media Server'])
    
    analysis_cache = {
        'total_jobs': len(data),
        'states': dict(states),
        'types': dict(types),
        'problem_jobs': len(problem_jobs),
        'problem_rate': (len(problem_jobs) / len(data)) * 100 if data else 0,
        'top_servers': dict(servers.most_common(10))
    }
    
    return analysis_cache

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/analysis')
def analysis():
    """Página de análisis"""
    
    # Análisis básico
    analysis_results = analyze_data()
    
    # Estadísticas para la plantilla
    stats = {
        'total_jobs': analysis_results.get('total_jobs', 0),
        'total_errors': analysis_results.get('problem_jobs', 0),
        'error_rate': round(analysis_results.get('problem_rate', 0), 2),
        'data_columns': 13  # Número fijo de columnas
    }
    
    # Crear visualizaciones básicas (HTML simple)
    figures = create_basic_visualizations(analysis_results)
    
    return render_template('analysis.html', 
                         figures=figures, 
                         stats=stats,
                         analysis_results=analysis_results)

@app.route('/train')
def train():
    """Página de entrenamiento"""
    return render_template('train.html')

@app.route('/predict')
def predict():
    """Página de predicción"""
    return render_template('predict.html')

@app.route('/documentation')
def documentation():
    """Página de documentación"""
    return render_template('documentation.html')

@app.route('/train_models', methods=['POST'])
def train_models():
    """Simula entrenamiento de modelos"""
    
    # Simulación de entrenamiento
    results = {
        'Random Forest': {
            'accuracy': 0.8945,
            'precision': 0.8723,
            'recall': 0.9012,
            'f1_score': 0.8865
        },
        'Gradient Boosting': {
            'accuracy': 0.8712,
            'precision': 0.8534,
            'recall': 0.8890,
            'f1_score': 0.8709
        },
        'Logistic Regression': {
            'accuracy': 0.7834,
            'precision': 0.7651,
            'recall': 0.8023,
            'f1_score': 0.7833
        }
    }
    
    return jsonify({
        'status': 'success',
        'message': 'Modelos entrenados exitosamente (simulación)',
        'results': results
    })

@app.route('/make_prediction', methods=['POST'])
def make_prediction():
    """Simula predicción de job"""
    
    # Obtener datos del formulario
    job_data = request.form.to_dict()
    
    # Simulación de predicción basada en reglas simples
    risk_score = 0
    
    # Factores de riesgo
    if int(job_data.get('start_hour', 12)) in range(8, 18):  # Horario laboral
        risk_score += 0.3
    
    if job_data.get('speed_category') in ['No_Speed', 'Low']:
        risk_score += 0.4
    
    if job_data.get('size_category') in ['Large', 'Very_Large']:
        risk_score += 0.2
    
    if 'unknown' in job_data.get('media_server', '').lower():
        risk_score += 0.3
    
    # Predicción
    prediction = risk_score > 0.5
    
    return jsonify({
        'status': 'success',
        'prediction': {
            'prediction': prediction,
            'probability_error': min(risk_score, 0.95),
            'probability_success': max(1 - risk_score, 0.05)
        },
        'job_data': job_data
    })

@app.route('/api/data_summary')
def data_summary():
    """API para resumen de datos"""
    
    data = load_data()
    
    return jsonify({
        'total_records': len(data),
        'columns': list(data[0].keys()) if data else [],
        'sample_data': data[:5] if data else []
    })

@app.route('/api/model_status')
def model_status():
    """API para estado del modelo"""
    
    return jsonify({
        'model_exists': True,  # Simulación
        'model_loaded': True,  # Simulación
        'status': 'ready'
    })

def create_basic_visualizations(analysis_results):
    """Crea visualizaciones HTML básicas"""
    
    if not analysis_results:
        return {}
    
    figures = {}
    
    # Distribución de estados (HTML/CSS simple)
    states = analysis_results.get('states', {})
    if states:
        html = '<div class="row">'
        total = sum(states.values())
        
        for state, count in states.items():
            percentage = (count / total) * 100
            html += f'''
            <div class="col-md-6 mb-3">
                <div class="card">
                    <div class="card-body">
                        <h6>{state}</h6>
                        <div class="progress">
                            <div class="progress-bar" style="width: {percentage}%">{count:,}</div>
                        </div>
                        <small>{percentage:.1f}%</small>
                    </div>
                </div>
            </div>
            '''
        
        html += '</div>'
        figures['state_distribution'] = html
    
    # Distribución de tipos
    types = analysis_results.get('types', {})
    if types:
        html = '<div class="row">'
        total = sum(types.values())
        
        for job_type, count in list(types.items())[:6]:  # Top 6
            percentage = (count / total) * 100
            html += f'''
            <div class="col-md-4 mb-3">
                <div class="card">
                    <div class="card-body text-center">
                        <h6>{job_type}</h6>
                        <h3 class="text-primary">{count:,}</h3>
                        <small>{percentage:.1f}%</small>
                    </div>
                </div>
            </div>
            '''
        
        html += '</div>'
        figures['type_distribution'] = html
    
    # Top servidores
    servers = analysis_results.get('top_servers', {})
    if servers:
        html = '<div class="table-responsive"><table class="table table-striped"><thead><tr><th>Servidor</th><th>Jobs</th></tr></thead><tbody>'
        
        for server, count in list(servers.items())[:8]:
            html += f'<tr><td>{server}</td><td>{count:,}</td></tr>'
        
        html += '</tbody></table></div>'
        figures['server_distribution'] = html
    
    return figures

if __name__ == '__main__':
    print("🚀 Iniciando aplicación Flask de demostración...")
    print("📊 Sistema de Análisis de Jobs de Backup")
    print("🔗 Acceder en: http://localhost:5000")
    print()
    print("📝 Nota: Esta es una versión de demostración con funcionalidad básica")
    print("📝 Para funcionalidad completa de ML, instalar dependencias: pip install -r requirements.txt")
    # Registrar rutas del chatbot
    try:
        from chatbot_routes import init_chatbot_routes
        init_chatbot_routes(app)
    except Exception as e:
        print(f"⚠️  Advertencia: No se pudo cargar las rutas del chatbot: {e}")

        # Ruta de respaldo para evitar BuildError en plantillas cuando el chatbot no esta disponible.
        if 'chatbot_page' not in app.view_functions:
            @app.route('/chatbot', endpoint='chatbot_page')
            def chatbot_page_unavailable():
                return (
                    "Chatbot no disponible: faltan dependencias de analisis (por ejemplo pandas). "
                    "Instala los paquetes requeridos para habilitarlo.",
                    503,
                )
    
    
    app.run(debug=True, host='0.0.0.0', port=5000)
