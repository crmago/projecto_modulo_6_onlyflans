from django.contrib import admin
from .models import Contacto, Flan

class ContactoAdmin(admin.ModelAdmin):
  pass

admin.site.register(Contacto)


class FlanAdmin(admin.ModelAdmin):
  pass

admin.site.register(Flan, FlanAdmin)
