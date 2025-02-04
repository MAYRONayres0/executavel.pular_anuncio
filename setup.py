
import sys
import os
from cx_Freeze import setup, Executable

# Definir o que deve ser incluído na pasta final

# Saida de arquivos
configuracao = Executable(
    script='video.py'
)
# Configurar o executável
setup(
    name='Pular_vídeo',
    version='1.0',
    description='Este programa pula anuncio automacicamente, se tiver',
    author='Mayron Ayres',
    options={'build_exe':{
        
        'include_msvcr': True
    }},
    executables=[configuracao]
)
