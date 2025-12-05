# 🌍 WhatsApp Messenger Pro v2.1 - Multi-País con Auto-Actualización

## 🆕 Novedades de la Versión 2.1

### ✨ Características Nuevas:

1. **🌎 Soporte Multi-País**
   - Selector de código de país integrado
   - Compatible con códigos de: USA (1), México (52), Argentina (54), Brasil (55), Chile (56), Colombia (57), Venezuela (58), y más países de Centroamérica y Sudamérica
   - Limpieza automática adaptada al país seleccionado

2. **🔄 Sistema de Actualización Automática**
   - Verificación automática de actualizaciones al iniciar
   - Botón de actualización manual (🔄)
   - Notificaciones de nuevas versiones disponibles
   - Descarga directa desde GitHub

3. **💻 Compatible con PC y Móviles**
   - Detección automática del sistema operativo (Windows, macOS, Linux)
   - Ajuste automático de la interfaz según el sistema
   - Modo especial para WhatsApp móvil/escritorio

4. **🎨 Mejoras en la Interfaz**
   - Indicador de sistema operativo en el header
   - Mejor adaptación a diferentes pantallas
   - Controles más intuitivos

---

## 📋 Requisitos

### Para Usar el Programa:
- ✅ Windows 10/11, macOS, o Linux
- ✅ WhatsApp (en PC o móvil)
- ✅ Conexión a internet
- ✅ Navegador web

### Para Compilar:
- Python 3.8+
- Dependencias del `requirements.txt`

---

## 🚀 Compilar el .exe

### Método Automático (PowerShell):
```powershell
.\compilar.ps1
```

### Método Manual:
```powershell
pip install -r requirements.txt
pip install pyinstaller
pyinstaller --clean whatsapp_messenger.spec
```

El archivo `WhatsApp_Messenger_Pro.exe` estará en `dist/`

---

## 💻 Guía de Uso

### 1. Configurar el Código de País

En la sección **⚙️ Configuración**, selecciona el código de tu país:
- 🇨🇴 Colombia: 57
- 🇲🇽 México: 52
- 🇦🇷 Argentina: 54
- 🇧🇷 Brasil: 55
- 🇨🇱 Chile: 56
- 🇺🇸 USA/Canadá: 1
- Y más...

### 2. Ingresar Números

Puedes ingresar números en cualquier formato:
```
3012906861
57 301 2906861
(57) 301-290-6861
+57 301 2906861
```

Luego haz clic en **🧹 Limpiar números** para formatearlos automáticamente.

### 3. Configurar Envío

- **Espera entre mensajes**: 15-20 segundos recomendado
- **Tiempo para cargar WhatsApp**: 20-25 segundos
- **Cerrar pestaña automáticamente**: Activado (recomendado)
- **Modo WhatsApp móvil/escritorio**: Activar si usas versión de escritorio

### 4. Escribir Mensaje

Personaliza tu mensaje con:
- Texto normal
- Saltos de línea
- Emojis 😊
- Enlaces

### 5. Enviar

1. Click en **▶️ INICIAR ENVÍO**
2. Confirma el número de destinatarios
3. WhatsApp Web se abrirá automáticamente
4. Mantén la ventana visible
5. El programa enviará los mensajes automáticamente

---

## 🔄 Sistema de Actualización

### Automática:
- Al iniciar el programa, se verifica automáticamente si hay actualizaciones
- Si hay una nueva versión, te preguntará si deseas descargarla

### Manual:
- Haz clic en el botón **🔄** en el header
- El programa verificará si hay actualizaciones
- Si existe una nueva versión, podrás descargarla

### Sin Internet:
- El programa funciona sin conexión
- Solo no podrá verificar actualizaciones

---

## 🌍 Compatibilidad Multi-Plataforma

### Windows 10/11
- ✅ Totalmente compatible
- ✅ Archivo .exe portable
- ✅ No requiere instalación

### macOS
- ✅ Compatible con Python
- ⚠️ Requiere permisos de accesibilidad para PyAutoGUI
- 📝 Ejecutar: `python3 enviar_whatsapp_gui_mejorada.py`

