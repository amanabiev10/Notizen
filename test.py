import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notizen.settings')

django.setup()

from accounts.models import User

max = User.objects.get(username='max')
max.set_password('Start123')
max.save()

#test