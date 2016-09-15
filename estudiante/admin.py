from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from estudiante.models import Estudiante
# Register your models here.
class EstudianteInline(admin.StackedInline):
    model = Estudiante
    can_delete = False

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EstudianteInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)