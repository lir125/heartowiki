# -*- mode: python ; coding: utf-8 -*-
import os
import sys

# onefile 실행 시 python3xx.dll 누락 방지: 현재 Python의 DLL을 명시적으로 포함
binaries_extra = []
for d in [getattr(sys, 'base_prefix', sys.prefix), sys.prefix, os.path.dirname(sys.executable)]:
    for name in ['python312.dll', 'python311.dll', 'python310.dll', 'python3.dll']:
        dll = os.path.join(d, name)
        if os.path.isfile(dll):
            binaries_extra.append((dll, '.'))
            break
    if binaries_extra:
        break

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=binaries_extra,
    datas=[('index.html', '.')],
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
    name='Heartowiki',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=['python312.dll', 'python311.dll', 'python310.dll', 'python3.dll'],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)
