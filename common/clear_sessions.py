import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myshop.settings")

import django

if 'setup' in dir(django):
    django.setup()

from django.contrib.sessions.models import Session

Session.objects.all().delete()
