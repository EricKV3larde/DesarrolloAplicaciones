from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'contraseña', 'fecha_nacimiento', 'sexo', 'ciudad')
    filter_horizontal = ('interes', 'aficiones')

admin.site.register(Usuario, UsuarioAdmin)
