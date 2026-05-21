#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
APLICACIÓN FLASK SIMPLE PARA BACKUP1.CSV
Sistema de Análisis de Jobs de Backup con Códigos Numéricos
Universidad Nacional de Chimborazo

Esta versión usa solo bibliotecas estándar de Python para máxima compatibilidad.
"""

from flask import Flask, render_template, request, jsonify
import csv
import json
import os
from collections import Counter
from datetime import datetime

app = Flask(__name__)

# Configuración global
DATA_FILE = 'backup1.csv'
data_cache = None

def load_backup1_data():
    """Carga y procesa el dataset backup1.csv usando solo bibliotecas estándar"""
    global data_cache
    
    if data_cache is not None:
        return data_cache
    
    try:
        if not os.path.exists(DATA_FILE):
            print(f"❌ Archivo {DATA_FILE} no encontrado")
            return None
        
        print(f"🔍 Cargando {DATA_FILE}...")
        
        data = []
        headers = []
        
        with open(DATA_FILE, 'r', encoding='utf-8', errors='ignore') as file:
            # Detectar delimitador
            first_line = file.readline()
            delimiter = ';' if ';' in first_line else ','
            
            file.seek(0)  # Volver al inicio
            reader = csv.reader(file, delimiter=delimiter)
            headers = [h.strip() for h in next(reader)]
            
            # Leer datos (limitar para demo)
            for row_num, row in enumerate(reader):
                if row_num > 50000:  # Limitar para mejor rendimiento
                    break
                data.append(row)
        
        data_cache = {
            'data': data,
            'headers': headers,
            'total_rows': len(data)
        }
        
        print(f"✅ Dataset cargado: {len(data)} registros")
        return data_cache
        
    except Exception as e:
        print(f"❌ Error cargando datos: {e}")
        return None

def analyze_status_codes():
    """Analiza los códigos de status del dataset"""
    dataset = load_backup1_data()
    if not dataset:
        return None
    
    # Encontrar columna Status
    status_col_idx = None
    for i, header in enumerate(dataset['headers']):
        if 'status' in header.lower():
            status_col_idx = i
            break
    
    if status_col_idx is None:
        return None
    
    # Procesar códigos de status
    status_codes = []
    for row in dataset['data']:
        if len(row) > status_col_idx:
            try:
                status = row[status_col_idx].strip()
                if status and status != '':
                    status_num = int(float(status))
                    status_codes.append(status_num)
            except (ValueError, IndexError):
                continue
    
    if not status_codes:
        return None
    
    # Contar códigos
    status_counter = Counter(status_codes)
    total_jobs = len(status_codes)
    success_jobs = status_counter.get(0, 0)
    error_jobs = total_jobs - success_jobs
    
    return {
        'total_jobs': total_jobs,
        'success_jobs': success_jobs,
        'error_jobs': error_jobs,
        'success_rate': (success_jobs / total_jobs) * 100 if total_jobs > 0 else 0,
        'error_rate': (error_jobs / total_jobs) * 100 if total_jobs > 0 else 0,
        'status_distribution': dict(status_counter),
        'top_error_codes': [(k, v) for k, v in sorted(status_counter.items(), key=lambda x: x[1], reverse=True) if k > 0][:10]
    }

def analyze_job_types():
    """Analiza tipos de jobs"""
    dataset = load_backup1_data()
    if not dataset:
        return None
    
    # Encontrar columna Type
    type_col_idx = None
    for i, header in enumerate(dataset['headers']):
        if 'type' in header.lower():
            type_col_idx = i
            break
    
    if type_col_idx is None:
        return None
    
    job_types = []
    for row in dataset['data']:
        if len(row) > type_col_idx:
            job_type = row[type_col_idx].strip()
            if job_type:
                job_types.append(job_type)
    
    type_counter = Counter(job_types)
    total = len(job_types)
    
    return {
        'distribution': [(job_type, count, (count/total)*100) for job_type, count in type_counter.most_common(10)],
        'total': total
    }

def create_simple_charts():
    """Crea datos para gráficos simples"""
    status_analysis = analyze_status_codes()
    if not status_analysis:
        return None
    
    # Datos para gráfico de status
    status_chart_data = {
        'labels': ['Jobs Exitosos (Status 0)', 'Jobs con Error (Status > 0)'],
        'values': [status_analysis['success_jobs'], status_analysis['error_jobs']],
        'colors': ['#28a745', '#dc3545']
    }
    
    # Datos para gráfico de códigos de error
    error_chart_data = {
        'labels': [f'Error {code}' for code, count in status_analysis['top_error_codes']],
        'values': [count for code, count in status_analysis['top_error_codes']],
        'colors': ['#dc3545'] * len(status_analysis['top_error_codes'])
    }
    
    return {
        'status_chart': status_chart_data,
        'error_chart': error_chart_data
    }

def predict_job_outcome(job_type, media_server, job_schedule):
    """Predicción simple basada en reglas"""
    status_analysis = analyze_status_codes()
    if not status_analysis:
        return {
            'prediction': 'Error',
            'confidence': 50,
            'reason': 'No hay datos disponibles'
        }
    
    # Predicción basada en tasa de éxito general
    base_confidence = status_analysis['success_rate']
    prediction = 'Éxito' if base_confidence > 50 else 'Error'
    
    # Ajustes según parámetros
    confidence = base_confidence
    reason = f'Tasa de éxito general: {base_confidence:.1f}%'
    
    if job_type and job_type.lower() == 'backup':
        confidence += 2
        reason += ' + Tipo backup (confiable)'
    
    if media_server and any(server in media_server.lower() for server in ['ecbplx', 'precan']):
        confidence += 1
        reason += ' + Servidor conocido'
    
    confidence = min(confidence, 99.9)
    
    return {
        'prediction': prediction,
        'confidence': round(confidence, 1),
        'reason': reason,
        'stats': status_analysis
    }

@app.route('/')
def index():
    """Página principal"""
    status_analysis = analyze_status_codes()
    return render_template('index_simple.html', stats=status_analysis)

@app.route('/analysis')
def analysis():
    """Página de análisis"""
    status_analysis = analyze_status_codes()
    job_types = analyze_job_types()
    charts = create_simple_charts()
    
    return render_template('analysis_simple.html', 
                         stats=status_analysis,
                         job_types=job_types,
                         charts=charts)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Sistema de predicciones"""
    if request.method == 'POST':
        job_type = request.form.get('job_type', '')
        media_server = request.form.get('media_server', '')
        job_schedule = request.form.get('job_schedule', '')
        
        result = predict_job_outcome(job_type, media_server, job_schedule)
        return render_template('predict_simple.html', prediction=result, show_result=True)
    
    return render_template('predict_simple.html', show_result=False)

