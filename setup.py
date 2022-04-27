from setuptools import setup

APP = ['App.py']
DATA_FILES = ['data/dyson_am09.json', 'data/icon.png']
OPTIONS = {
    'argv_emulation': True,
    'iconfile':'data/icon.icns',
    'plist': {
        'CFBundleShortVersionString': '0.2.0',
        'LSUIElement': True,
    },
    'packages': ['rumps', 'broadlink', 'cffi', 'src'],
}

setup(
    app=APP,
    name='Dyson Fan',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    install_requires=['rumps', 'broadlink', 'cffi']
)