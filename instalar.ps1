# Script de instalacion rapida para WhatsApp Messenger Pro

Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "  WhatsApp Messenger Pro v2.1 - Instalacion" -ForegroundColor Green
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# Verificar Python
Write-Host "[1/3] Verificando Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "   OK Python encontrado: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "   X Python no encontrado!" -ForegroundColor Red
    Write-Host "   Descarga Python desde: https://www.python.org/downloads/" -ForegroundColor Yellow
    Write-Host ""
    pause
    exit 1
}

Write-Host ""
Write-Host "[2/3] Instalando dependencias..." -ForegroundColor Yellow
pip install -r requirements.txt

if ($LASTEXITCODE -eq 0) {
    Write-Host "   OK Dependencias instaladas correctamente" -ForegroundColor Green
} else {
    Write-Host "   X Error al instalar dependencias" -ForegroundColor Red
    pause
    exit 1
}

Write-Host ""
Write-Host "[3/3] Verificando instalacion..." -ForegroundColor Yellow

# Verificar paquetes
$packages = @("pywhatkit", "pyautogui")
$allInstalled = $true

foreach ($package in $packages) {
    try {
        python -c "import $package" 2>$null
        if ($LASTEXITCODE -eq 0) {
            Write-Host "   OK $package instalado" -ForegroundColor Green
        } else {
            Write-Host "   X $package NO instalado" -ForegroundColor Red
            $allInstalled = $false
        }
    } catch {
        Write-Host "   X Error verificando $package" -ForegroundColor Red
        $allInstalled = $false
    }
}

Write-Host ""
if ($allInstalled) {
    Write-Host "===============================================" -ForegroundColor Cyan
    Write-Host "     INSTALACION COMPLETADA CON EXITO" -ForegroundColor Green
    Write-Host "===============================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Que deseas hacer ahora?" -ForegroundColor White
    Write-Host ""
    Write-Host "  1. Ejecutar el programa" -ForegroundColor Yellow
    Write-Host "  2. Compilar a .exe" -ForegroundColor Yellow
    Write-Host "  3. Salir" -ForegroundColor Yellow
    Write-Host ""
    
    $choice = Read-Host "Selecciona una opcion (1-3)"
    
    switch ($choice) {
        "1" {
            Write-Host ""
            Write-Host "Iniciando programa..." -ForegroundColor Cyan
            python enviar_whatsapp_gui_mejorada.py
        }
        "2" {
            Write-Host ""
            Write-Host "Iniciando compilacion..." -ForegroundColor Cyan
            .\compilar.ps1
        }
        "3" {
            Write-Host ""
            Write-Host "Hasta pronto!" -ForegroundColor Green
        }
        default {
            Write-Host ""
            Write-Host "Opcion invalida. Saliendo..." -ForegroundColor Yellow
        }
    }
} else {
    Write-Host "===============================================" -ForegroundColor Cyan
    Write-Host "     ERROR EN LA INSTALACION" -ForegroundColor Red
    Write-Host "===============================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Intenta ejecutar manualmente:" -ForegroundColor Yellow
    Write-Host "  pip install --upgrade -r requirements.txt" -ForegroundColor White
}

Write-Host ""
Write-Host "Presiona cualquier tecla para salir..."
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
