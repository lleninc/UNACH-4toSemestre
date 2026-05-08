#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
APLICACIÓN FLASK DEMO PARA BACKUP1.CSV
Sistema de Análisis de Jobs de Backup con Códigos Numéricos
Universidad Nacional de Chimborazo

Esta aplicación maneja el dataset backup1.csv donde:
- Status = 0: Job satisfactorio (éxito)
- Status > 0: Diferentes códigos de error

Características:
- Análisis exploratorio de datos
- Visualizaciones interactivas
- Predicciones básicas basadas en reglas
- Interface web responsive
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.express as px
import plotly.utils
import json
import os
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# Configuración global
DATA_FILE = 'backup1.csv'
df_global = None

def load_data():
    """Carga el dataset backup1.csv"""
    global df_global
    try:
        if os.path.exists(DATA_FILE):
            print(f"🔍 Cargando {DATA_FILE}...")
            df_global = pd.read_csv(DATA_FILE, sep=';', encoding='utf-8', low_memory=False, on_bad_lines='skip')
            
            # Limpieza de columnas
            df_global.columns = df_global.columns.str.strip()
            
            # Procesamiento específico para backup1.csv
            if 'Status' in df_global.columns:
                df_global['Status_Numeric'] = pd.to_numeric(df_global['Status'], errors='coerce')
                df_global['Has_Error'] = (df_global['Status_Numeric'] > 0).astype(int)
                df_global['Success'] = (df_global['Status_Numeric'] == 0).astype(int)
            
            print(f"✅ Dataset cargado: {len(df_global)} registros")
            return True
        else:
            print(f"❌ Archivo {DATA_FILE} no encontrado")
            return False
    except Exception as e:
        print(f"❌ Error cargando datos: {e}")
        return False

def get_basic_stats():
    """Obtiene estadísticas básicas del dataset"""
    if df_global is None:
        return None
    
    stats = {
        'total_jobs': len(df_global),
        'total_columns': len(df_global.columns),
        'success_jobs': 0,
        'error_jobs': 0,
        'error_rate': 0,
        'success_rate': 0
    }
    
    if 'Status_Numeric' in df_global.columns:
        numeric_status = df_global['Status_Numeric'].dropna()
        stats['success_jobs'] = int(sum(numeric_status == 0))
        stats['error_jobs'] = int(sum(numeric_status > 0))
        stats['total_valid'] = len(numeric_status)
        
        if len(numeric_status) > 0:
            stats['error_rate'] = (stats['error_jobs'] / len(numeric_status)) * 100
            stats['success_rate'] = (stats['success_jobs'] / len(numeric_status)) * 100
    
    return stats

def create_status_distribution_chart():
    """Crea gráfico de distribución de códigos de status"""
    if df_global is None or 'Status_Numeric' not in df_global.columns:
        return None
    
    try:
        status_counts = df_global['Status_Numeric'].value_counts().sort_index()
        
        # Separar éxitos de errores
        success_count = status_counts.get(0, 0)
        error_codes = status_counts[status_counts.index > 0]
        
        # Crear gráfico de barras
        fig = go.Figure()
        
        # Barra de éxito
        fig.add_trace(go.Bar(
            x=['Status 0 (Éxito)'],
            y=[success_count],
            name='Jobs Exitosos',
            marker_color='green',
            text=[f'{success_count:,}'],
            textposition='auto'
        ))
        
        # Barras de errores
        if len(error_codes) > 0:
            error_labels = [f'Status {int(code)}' for code in error_codes.index]
            fig.add_trace(go.Bar(
                x=error_labels,
                y=error_codes.values,
                name='Jobs con Error',
                marker_color='red',
                text=[f'{count:,}' for count in error_codes.values],
                textposition='auto'
            ))
        
        fig.update_layout(
            title='Distribución de Códigos de Status',
            xaxis_title='Código de Status',
            yaxis_title='Cantidad de Jobs',
            showlegend=True,
            height=500
        )
        
        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    except Exception as e:
        print(f"Error creando gráfico de status: {e}")
        return None

def create_job_type_chart():
    """Crea gráfico de distribución por tipo de job"""
    if df_global is None:
        return None
    
    try:
        # Buscar columna de tipo
        type_col = None
        for col in df_global.columns:
            if 'type' in col.lower() or 'tipo' in col.lower():
                type_col = col
                break
        
        if type_col is None:
            return None
        
        type_counts = df_global[type_col].value_counts().head(10)
        
        fig = px.pie(
            values=type_counts.values,
            names=type_counts.index,
            title='Distribución por Tipo de Job'
        )
        
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(height=500)
        
        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    except Exception as e:
        print(f"Error creando gráfico de tipos: {e}")
        return None

