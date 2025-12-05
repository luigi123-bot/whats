# 📱 WhatsApp Messenger Pro - Guía Completa

## 🆕 Versión 2.1 - Multi-País con Auto-Actualización

**WhatsApp Messenger Pro** es una aplicación de escritorio que te permite enviar mensajes de WhatsApp de forma masiva a múltiples números de teléfono de manera rápida y sencilla.

### ✨ Características principales:
- 🌍 **Soporte Multi-País** - Compatible con 17+ códigos internacionales
- 🔄 **Actualización Automática** - Se actualiza automáticamente
- 💻 **Multi-Plataforma** - Windows, macOS, Linux
- 📞 Envío masivo de mensajes a múltiples contactos
- 🎨 Interfaz gráfica moderna y profesional
- 📊 Contador de números y caracteres en tiempo real
- 🧹 Limpieza automática de números (formato internacional)
- 📂 Importación de números desde archivos
- 📝 Registro detallado de envíos
- ⚙️ Configuración personalizable de tiempos
- ⏹️ Control de inicio/parada durante el envío

---

## 🚀 Inicio Rápido

### Instalación y Compilación
```powershell
# 1. Instalar dependencias
.\instalar.ps1

# 2. Compilar a .exe
.\compilar.ps1

# 3. Ejecutar
.\dist\WhatsApp_Messenger_Pro.exe
```

📖 **[Ver Guía de Inicio Rápido](INICIO_RAPIDO.md)**

📚 **[Ver Documentación Completa v2.1](README_v2.1.md)**

---

## 📋 Requisitos Previos

### Para usar el programa:
- ✅ Windows 10/11
- ✅ WhatsApp Web (se abre automáticamente)
- ✅ Conexión a internet
- ✅ Tu teléfono con WhatsApp conectado

### Para compilar el .exe (opcional):
- Python 3.8 o superior
- PyInstaller
- Dependencias del archivo `requirements.txt`

---

## 🚀 Cómo Compilar el Archivo .exe

### Opción 1: Usando el Script Automático (Recomendado)

1. **Abre PowerShell en la carpeta del proyecto**
   - Click derecho en la carpeta → "Abrir en Terminal" o "PowerShell aquí"

2. **Ejecuta el script de compilación**
   ```powershell
   .\compilar.ps1
   ```

3. **El script hará automáticamente:**
   - ✓ Verificar PyInstaller (y lo instalará si no existe)
   - ✓ Instalar todas las dependencias necesarias
   - ✓ Limpiar archivos de compilaciones anteriores
   - ✓ Compilar la aplicación a .exe
   - ✓ Mostrar el resultado y ubicación del archivo

4. **Encuentra tu .exe**
   - El archivo estará en: `dist\WhatsApp_Messenger_Pro.exe`

### Opción 2: Compilación Manual

```powershell
# 1. Instalar PyInstaller
pip install pyinstaller

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Compilar
pyinstaller --clean whatsapp_messenger.spec
```

---

## 💻 Cómo Usar la Aplicación

### 1️⃣ **Preparar los Números**

#### Opción A: Escribir manualmente
```
573012906861
573001234567
573009876543
```

#### Opción B: Cargar desde archivo
- Click en "📂 Cargar archivo"
- Selecciona un archivo .txt o .csv con los números

#### Opción C: Limpiar números
- Pega números en cualquier formato
- Click en "🧹 Limpiar números"
- El programa automáticamente:
  - Elimina espacios, guiones y paréntesis
  - Agrega el código de país (+57)
  - Remueve ceros iniciales
  - Elimina líneas vacías

**Formatos aceptados:**
```
57 301 2906861
(57) 301-290-6861
0 301 2906861
301 2906861
+57 301 2906861
```

Todos se convierten a: `573012906861`

### 2️⃣ **Escribir el Mensaje**

Escribe el mensaje que deseas enviar a todos los contactos. Puedes incluir:
- Texto normal
- Saltos de línea
- Emojis
- Enlaces

### 3️⃣ **Configurar Opciones**

- **Espera entre mensajes**: Tiempo en segundos entre cada envío (recomendado: 15-20 seg)
- **Tiempo para cargar WhatsApp**: Tiempo que espera para abrir WhatsApp Web (recomendado: 20 seg)
- **Cerrar pestaña automáticamente**: Cierra la pestaña después de cada envío

