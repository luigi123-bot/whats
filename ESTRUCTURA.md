# 📦 Estructura del Proyecto

```
whats/
│
├── 📄 enviar_whatsapp_gui_mejorada.py    # Código fuente principal v2.1
├── 📄 enviar_whatsapp_gui.py             # Versión anterior (legacy)
├── 📄 enviar_whatsapp.py                 # Versión CLI (legacy)
│
├── 📋 requirements.txt                    # Dependencias de Python
├── 🔧 whatsapp_messenger.spec            # Configuración PyInstaller
├── 📊 version.json                        # Info de versión para auto-update
│
├── 🛠️ instalar.ps1                        # Script de instalación
├── 🔨 compilar.ps1                        # Script de compilación
│
├── 📖 README.md                           # Documentación principal
├── 📚 README_v2.1.md                      # Documentación completa v2.1
├── ⚡ INICIO_RAPIDO.md                    # Guía rápida
├── 📝 PyWhatKit_DB.txt                    # Base de datos PyWhatKit
│
├── 🙈 .gitignore                          # Archivos ignorados por Git
│
└── 📁 dist/                               # Carpeta con el .exe (después de compilar)
    └── WhatsApp_Messenger_Pro.exe
```

---

## 🎯 Archivos Principales

### Código Fuente
- **enviar_whatsapp_gui_mejorada.py**: Versión 2.1 con todas las mejoras

### Scripts de Ayuda
- **instalar.ps1**: Instala todas las dependencias automáticamente
- **compilar.ps1**: Compila el programa a .exe

### Configuración
- **requirements.txt**: Lista de paquetes Python necesarios
- **whatsapp_messenger.spec**: Configuración para PyInstaller
- **version.json**: Información de versión para actualizaciones

### Documentación
- **README.md**: Guía principal
- **README_v2.1.md**: Documentación completa de la versión 2.1
- **INICIO_RAPIDO.md**: Guía de inicio rápido

---

## 🔄 Flujo de Trabajo

### Para Desarrolladores:
```
1. Clonar repo
2. Ejecutar instalar.ps1
3. Modificar código
4. Probar: python enviar_whatsapp_gui_mejorada.py
5. Compilar: .\compilar.ps1
6. Actualizar version.json
7. Commit y push
```

### Para Usuarios:
```
1. Descargar release
2. Ejecutar WhatsApp_Messenger_Pro.exe
3. Usar el programa
4. Recibir actualizaciones automáticas
```

---

## 🌟 Características por Archivo

### enviar_whatsapp_gui_mejorada.py
- ✅ Interfaz gráfica moderna
- ✅ Sistema de actualización
- ✅ Multi-país
- ✅ Multi-plataforma
- ✅ Limpieza de números
- ✅ Registro de envíos

### instalar.ps1
- ✅ Verifica Python
- ✅ Instala dependencias
- ✅ Menú interactivo
- ✅ Opciones de inicio

### compilar.ps1
- ✅ Verifica PyInstaller
- ✅ Limpia compilaciones anteriores
- ✅ Compila a .exe
- ✅ Muestra resultado

---

## 📝 Notas para Contribuidores

### Antes de Contribuir:
1. Lee README_v2.1.md
2. Prueba los cambios localmente
3. Actualiza version.json si es necesario
4. Actualiza la documentación

### Versioning:
- **Major (X.0.0)**: Cambios grandes, breaking changes
- **Minor (0.X.0)**: Nuevas características
- **Patch (0.0.X)**: Correcciones de bugs

### Ejemplo:
- v2.0.0 → Rediseño completo UI
- v2.1.0 → Sistema de actualizaciones + multi-país
- v2.1.1 → Corrección de bugs

---

## 🔗 Enlaces Útiles

- **Repositorio**: https://github.com/luigi123-bot/whats
- **Issues**: https://github.com/luigi123-bot/whats/issues
- **Releases**: https://github.com/luigi123-bot/whats/releases

---

**Actualizado: 04/12/2025 - v2.1.0**