def create_error_analysis_chart():
    """Crea gráfico de análisis de errores por código"""
    if df_global is None or 'Status_Numeric' not in df_global.columns:
        return None
    
    try:
        # Obtener solo jobs con error
        error_jobs = df_global[df_global['Status_Numeric'] > 0]
        
        if len(error_jobs) == 0:
            return None
        
        error_codes = error_jobs['Status_Numeric'].value_counts().head(10)
        
        fig = go.Figure(data=[
            go.Bar(
                x=[f'Error {int(code)}' for code in error_codes.index],
                y=error_codes.values,
                marker_color='red',
                text=[f'{count} jobs' for count in error_codes.values],
                textposition='auto'
            )
        ])
        
        fig.update_layout(
            title='Top 10 Códigos de Error más Frecuentes',
            xaxis_title='Código de Error',
            yaxis_title='Cantidad de Jobs',
            height=500
        )
        
        return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    except Exception as e:
        print(f"Error creando gráfico de errores: {e}")
        return None

def predict_job_outcome(job_type, media_server, job_schedule):
    """
    Predicción simple basada en reglas para demostración
    """
    try:
        stats = get_basic_stats()
        if stats is None:
            return {'prediction': 'Error', 'confidence': 50, 'reason': 'No hay datos disponibles'}
        
        # Reglas básicas de predicción basadas en análisis
        confidence = 50
        prediction = 'Error'
        reason = 'Predicción base'
        
        # Ajustar según tasa de éxito general
        if stats['success_rate'] > 90:
            prediction = 'Éxito'
            confidence = stats['success_rate']
            reason = f'Alta tasa de éxito general ({stats["success_rate"]:.1f}%)'
        
        # Ajustar según tipo de job (si está disponible)
        if job_type and job_type.lower() == 'backup':
            confidence += 10
            reason += ' + Tipo backup (más confiable)'
        
        # Ajustar según servidor
        if media_server and any(server in media_server.lower() for server in ['ecbplx', 'precan']):
            confidence += 5
            reason += ' + Servidor conocido'
        
        # Limitar confianza
        confidence = min(confidence, 95)
        
        return {
            'prediction': prediction,
            'confidence': round(confidence, 1),
            'reason': reason,
            'stats': stats
        }
    except Exception as e:
        return {
            'prediction': 'Error',
            'confidence': 50,
            'reason': f'Error en predicción: {str(e)}'
        }

@app.route('/')
def index():
    """Página principal"""
    stats = get_basic_stats()
    return render_template('index.html', stats=stats, dataset_type='backup1')

@app.route('/analysis')
def analysis():
    """Página de análisis exploratorio"""
    stats = get_basic_stats()
    
    # Crear gráficos
    status_chart = create_status_distribution_chart()
    type_chart = create_job_type_chart()
    error_chart = create_error_analysis_chart()
    
    return render_template('analysis.html', 
                         stats=stats,
                         status_chart=status_chart,
                         type_chart=type_chart,
                         error_chart=error_chart,
                         dataset_type='backup1')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Sistema de predicciones"""
    if request.method == 'POST':
        job_type = request.form.get('job_type', '')
        media_server = request.form.get('media_server', '')
        job_schedule = request.form.get('job_schedule', '')
        
        result = predict_job_outcome(job_type, media_server, job_schedule)
        return render_template('predict.html', prediction=result, show_result=True)
    
    return render_template('predict.html', show_result=False)

@app.route('/api/stats')
def api_stats():
    """API para obtener estadísticas"""
    stats = get_basic_stats()
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
    """Página de documentación"""
    return render_template('documentation.html', dataset_type='backup1')

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html', error='Página no encontrada'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error='Error interno del servidor'), 500

if __name__ == '__main__':
    print("🚀 Iniciando aplicación Flask para BACKUP1.CSV...")
    print("📊 Sistema de Análisis de Jobs de Backup con Códigos Numéricos")
    print("🔗 Acceder en: http://localhost:5000")
    print("📝 Dataset: backup1.csv (Status numéricos: 0=éxito, >0=error)")
    
    # Cargar datos al inicio
    if load_data():
        stats = get_basic_stats()
        if stats:
            print(f"📈 Jobs analizados: {stats['total_jobs']:,}")
            print(f"✅ Jobs exitosos: {stats['success_jobs']:,} ({stats['success_rate']:.1f}%)")
            print(f"❌ Jobs con error: {stats['error_jobs']:,} ({stats['error_rate']:.1f}%)")
        
        app.run(host='0.0.0.0', port=5000, debug=True)
    else:
        print("❌ No se pudo cargar el dataset. Verifique que existe backup1.csv")
        print("💡 Para crear el dataset, copie backup1.csv al directorio actual")
