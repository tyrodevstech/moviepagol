import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv('DEBUG')
ROOT = Path.home()
DOMAIN_ROOT = 'moviepagol.com'

SITE_URL = 'https://moviepagol.com' if not DEBUG else ''


# DATABASES = {
#     'pgsql': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'moviepagol',
#         'USER': 'postgres',
#         'PASSWORD': '1234',
#         'HOST': 'localhost',
#         'PORT': '9999',
#     }
# }

