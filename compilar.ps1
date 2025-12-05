# Script para compilar WhatsApp Messenger Pro a .exe
# Asegurate de tener instalado PyInstaller antes de ejecutar

Write-Host "================================================" -ForegroundColor Cyan
Write-Host "  WhatsApp Messenger Pro - Compilador" -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si PyInstaller esta instalado
Write-Host "[1/5] Verificando PyInstaller..." -ForegroundColor Yellow
try {
    $pyinstaller = Get-Command pyinstaller -ErrorAction Stop
    Write-Host "   OK PyInstaller encontrado" -ForegroundColor Green
} catch {
    Write-Host "   X PyInstaller no encontrado. Instalando..." -ForegroundColor Red
    pip install pyinstaller
    Write-Host "   OK PyInstaller instalado" -ForegroundColor Green
}

Write-Host ""
Write-Host "[2/5] Instalando dependencias..." -ForegroundColor Yellow
pip install -r requirements.txt
Write-Host "   OK Dependencias instaladas" -ForegroundColor Green

Write-Host ""
Write-Host "[3/5] Limpiando archivos anteriores..." -ForegroundColor Yellow
if (Test-Path "build") {
    Remove-Item -Path "build" -Recurse -Force
    Write-Host "   OK Carpeta 'build' eliminada" -ForegroundColor Green
}
if (Test-Path "dist") {
    Remove-Item -Path "dist" -Recurse -Force
    Write-Host "   OK Carpeta 'dist' eliminada" -ForegroundColor Green
}

Write-Host ""
Write-Host "[4/5] Compilando aplicacion..." -ForegroundColor Yellow
Write-Host "   (Esto puede tardar varios minutos...)" -ForegroundColor Cyan
pyinstaller --clean whatsapp_messenger.spec

if ($LASTEXITCODE -eq 0) {
    Write-Host "   OK Compilacion exitosa" -ForegroundColor Green
    
    Write-Host ""
    Write-Host "[5/5] Verificando archivo ejecutable..." -ForegroundColor Yellow
    if (Test-Path "dist\WhatsApp_Messenger_Pro.exe") {
        Write-Host "   OK Archivo .exe creado correctamente" -ForegroundColor Green
        $fileSize = (Get-Item "dist\WhatsApp_Messenger_Pro.exe").Length / 1MB
        Write-Host "   INFO Tamanio: $([math]::Round($fileSize, 2)) MB" -ForegroundColor Cyan
        
        Write-Host ""
        Write-Host "================================================" -ForegroundColor Cyan
        Write-Host "           OK COMPILACION COMPLETADA            " -ForegroundColor Green
        Write-Host "================================================" -ForegroundColor Cyan
        Write-Host ""
        Write-Host "El archivo ejecutable esta en:" -ForegroundColor White
        Write-Host "   CARPETA dist\WhatsApp_Messenger_Pro.exe" -ForegroundColor Yellow
        Write-Host ""
        Write-Host "Puedes compartir este archivo .exe con cualquier persona." -ForegroundColor White
        Write-Host "No necesitan tener Python instalado para usarlo." -ForegroundColor White
        Write-Host ""
        
        # Preguntar si desea abrir la carpeta
        $response = Read-Host "Deseas abrir la carpeta del ejecutable? (S/N)"
        if ($response -eq "S" -or $response -eq "s") {
            explorer.exe "dist"
        }
    } else {
        Write-Host "   X Error: No se encontro el archivo .exe" -ForegroundColor Red
    }
} else {
    Write-Host ""
    Write-Host "   X Error durante la compilacion" -ForegroundColor Red
    Write-Host "   Revisa los mensajes de error anteriores" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Presiona cualquier tecla para salir..."
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown')
