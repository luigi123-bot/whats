# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['enviar_whatsapp_gui_mejorada.py'],
    pathex=[],
    binaries=[],
    datas=[('version.json', '.')],
    hiddenimports=['pywhatkit', 'pyautogui', 'tkinter', 'urllib.request', 'json', 'platform', 'PIL', 'PIL.Image', 'PIL._imaging'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='WhatsApp_Messenger_Pro',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Sin consola para interfaz gráfica
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Puedes agregar 'icon.ico' si tienes un ícono
)
