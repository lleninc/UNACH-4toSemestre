# ============================================================
# UNACH - 4to Semestre 2026-1S
# Completa la estructura de carpetas en el repo existente
# 
# Ejecutar desde:
# E:\Unach\Semestre4\EstudioGITClaude\UNACH-4toSemestre
#
#   .\completar_estructura.ps1
# ============================================================

$base = $PSScriptRoot
if (-not $base) { $base = Get-Location }

$materias = @(
    "01-Metodos-Numericos",
    "02-Machine-Learning",
    "03-Metaheuristicas",
    "04-Analitica-de-Datos",
    "05-Administracion-BD"
)

$unidades = @(
    "Unidad1",
    "Unidad2",
    "Unidad3",
    "Unidad4"
)

# Subcarpetas dentro de cada Unidad (Tema + Semana)
$temas = @(
    "Tema1-Semana1",
    "Tema1-Semana2",
    "Tema2-Semana3",
    "Tema2-Semana4"
)

Write-Host ""
Write-Host "=================================================" -ForegroundColor Cyan
Write-Host "  UNACH 4to Semestre - Completar estructura" -ForegroundColor Cyan
Write-Host "  Base: $base" -ForegroundColor Cyan
Write-Host "=================================================" -ForegroundColor Cyan
Write-Host ""

$creadas = 0
$existentes = 0

foreach ($materia in $materias) {
    Write-Host "[$materia]" -ForegroundColor Yellow

    foreach ($unidad in $unidades) {
        foreach ($tema in $temas) {
            $ruta = Join-Path $base "$materia\$unidad\$tema"

            if (-Not (Test-Path $ruta)) {
                New-Item -ItemType Directory -Path $ruta -Force | Out-Null

                # Crear notas.md vacio en cada carpeta
                $notasPath = Join-Path $ruta "notas.md"
                $unidadNum = $unidad -replace "Unidad", ""
                $temaNum   = ($tema -split "-")[0] -replace "Tema", ""
                $semanaNum = ($tema -split "Semana")[1]
                $contenido = "# $materia - U$unidadNum T$temaNum S$semanaNum`n`n## Notas de clase`n`n## Quiz`n`n## Actividades`n"
                Set-Content -Path $notasPath -Value $contenido -Encoding UTF8

                Write-Host "  [+] $unidad\$tema" -ForegroundColor Green
                $creadas++
            } else {
                Write-Host "  [=] $unidad\$tema (ya existe)" -ForegroundColor DarkGray
                $existentes++
            }
        }
    }
    Write-Host ""
}

Write-Host "=================================================" -ForegroundColor Cyan
Write-Host "  Carpetas creadas  : $creadas" -ForegroundColor Green
Write-Host "  Ya existian       : $existentes" -ForegroundColor DarkGray
Write-Host "=================================================" -ForegroundColor Cyan
Write-Host ""
