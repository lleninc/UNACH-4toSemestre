#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DEMOSTRACIÓN COMPLETA BACKUP1.CSV
Sistema de Análisis de Jobs de Backup con Códigos Numéricos
Universidad Nacional de Chimborazo

Este script demuestra el análisis completo del dataset backup1.csv donde:
- Status = 0: Job satisfactorio (éxito)
- Status > 0: Diferentes códigos de error

Solo usa bibliotecas estándar de Python para máxima compatibilidad.
"""

import csv
import json
from collections import Counter, defaultdict
from datetime import datetime
import os

def load_backup1_data():
    """Carga y procesa el dataset backup1.csv"""
    print("🔍 ANÁLISIS COMPLETO BACKUP1.CSV")
    print("=" * 50)
    
    if not os.path.exists('backup1.csv'):
        print("❌ Error: Archivo backup1.csv no encontrado")
        return None
    
    print("📂 Cargando dataset backup1.csv...")
    
    data = []
    headers = []
    
    try:
        with open('backup1.csv', 'r', encoding='utf-8', errors='ignore') as file:
            # Detectar delimitador
            first_line = file.readline()
            if ';' in first_line:
                delimiter = ';'
            elif ',' in first_line:
                delimiter = ','
            else:
                delimiter = '\t'
            
            file.seek(0)  # Volver al inicio
            
            reader = csv.reader(file, delimiter=delimiter)
            headers = next(reader)
            
            # Limpiar headers
            headers = [h.strip() for h in headers]
            
            # Leer datos
            for row_num, row in enumerate(reader):
                if row_num > 100000:  # Limitar para demo
                    break
                data.append(row)
        
        print(f"✅ Dataset cargado: {len(data)} registros")
        print(f"📊 Columnas: {len(headers)}")
        
        return data, headers
        
    except Exception as e:
        print(f"❌ Error cargando datos: {e}")
        return None, None

def analyze_status_codes(data, headers):
    """Analiza los códigos de status numéricos"""
    print(f"\n🔢 ANÁLISIS DE CÓDIGOS DE STATUS")
    print("-" * 40)
    
    # Encontrar columna Status
    status_col_idx = None
    for i, header in enumerate(headers):
        if 'status' in header.lower():
            status_col_idx = i
            break
    
    if status_col_idx is None:
        print("❌ Columna Status no encontrada")
        return None
    
    print(f"📍 Columna Status encontrada: {headers[status_col_idx]} (posición {status_col_idx})")
    
    # Procesar códigos de status
    status_codes = []
    for row in data:
        if len(row) > status_col_idx:
            try:
                status = row[status_col_idx].strip()
                if status and status != '':
                    status_num = int(float(status))
                    status_codes.append(status_num)
            except (ValueError, IndexError):
                continue
    
    if not status_codes:
        print("❌ No se encontraron códigos de status válidos")
        return None
    
    # Contar códigos
    status_counter = Counter(status_codes)
    
    # Estadísticas
    total_jobs = len(status_codes)
    success_jobs = status_counter.get(0, 0)
    error_jobs = total_jobs - success_jobs
    error_rate = (error_jobs / total_jobs) * 100 if total_jobs > 0 else 0
    
    print(f"\n📊 RESULTADOS DEL ANÁLISIS:")
    print(f"✅ Jobs exitosos (Status=0): {success_jobs:,} ({((success_jobs/total_jobs)*100):.1f}%)")
    print(f"❌ Jobs con error (Status>0): {error_jobs:,} ({error_rate:.1f}%)")
    print(f"📈 Total analizado: {total_jobs:,} jobs")
    
    # Top códigos de error
    error_codes = {k: v for k, v in status_counter.items() if k > 0}
    if error_codes:
        print(f"\n🚨 TOP 10 CÓDIGOS DE ERROR:")
        sorted_errors = sorted(error_codes.items(), key=lambda x: x[1], reverse=True)[:10]
        for code, count in sorted_errors:
            percentage = (count / total_jobs) * 100
            print(f"  Error {code}: {count:,} jobs ({percentage:.2f}%)")
    
    # Distribución completa
    print(f"\n📋 DISTRIBUCIÓN COMPLETA DE STATUS:")
    sorted_status = sorted(status_counter.items())
    for code, count in sorted_status[:20]:  # Mostrar primeros 20
        percentage = (count / total_jobs) * 100
        status_type = "✅ ÉXITO" if code == 0 else "❌ ERROR"
        print(f"  Status {code:2d}: {count:6,} jobs ({percentage:5.1f}%) {status_type}")
    
    if len(sorted_status) > 20:
        print(f"  ... y {len(sorted_status)-20} códigos más")
    
    return {
        'total_jobs': total_jobs,
        'success_jobs': success_jobs,
        'error_jobs': error_jobs,
        'error_rate': error_rate,
        'status_distribution': dict(status_counter),
        'top_error_codes': sorted_errors
    }

def analyze_job_types(data, headers):
    """Analiza tipos de jobs"""
    print(f"\n📋 ANÁLISIS DE TIPOS DE JOBS")
    print("-" * 35)
    
    # Encontrar columna Type
    type_col_idx = None
    for i, header in enumerate(headers):
        if 'type' in header.lower():
            type_col_idx = i
            break
    
    if type_col_idx is None:
        print("❌ Columna Type no encontrada")
        return None
    
    # Procesar tipos
    job_types = []
    for row in data:
        if len(row) > type_col_idx:
            job_type = row[type_col_idx].strip()
            if job_type:
                job_types.append(job_type)
    
    type_counter = Counter(job_types)
    total = len(job_types)
    
    print(f"📊 Distribución por tipo de job:")
    for job_type, count in type_counter.most_common(10):
        percentage = (count / total) * 100
        print(f"  {job_type}: {count:,} ({percentage:.1f}%)")
    
    return dict(type_counter)

def analyze_servers(data, headers):
    """Analiza servidores más utilizados"""
    print(f"\n🖥️ ANÁLISIS DE SERVIDORES")
    print("-" * 30)
    
    # Buscar columnas de servidor
    server_cols = []
    for i, header in enumerate(headers):
        if any(keyword in header.lower() for keyword in ['server', 'media', 'client']):
            server_cols.append((i, header))
    
    if not server_cols:
        print("❌ Columnas de servidor no encontradas")
        return None
    
    all_servers = []
    for col_idx, col_name in server_cols:
        print(f"\n📍 Analizando columna: {col_name}")
        servers = []
        for row in data:
            if len(row) > col_idx:
                server = row[col_idx].strip()
                if server and server not in ['', 'nan', 'NaN']:
                    servers.append(server)
        
        if servers:
            server_counter = Counter(servers)
            print(f"  Top 5 servidores en {col_name}:")
            for server, count in server_counter.most_common(5):
                print(f"    {server}: {count:,}")
            all_servers.extend(servers)
    
    return Counter(all_servers)

def generate_insights(status_analysis, job_types, servers):
    """Genera insights y recomendaciones"""
    print(f"\n💡 INSIGHTS Y RECOMENDACIONES")
    print("-" * 40)
    
    if status_analysis:
        error_rate = status_analysis['error_rate']
        
        print(f"📈 ESTADO ACTUAL DEL SISTEMA:")
        print(f"  Tasa de error: {error_rate:.2f}%")
        
        if error_rate < 1:
            print("  ✅ EXCELENTE - Muy baja tasa de errores")
            print("  🎯 Objetivo: Mantener configuración actual")
        elif error_rate < 5:
            print("  ⚠️ ACEPTABLE - Tasa de errores moderada")
            print("  🎯 Objetivo: Reducir errores específicos")
        else:
            print("  🚨 CRÍTICO - Alta tasa de errores")
            print("  🎯 Objetivo: Revisión urgente del sistema")
        
        print(f"\n🔧 RECOMENDACIONES ESPECÍFICAS:")
        
        # Basado en tasa de error
        if error_rate < 1:
            print("  • Implementar monitoreo preventivo")
            print("  • Documentar configuraciones exitosas")
            print("  • Establecer alertas tempranas")
        else:
            print("  • Analizar códigos de error más frecuentes")
            print("  • Revisar jobs fallidos por patrón temporal")
            print("  • Optimizar configuración de servidores problemáticos")
        
        # Recomendaciones por códigos de error
        if 'top_error_codes' in status_analysis and status_analysis['top_error_codes']:
            top_error = status_analysis['top_error_codes'][0]
            print(f"  • Priorizar solución del Error {top_error[0]} ({top_error[1]:,} ocurrencias)")
        
        # Potencial de ML
        total_jobs = status_analysis['total_jobs']
        if total_jobs > 10000:
            print(f"\n🤖 POTENCIAL DE MACHINE LEARNING:")
            print(f"  Dataset tamaño: {total_jobs:,} registros ✅")
            print(f"  Distribución balanceada: {'✅' if 1 <= error_rate <= 10 else '⚠️'}")
            print(f"  Recomendación: {'Implementar ML' if error_rate > 0.5 else 'ML opcional'}")
    
    print(f"\n🎯 PRÓXIMOS PASOS:")
    print("  1. Ejecutar aplicación web para análisis interactivo")
    print("  2. Implementar sistema de alertas automáticas")
    print("  3. Configurar dashboard de monitoreo en tiempo real")
    print("  4. Entrenar modelo ML para predicción proactiva")

def save_report(status_analysis, job_types, servers):
    """Guarda reporte completo en JSON"""
    report = {
        'timestamp': datetime.now().isoformat(),
        'dataset': 'backup1.csv',
        'analysis_type': 'Códigos numéricos de status',
        'status_analysis': status_analysis,
        'job_types': dict(job_types) if job_types else {},
        'servers': dict(servers.most_common(20)) if servers else {},
        'summary': {
            'error_rate': status_analysis['error_rate'] if status_analysis else 0,
            'recommendation': 'Implementar monitoreo ML' if status_analysis and status_analysis['error_rate'] > 0.5 else 'Mantener monitoreo básico'
        }
    }
    
    with open('backup1_complete_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Reporte completo guardado en 'backup1_complete_report.json'")

def main():
    """Función principal de demostración"""
    print("🚀 INICIANDO DEMOSTRACIÓN COMPLETA BACKUP1.CSV")
    print("📊 Universidad Nacional de Chimborazo")
    print("🎓 Ingeniería en Sistemas y Computación")
    print()
    
    # Cargar datos
    data, headers = load_backup1_data()
    if not data:
        return
    
    # Análisis principal
    status_analysis = analyze_status_codes(data, headers)
    job_types = analyze_job_types(data, headers)
    servers = analyze_servers(data, headers)
    
    # Insights y recomendaciones
    generate_insights(status_analysis, job_types, servers)
    
    # Guardar reporte
    save_report(status_analysis, job_types, servers)
    
    print(f"\n🎉 DEMOSTRACIÓN COMPLETADA")
    print("=" * 50)
    print("✅ Dataset backup1.csv analizado exitosamente")
    print("📊 Códigos de status interpretados correctamente")
    print("💡 Insights y recomendaciones generados")
    print("💾 Reporte JSON guardado")
    print("\n🚀 Para análisis interactivo, ejecute:")
    print("   python app_backup1.py")

if __name__ == "__main__":
    main()
