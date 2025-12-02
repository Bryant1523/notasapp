# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['app_nc.py'],
    pathex=[],
    binaries=[],
    datas=[('plantilla_default.xlsx', '.'), ('plantilla_APC.xlsx', '.'), ('plantilla_PCV.xlsx', '.'), ('plantilla_CYM.xlsx', '.'), ('plantilla_EFE.xlsx', '.'), ('Alimentos Polar (Completo).webp', '.'), ('Pepsi-Cola.webp', '.'), ('Cervecería Polar (Completo).webp', '.'), ('Productos EFE.webp', '.'), ('Alimentos Polar (Solo Logo).webp', '.'), ('Cervecería Polar (Solo Logo).webp', '.'), ('Logo Empresas Polar (Color).png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='GeneradorNC',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
