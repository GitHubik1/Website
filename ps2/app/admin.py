from django.contrib import admin
from .models import Myuser
from .models import Message

admin.site.register(Myuser)
admin.site.register(Message)