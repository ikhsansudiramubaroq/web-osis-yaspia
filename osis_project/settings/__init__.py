from .base import * 

# Jika ada setting environment 'production', pakai pro.py, 
# jika tidak, pakai local.py

from decouple import config 

if config('DEBUG', default=False, cast=bool):
    from .local import *
else :
    from .pro import *