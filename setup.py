# -*- coding: utf-8 -*-
from distutils.core import setup
from glob import glob


PACKAGE_NAME = 'chessly'
PACKAGE_VERSION = '1.0.0'


setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    description='The game of Chess in python',
    author='Alok Gandhi',
    author_email='alok.gandhi2002@gmail.com',
    url='https://github.com/alok1974/chessly',
    packages=[
        'chessly',
        'chessly.core',
        'chessly.element',
        'chessly.gui',
        'chessly.resource',
    ],
    package_data={
        'chessly': ['resource/*/*.*'],
    },
    package_dir={
        'chessly': 'src/chessly'
    },
    download_url=(
        'https://github.com/alok1974/chessly/archive/'
        f'v{PACKAGE_VERSION}.tar.gz'),
    scripts=glob('src/scripts/*'),
    install_requires=[
        'Pillow >=7.2.0',
        'PySide2 >=5.15.0',
        'imageio >=2.9.0',
        'imageio-ffmpeg >=0.4.2',
        'stockfish >=3.10.2'
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language:: Python:: 3.7',
        'Topic :: Games/Entertainment :: Board Games',
    ],
)
