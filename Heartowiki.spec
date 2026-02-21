# -*- mode: python ; coding: utf-8 -*-
import os
import sys

# onefile: python3xx.dll을 프로젝트 _py_dll에서 로드 (빌드 전 copy_py_dll.py 실행)
_spec_dir = os.getcwd()
_py_dll_dir = os.path.join(_spec_dir, '_py_dll')
binaries_extra = []
for name in ['python312.dll', 'python311.dll', 'python310.dll']:
    local_dll = os.path.join(_py_dll_dir, name)
    if os.path.isfile(local_dll):
        binaries_extra.append((local_dll, '.'))
        break
if not binaries_extra:
    for d in [getattr(sys, 'base_prefix', sys.prefix), os.path.dirname(sys.executable)]:
        for name in ['python312.dll', 'python311.dll', 'python310.dll']:
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
    upx=False,
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'],
)
