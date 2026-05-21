"""
Análisis básico de datos de backup jobs
Este script funciona con librerías básicas de Python para demostración inicial
"""

import csv
import json
from collections import Counter, defaultdict
from datetime import datetime
import os

def load_backup_data(file_path='e:\\Unach\\Semestre4\\EstudioGITClaude\\UNACH-4toSemestre\\Examen\\backup_ml_app\\data\\backup.csv'):
    """Carga los datos del archivo CSV"""
    jobs = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                jobs.append(row)
        
        print(f"✅ Datos cargados: {len(jobs)} registros")
        return jobs
        
    except FileNotFoundError:
        print(f"❌ Archivo no encontrado: {file_path}")
        return []
    except Exception as e:
        print(f"❌ Error cargando datos: {e}")
        return []

def analyze_job_states(jobs):
    """Analiza la distribución de estados de jobs"""
    print("\\n📊 ANÁLISIS DE ESTADOS DE JOBS")
    print("-" * 40)
    
    states = Counter(job['State'] for job in jobs)
    total = len(jobs)
    
    for state, count in states.most_common():
        percentage = (count / total) * 100
        print(f"{state:15} | {count:6,} | {percentage:5.1f}%")
    
    # Identificar jobs con problemas
    problem_states = [job for job in jobs if job['State'] not in ['Active', 'Queued']]
    problem_rate = (len(problem_states) / total) * 100
    
    print(f"\\n⚠️  Jobs con problemas: {len(problem_states):,} ({problem_rate:.1f}%)")
    
    return states

def analyze_job_types(jobs):
    """Analiza la distribución de tipos de jobs"""
    print("\\n📋 ANÁLISIS DE TIPOS DE JOBS")
    print("-" * 40)
    
    types = Counter(job['Type'] for job in jobs)
    total = len(jobs)
    
    for job_type, count in types.most_common():
        percentage = (count / total) * 100
        print(f"{job_type:20} | {count:6,} | {percentage:5.1f}%")
    
    return types