### 4️⃣ **Iniciar Envío**

1. Click en "▶️ INICIAR ENVÍO"
2. Confirma el número de mensajes a enviar
3. **IMPORTANTE**: El programa abrirá WhatsApp Web
4. Mantén la ventana de WhatsApp Web visible
5. El programa enviará automáticamente todos los mensajes

### 5️⃣ **Durante el Envío**

- 📊 El registro muestra el progreso en tiempo real
- ⏹️ Puedes detener el envío en cualquier momento
- 🔵 El estado indica el progreso actual
- ✅/❌ Cada envío se marca como exitoso o fallido

---

## ⚠️ Consejos Importantes

### ✅ HACER:
- ✓ Mantén WhatsApp Web visible durante el envío
- ✓ Usa tiempos de espera adecuados (15-20 seg mínimo)
- ✓ Verifica que tu teléfono esté conectado a WhatsApp
- ✓ Prueba primero con 2-3 números
- ✓ Mantén la conexión a internet estable

### ❌ NO HACER:
- ✗ No minimices o cambies de ventana durante el envío
- ✗ No uses la computadora para otras tareas
- ✗ No pongas tiempos muy cortos (WhatsApp puede bloquearte)
- ✗ No envíes spam o mensajes no solicitados
- ✗ No uses con fines comerciales sin permiso

---

## 🛠️ Solución de Problemas

### El programa no abre WhatsApp Web
- **Solución**: Aumenta el "Tiempo para cargar WhatsApp" a 25-30 segundos

### Los mensajes no se envían
- Verifica que WhatsApp Web esté funcionando correctamente
- Revisa que los números estén en formato correcto
- Aumenta el tiempo de espera entre mensajes

### Error "PyInstaller no encontrado"
```powershell
pip install pyinstaller
```

### Error durante la compilación
```powershell
# Reinstalar dependencias
pip install --upgrade -r requirements.txt

# Limpiar y volver a compilar
Remove-Item -Path "build","dist" -Recurse -Force
pyinstaller --clean whatsapp_messenger.spec
```

### El .exe no abre o da error
- Verifica que el antivirus no esté bloqueándolo
- Ejecuta como administrador
- Recompila el programa

---

## 📦 Compartir el Programa

Una vez compilado, puedes compartir el archivo `WhatsApp_Messenger_Pro.exe` con cualquier persona.

**El usuario NO necesita:**
- ❌ Tener Python instalado
- ❌ Instalar dependencias
- ❌ Conocimientos técnicos

**Solo necesita:**
- ✅ Windows 10/11
- ✅ WhatsApp en su teléfono
- ✅ Conexión a internet

---

## 📁 Estructura del Proyecto

```
whats/
│
├── enviar_whatsapp_gui_mejorada.py  # Código fuente principal
├── requirements.txt                  # Dependencias de Python
├── whatsapp_messenger.spec          # Configuración de PyInstaller
├── compilar.ps1                      # Script de compilación
├── README.md                         # Este archivo
│
└── dist/                            # Carpeta con el .exe (después de compilar)
    └── WhatsApp_Messenger_Pro.exe
```

---

## 🔒 Consideraciones Legales

- Este programa es solo para uso personal
- No envíes spam o mensajes no solicitados
- Respeta las políticas de WhatsApp
- Usa con responsabilidad
- El uso indebido puede resultar en el bloqueo de tu cuenta de WhatsApp

---

## 📞 Soporte

Si tienes problemas:
1. Revisa la sección de "Solución de Problemas"
2. Verifica que todos los requisitos estén cumplidos
3. Intenta recompilar el programa

---

## 📝 Notas de la Versión

### v2.0 (Actual)
- 🎨 Interfaz gráfica completamente rediseñada
- 🚀 Mejoras en rendimiento
- 📊 Contadores en tiempo real
- 🧹 Limpieza automática de números
- 📂 Importación de archivos
- ⚙️ Configuración avanzada
- 🛠️ Mejor manejo de errores
- 📝 Registro detallado de operaciones

---

## ⭐ Características Futuras (Posibles)

- 📎 Envío de archivos adjuntos
- 🎯 Programación de envíos
- 📊 Estadísticas detalladas
- 💾 Guardar configuraciones
- 🔄 Reintento automático de envíos fallidos

---

**¡Disfruta de WhatsApp Messenger Pro! 📱✨**
