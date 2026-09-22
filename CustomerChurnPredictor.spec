# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_dynamic_libs
from PyInstaller.utils.hooks import collect_all

datas = [('models', 'models'), ('templates', 'templates')]
binaries = [('C:/Windows/WinSxS/amd64_microsoft-windows-m..namespace-downlevel_31bf3856ad364e35_10.0.26100.1_none_c4588310e9a6e860/api-ms-win-crt-convert-l1-1-0.dll', '.'), ('C:/Windows/WinSxS/amd64_microsoft-windows-m..namespace-downlevel_31bf3856ad364e35_10.0.26100.1_none_c4588310e9a6e860/api-ms-win-crt-environment-l1-1-0.dll', '.'), ('C:/Windows/WinSxS/amd64_microsoft-windows-m..namespace-downlevel_31bf3856ad364e35_10.0.26100.1_none_c4588310e9a6e860/api-ms-win-crt-filesystem-l1-1-0.dll', '.'), ('C:/Windows/WinSxS/amd64_microsoft-windows-m..namespace-downlevel_31bf3856ad364e35_10.0.26100.1_none_c4588310e9a6e860/api-ms-win-crt-heap-l1-1-0.dll', '.'), ('C:/Windows/WinSxS/amd64_microsoft-windows-m..namespace-downlevel_31bf3856ad364e35_10.0.26100.1_none_c4588310e9a6e860/api-ms-win-crt-locale-l1-1-0.dll', '.'), ('C:/Windows/WinSxS/amd64_microsoft-windows-m..namespace-downlevel_31bf3856ad364e35_10.0.26100.1_none_c4588310e9a6e860/api-ms-win-crt-math-l1-1-0.dll', '.'), ('C:/Windows/WinSxS/amd64_microsoft-windows-m..namespace-downlevel_31bf3856ad364e35_10.0.26100.1_none_c4588310e9a6e860/api-ms-win-crt-process-l1-1-0.dll', '.'), ('C:/Windows/WinSxS/amd64_microsoft-windows-m..namespace-downlevel_31bf3856ad364e35_10.0.26100.1_none_c4588310e9a6e860/api-ms-win-crt-runtime-l1-1-0.dll', '.'), ('C:/Windows/WinSxS/amd64_microsoft-windows-m..namespace-downlevel_31bf3856ad364e35_10.0.26100.1_none_c4588310e9a6e860/api-ms-win-crt-stdio-l1-1-0.dll', '.'), ('C:/Windows/WinSxS/amd64_microsoft-windows-m..namespace-downlevel_31bf3856ad364e35_10.0.26100.1_none_c4588310e9a6e860/api-ms-win-crt-string-l1-1-0.dll', '.'), ('C:/Windows/WinSxS/amd64_microsoft-windows-m..namespace-downlevel_31bf3856ad364e35_10.0.26100.1_none_c4588310e9a6e860/api-ms-win-crt-time-l1-1-0.dll', '.'), ('C:/Windows/WinSxS/amd64_microsoft-windows-m..namespace-downlevel_31bf3856ad364e35_10.0.26100.1_none_c4588310e9a6e860/api-ms-win-crt-utility-l1-1-0.dll', '.'), ('C:/Windows/WinSxS/amd64_microsoft-windows-ucrt_31bf3856ad364e35_10.0.26100.8875_none_475e723fc9a13486/ucrtbase.dll', '.')]
hiddenimports = []
binaries += collect_dynamic_libs('torch')
binaries += collect_dynamic_libs('numpy')
tmp_ret = collect_all('sklearn')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['desktop_app.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
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
    [],
    exclude_binaries=True,
    name='CustomerChurnPredictor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='CustomerChurnPredictor',
)