def analyze_temporal_patterns(jobs):
    """Analiza patrones temporales"""
    print("\\n⏰ ANÁLISIS TEMPORAL")
    print("-" * 40)
    
    hourly_distribution = defaultdict(int)
    
    for job in jobs:
        start_time = job.get('Start Time', '')
        if start_time:
            try:
                # Extraer hora (formato esperado: DD/MM/YYYY HH:MM)
                if ' ' in start_time:
                    time_part = start_time.split(' ')[1]
                    hour = int(time_part.split(':')[0])
                    hourly_distribution[hour] += 1
            except:
                continue
    
    print("Distribución por hora:")
    for hour in sorted(hourly_distribution.keys()):
        count = hourly_distribution[hour]
        bar = "█" * min(50, count // 100)  # Barra visual
        print(f"{hour:2d}:00 | {count:4,} | {bar}")
    
    return hourly_distribution

def analyze_media_servers(jobs):
    """Analiza la distribución por Media Server"""
    print("\\n🖥️  ANÁLISIS DE MEDIA SERVERS")
    print("-" * 40)
    
    servers = Counter(job['Media Server'] for job in jobs if job['Media Server'])
    
    print("Top 10 servidores más utilizados:")
    for server, count in servers.most_common(10):
        print(f"{server:25} | {count:6,}")
    
    return servers

def analyze_performance_metrics(jobs):
    """Analiza métricas de rendimiento"""
    print("\\n⚡ ANÁLISIS DE RENDIMIENTO")
    print("-" * 40)
    
    # Analizar velocidades (KB/Sec)
    speeds = []
    sizes = []
    
    for job in jobs:
        try:
            kb_sec = job.get('KB/Sec', '').replace(',', '')
            if kb_sec and kb_sec.replace('.', '').isdigit():
                speeds.append(float(kb_sec))
            
            kilobytes = job.get('Kilobytes', '').replace(',', '')
            if kilobytes and kilobytes.replace('.', '').isdigit():
                sizes.append(float(kilobytes))
        except:
            continue
    
    if speeds:
        speeds.sort()
        n = len(speeds)
        print(f"Velocidades (KB/Sec) - {n:,} muestras:")
        print(f"  Mínima:    {speeds[0]:8.1f}")
        print(f"  Máxima:    {speeds[-1]:8.1f}")
        print(f"  Mediana:   {speeds[n//2]:8.1f}")
        print(f"  Promedio:  {sum(speeds)/n:8.1f}")
    
    if sizes:
        sizes.sort()
        n = len(sizes)
        print(f"\\nTamaños (KB) - {n:,} muestras:")
        print(f"  Mínimo:    {sizes[0]:12,.0f}")
        print(f"  Máximo:    {sizes[-1]:12,.0f}")
        print(f"  Mediana:   {sizes[n//2]:12,.0f}")
        print(f"  Promedio:  {sum(sizes)/n:12,.0f}")

def generate_insights(jobs):
    """Genera insights y recomendaciones"""
    print("\\n💡 INSIGHTS Y RECOMENDACIONES")
    print("-" * 40)
    
    total_jobs = len(jobs)
    problem_jobs = [job for job in jobs if job['State'] not in ['Active', 'Queued']]
    problem_rate = (len(problem_jobs) / total_jobs) * 100
    
    print("📈 Insights principales:")
    print(f"1. Tasa de problemas actual: {problem_rate:.1f}%")
    
    # Analizar patrones en jobs problemáticos
    if problem_jobs:
        problem_types = Counter(job['Type'] for job in problem_jobs)
        print(f"2. Tipos más problemáticos: {problem_types.most_common(3)}")
        
        problem_servers = Counter(job['Media Server'] for job in problem_jobs if job['Media Server'])
        if problem_servers:
            print(f"3. Servidores con más problemas: {problem_servers.most_common(3)}")
    
    print("\\n🎯 Recomendaciones:")
    if problem_rate > 10:
        print("• Alta tasa de problemas - Revisar configuraciones del sistema")
    elif problem_rate > 5:
        print("• Tasa moderada de problemas - Optimizar programación de jobs")
    else:
        print("• Tasa baja de problemas - Mantener configuración actual")
    
    print("• Implementar monitoreo predictivo con Machine Learning")
    print("• Balancear carga entre servidores disponibles")
    print("• Optimizar ventanas de backup en horarios de menor uso")

def generate_summary_report(jobs):
    """Genera un reporte resumen"""
    
    report = {
        'total_jobs': len(jobs),
        'analysis_date': datetime.now().isoformat(),
        'job_states': dict(Counter(job['State'] for job in jobs)),
        'job_types': dict(Counter(job['Type'] for job in jobs)),
        'problem_rate': len([job for job in jobs if job['State'] not in ['Active', 'Queued']]) / len(jobs) * 100,
        'top_servers': dict(Counter(job['Media Server'] for job in jobs if job['Media Server']).most_common(5))
    }
    
    # Guardar reporte en JSON
    with open('backup_analysis_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"\\n💾 Reporte guardado en 'backup_analysis_report.json'")
    return report

def main():
    """Función principal de análisis"""
    print("🔍 ANÁLISIS DE DATOS DE BACKUP JOBS")
    print("=" * 50)
    
    # Cargar datos
    jobs = load_backup_data()
    
    if not jobs:
        print("❌ No se pudieron cargar los datos")
        return
    
    # Realizar análisis
    analyze_job_states(jobs)
    analyze_job_types(jobs)
    analyze_temporal_patterns(jobs)
    analyze_media_servers(jobs)
    analyze_performance_metrics(jobs)
    generate_insights(jobs)
    
    # Generar reporte
    report = generate_summary_report(jobs)
    
    print("\\n" + "=" * 50)
    print("✅ ANÁLISIS COMPLETADO")
    print(f"📊 Total de jobs analizados: {len(jobs):,}")
    print(f"📈 Tasa de problemas: {report['problem_rate']:.1f}%")
    print("\\n🚀 Para análisis más avanzado, ejecute la aplicación Flask completa")

if __name__ == "__main__":
    main()
