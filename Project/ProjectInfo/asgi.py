"""
Конфигурация ASGI для проекта DZ_SF_D1.

Он предоставляет вызываемый ASGI как переменную уровня модуля с именем``application``.

Дополнительные сведения об этом файле см.
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DZ_SF_D1.settings')

application = get_asgi_application()
