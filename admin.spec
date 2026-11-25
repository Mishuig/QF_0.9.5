# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['admin/main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('assets', 'assets'),
        ('client/ui', 'client/ui'),
        ('fonts', 'fonts'),
    ],
    hiddenimports=[
        'admin',
        'admin.students_tab',
        'admin.tests_tab',
        'admin.results_tab',
        'core',
        'core.ui_kit',
        'core.ui_theme',
        'core.db',
        'core.dialogs',
        'PyQt6.QtSvg',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['tkinter'],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='QuizForge-Admin',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/logo-admin.ico',
)
