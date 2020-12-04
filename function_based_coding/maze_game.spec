# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['maze_game.py'],
             pathex=['/Users/preetikumar/python_for_arkin/function_based_coding'],
             binaries=[],
             datas= [
                    ('pgzero', 'pgzero'),
                    ('images', 'images'),
                    ('sounds', 'sounds'),
                    ('fonts', 'fonts'),
                    ('maze_game.py', '.')
            ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='maze_game',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='maze_game')
app = BUNDLE(exe,
         name='myscript.app',
         icon=None,
         bundle_identifier=None,
         info_plist={
            'NSPrincipalClass': 'NSApplication',
            'NSAppleScriptEnabled': False,
            'CFBundleDocumentTypes': [
                {
                    'CFBundleTypeName': 'My File Format',
                    'CFBundleTypeIconFile': 'MyFileIcon.icns',
                    'LSItemContentTypes': ['com.example.myformat'],
                    'LSHandlerRank': 'Owner'
                    }
                ]
            },
         )

distpath = '.'