### Linux
- ✅ Compatible con Python
- ⚠️ Requiere instalar tkinter: `sudo apt-get install python3-tk`
- 📝 Ejecutar: `python3 enviar_whatsapp_gui_mejorada.py`

---

## 🛠️ Solución de Problemas

### No se detectan actualizaciones
- **Causa**: Sin conexión a internet o GitHub no accesible
- **Solución**: Verifica tu conexión o descarga manualmente desde GitHub

### Error al limpiar números
- **Causa**: Código de país incorrecto
- **Solución**: Selecciona el código correcto en Configuración

### WhatsApp no abre o no envía
- **Causa**: Tiempo de espera muy corto
- **Solución**: Aumenta "Tiempo para cargar WhatsApp" a 25-30 seg

### El programa no inicia
- **Causa**: Faltan dependencias o antivirus bloqueando
- **Solución**: 
  - Ejecuta como administrador
  - Agrega excepción en el antivirus
  - Reinstala con `pip install -r requirements.txt`

---

## 📱 Uso con WhatsApp Móvil

1. Abre WhatsApp Web en tu navegador
2. Escanea el código QR con tu teléfono
3. Activa **"Modo WhatsApp móvil/escritorio"** en Configuración
4. Inicia el envío normalmente

---

## 🔒 Seguridad y Privacidad

- ✅ No recopilamos ningún dato
- ✅ Todo funciona localmente en tu PC
- ✅ No enviamos información a servidores externos
- ✅ Código fuente abierto en GitHub
- ⚠️ Usa responsablemente, no envíes spam

---

## 📞 Códigos de País Soportados

| País | Código | Formato Ejemplo |
|------|--------|-----------------|
| 🇺🇸 USA/Canadá | 1 | 1 555 123 4567 |
| 🇲🇽 México | 52 | 52 55 1234 5678 |
| 🇦🇷 Argentina | 54 | 54 11 1234 5678 |
| 🇧🇷 Brasil | 55 | 55 11 91234 5678 |
| 🇨🇱 Chile | 56 | 56 9 1234 5678 |
| 🇨🇴 Colombia | 57 | 57 301 234 5678 |
| 🇻🇪 Venezuela | 58 | 58 412 123 4567 |
| 🇬🇹 Guatemala | 502 | 502 1234 5678 |
| 🇸🇻 El Salvador | 503 | 503 1234 5678 |
| 🇭🇳 Honduras | 504 | 504 1234 5678 |
| 🇳🇮 Nicaragua | 505 | 505 1234 5678 |
| 🇨🇷 Costa Rica | 506 | 506 1234 5678 |
| 🇵🇦 Panamá | 507 | 507 1234 5678 |
| 🇭🇹 Haití | 509 | 509 1234 5678 |
| 🇧🇴 Bolivia | 591 | 591 7 123 4567 |
| 🇪🇨 Ecuador | 593 | 593 98 123 4567 |
| 🇵🇾 Paraguay | 595 | 595 981 123 456 |

---

## 📝 Notas de Versiones

### v2.1.0 (04/12/2025)
- ✨ Sistema de actualización automática
- 🌎 Soporte multi-país con 17+ códigos
- 💻 Compatible con Windows, macOS, Linux
- 📱 Modo especial para WhatsApp móvil
- 🎨 Mejoras en la interfaz
- 🔧 Optimizaciones de rendimiento

### v2.0.0
- 🎨 Interfaz gráfica completamente rediseñada
- 📊 Contadores en tiempo real
- 🧹 Limpieza automática de números
- 📂 Importación de archivos

---

## 🚀 Compartir el Programa

El archivo `.exe` compilado es completamente portable:
- ✅ Funciona sin instalación
- ✅ No requiere Python
- ✅ Se puede compartir por WhatsApp, email, USB, etc.
- ✅ Recibe actualizaciones automáticas

---

## 📄 Licencia

Este proyecto es de código abierto. Úsalo libremente pero con responsabilidad.

---

## 🔗 Enlaces

- **GitHub**: https://github.com/luigi123-bot/whats
- **Releases**: https://github.com/luigi123-bot/whats/releases
- **Reportar problemas**: https://github.com/luigi123-bot/whats/issues

---

**¡Disfruta de WhatsApp Messenger Pro v2.1! 📱✨🌍**