@app.route('/api/stats')
def api_stats():
    """API para estadísticas"""
    stats = analyze_status_codes()
    return jsonify(stats)

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API para predicciones"""
    data = request.json
    result = predict_job_outcome(
        data.get('job_type', ''),
        data.get('media_server', ''),
        data.get('job_schedule', '')
    )
    return jsonify(result)

@app.route('/documentation')
def documentation():
    """Documentación del sistema"""
    return render_template('documentation_simple.html')

@app.errorhandler(404)
def not_found(error):
    return f"""
    <h1>Página no encontrada</h1>
    <p>La página que buscas no existe.</p>
    <a href="/">Volver al inicio</a>
    """, 404

@app.errorhandler(500)
def internal_error(error):
    return f"""
    <h1>Error interno</h1>
    <p>Ha ocurrido un error interno del servidor.</p>
    <p>Error: {str(error)}</p>
    <a href="/">Volver al inicio</a>
    """, 500

if __name__ == '__main__':
    print("🚀 Iniciando aplicación Flask SIMPLE para BACKUP1.CSV...")
    print("📊 Sistema de Análisis de Jobs de Backup (Versión Compatible)")
    print("🔗 Acceder en: http://localhost:5001")
    print("📝 Dataset: backup1.csv (Status numéricos: 0=éxito, >0=error)")
    print("⚡ Usando solo bibliotecas estándar de Python")
    
    # Intentar cargar datos
    if load_backup1_data():
        stats = analyze_status_codes()
        if stats:
            print(f"📈 Jobs analizados: {stats['total_jobs']:,}")
            print(f"✅ Jobs exitosos: {stats['success_jobs']:,} ({stats['success_rate']:.1f}%)")
            print(f"❌ Jobs con error: {stats['error_jobs']:,} ({stats['error_rate']:.1f}%)")
        
        app.run(host='0.0.0.0', port=5001, debug=True)
    else:
        print("❌ No se pudo cargar el dataset.")
        print("💡 Verifique que backup1.csv existe en el directorio actual")
