from django.contrib import admin

# Register your models here.
from .models import Songs, Movies

admin.site.register(Songs)
admin.site.register(Movies)
