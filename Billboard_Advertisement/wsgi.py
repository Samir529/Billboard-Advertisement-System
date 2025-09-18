"""
WSGI config for Billboard_Advertisement project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Billboard_Advertisement.settings')

application = get_wsgi_application()
static_root = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'staticfiles')
application = WhiteNoise(application, root=static_root)
