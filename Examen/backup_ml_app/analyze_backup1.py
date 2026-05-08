#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ANÁLISIS DE DATOS BACKUP1.CSV - CÓDIGOS DE STATUS NUMÉRICOS
Sistema de Análisis de Jobs de Backup con Códigos de Error
Universidad Nacional de Chimborazo

Este módulo analiza el dataset backup1.csv donde:
- Status = 0: Job satisfactorio (éxito)
- Status > 0: Diferentes códigos de error
"""

import pandas as pd
import os
import json
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

def analyze_backup1_dataset():
    """
    Analiza el dataset backup1.csv con códigos de status numéricos
    """
    print("🔍 ANÁLISIS DE BACKUP1.CSV - CÓDIGOS DE STATUS NUMÉRICOS")
    print("=" * 60)
    
    # Ruta del archivo
    file_path = "backup1.csv"
    
    if not os.path.exists(file_path):
        print(f"❌ Error: No se encontró el archivo {file_path}")
        return None
    
    try:
        # Intentar diferentes delimitadores y encodings
        print("📂 Cargando datos...")
        
        # Primero verificar la estructura del archivo
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            first_lines = [f.readline().strip() for _ in range(5)]
        
        print("📋 Primeras líneas del archivo:")
        for i, line in enumerate(first_lines):
            print(f"  Línea {i+1}: {line[:100]}{'...' if len(line) > 100 else ''}")
        
        # Detectar delimitador
        if ';' in first_lines[0]:
            delimiter = ';'
            print("✅ Delimitador detectado: punto y coma (;)")
        elif ',' in first_lines[0]:
            delimiter = ','
            print("✅ Delimitador detectado: coma (,)")
        else:
            delimiter = '\t'
            print("✅ Delimitador detectado: tabulación")
        
        # Cargar datos con manejo de errores
        try:
            df = pd.read_csv(file_path, delimiter=delimiter, encoding='utf-8', low_memory=False, on_bad_lines='skip')
        except Exception as e:
            print(f"⚠️ Error con UTF-8, intentando con ISO-8859-1: {e}")
            df = pd.read_csv(file_path, delimiter=delimiter, encoding='iso-8859-1', low_memory=False, on_bad_lines='skip')
        
        print(f"✅ Datos cargados: {len(df)} registros")
        print(f"📊 Columnas encontradas: {len(df.columns)}")
        
        # Mostrar nombres de columnas
        print("\n📋 ESTRUCTURA DE COLUMNAS:")
        print("-" * 40)
        for i, col in enumerate(df.columns):
            print(f"  {i+1:2d}. {col}")
        
        # Buscar la columna Status
        status_col = None
        for col in df.columns:
            if 'status' in col.lower() or 'estado' in col.lower():
                status_col = col
                break
        
        if status_col is None:
            print("❌ No se encontró columna de Status")
            # Verificar si la columna está en posición específica
            if len(df.columns) >= 3:
                status_col = df.columns[2]  # Tercera columna (index 2)
                print(f"📍 Usando columna en posición 3: '{status_col}'")
        
        print(f"\n🎯 ANÁLISIS DE COLUMNA DE STATUS: '{status_col}'")
        print("-" * 50)
        
        # Analizar valores únicos en la columna de status
        if status_col in df.columns:
            status_values = df[status_col].value_counts().sort_index()
            print("📊 Distribución de valores de Status:")
            
            # Verificar si hay valores numéricos
            numeric_status = df[status_col].apply(pd.to_numeric, errors='coerce')
            non_null_numeric = numeric_status.dropna()
            
            if len(non_null_numeric) > 0:
                print(f"✅ Encontrados {len(non_null_numeric)} valores numéricos de status")
                
                # Analizar códigos de status numéricos
                numeric_counts = non_null_numeric.value_counts().sort_index()
                print("\n🔢 CÓDIGOS DE STATUS NUMÉRICOS:")
                print("-" * 30)
                
                total_numeric = len(non_null_numeric)
                success_count = 0
                error_count = 0
                
                for status_code, count in numeric_counts.items():
                    percentage = (count / total_numeric) * 100
                    if status_code == 0:
                        print(f"  ✅ Código {int(status_code)} (ÉXITO): {count:,} jobs ({percentage:.1f}%)")
                        success_count = count
                    else:
                        print(f"  ❌ Código {int(status_code)} (ERROR): {count:,} jobs ({percentage:.1f}%)")
                        error_count += count
                
                # Resumen de éxito vs errores
                print(f"\n📈 RESUMEN DE RESULTADOS:")
                print("-" * 30)
                print(f"✅ Jobs exitosos (Status = 0): {success_count:,} ({(success_count/total_numeric)*100:.1f}%)")
                print(f"❌ Jobs con error (Status > 0): {error_count:,} ({(error_count/total_numeric)*100:.1f}%)")
                print(f"📊 Total de jobs analizados: {total_numeric:,}")
                
                # Tasa de error
                error_rate = (error_count / total_numeric) * 100
                print(f"⚠️ Tasa de error actual: {error_rate:.1f}%")
                
            else:
                print("❌ No se encontraron valores numéricos válidos en la columna Status")
                print("📋 Valores únicos encontrados:")
                for value, count in status_values.head(10).items():
                    print(f"  '{value}': {count}")
        
        # Análisis adicional de otras columnas importantes
        print(f"\n🔍 ANÁLISIS ADICIONAL DEL DATASET")
        print("-" * 40)
        
        # Buscar columnas de interés
        important_cols = {}
        for col in df.columns:
            col_lower = col.lower()
            if any(keyword in col_lower for keyword in ['type', 'tipo', 'client', 'cliente']):
                important_cols['type'] = col
            elif any(keyword in col_lower for keyword in ['state', 'estado']):
                important_cols['state'] = col
            elif any(keyword in col_lower for keyword in ['server', 'servidor']):
                important_cols['server'] = col
        
        # Análisis por tipo de job
        if 'type' in important_cols and important_cols['type'] in df.columns:
            type_col = important_cols['type']
            print(f"\n📊 ANÁLISIS POR TIPO DE JOB (Columna: {type_col}):")
            type_counts = df[type_col].value_counts()
            for job_type, count in type_counts.head(10).items():
                percentage = (count / len(df)) * 100
                print(f"  {job_type}: {count:,} ({percentage:.1f}%)")
        
        # Análisis por estado
        if 'state' in important_cols and important_cols['state'] in df.columns:
            state_col = important_cols['state']
            print(f"\n📊 ANÁLISIS POR ESTADO (Columna: {state_col}):")
            state_counts = df[state_col].value_counts()
            for state, count in state_counts.head(10).items():
                percentage = (count / len(df)) * 100
                print(f"  {state}: {count:,} ({percentage:.1f}%)")
        
        # Generar reporte JSON
        report = {
            'timestamp': datetime.now().isoformat(),
            'dataset': 'backup1.csv',
            'total_records': len(df),
            'total_columns': len(df.columns),
            'status_column': status_col,
            'analysis_summary': {
                'total_jobs': len(df),
                'numeric_status_jobs': len(non_null_numeric) if 'non_null_numeric' in locals() else 0,
                'success_jobs': success_count if 'success_count' in locals() else 0,
                'error_jobs': error_count if 'error_count' in locals() else 0,
                'error_rate_percent': error_rate if 'error_rate' in locals() else 0
            }
        }
        
        # Guardar reporte
        with open('backup1_analysis_report.json', 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Reporte guardado en 'backup1_analysis_report.json'")
        print("\n" + "=" * 60)
        print("✅ ANÁLISIS COMPLETADO")
        print(f"📊 Dataset: backup1.csv")
        print(f"📈 Total de registros: {len(df):,}")
        
        if 'error_rate' in locals():
            print(f"⚠️ Tasa de error: {error_rate:.1f}%")
            if error_rate > 50:
                print("🚨 ALTA TASA DE ERRORES - Requiere atención inmediata")
            elif error_rate > 20:
                print("⚠️ TASA DE ERRORES MODERADA - Requiere monitoreo")
            else:
                print("✅ TASA DE ERRORES ACEPTABLE")
        
        print("\n🚀 Para análisis ML completo, actualizar sistema principal")
        
        return df
        
    except Exception as e:
        print(f"❌ Error al procesar el archivo: {e}")
        import traceback
        traceback.print_exc()
        return None

def main():
    """Función principal"""
    analyze_backup1_dataset()

if __name__ == "__main__":
    main()
