from django.contrib import admin
from django.contrib.auth.models import Group, User

from core.models import Pdf

admin.site.register(Pdf)
# admin.site.unregister(User)
