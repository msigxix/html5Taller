from django.contrib import admin

# Register your models here.
from .models import Perfil, campus, carreras, periodoslectivos, estudiantesresumen, asignaturasresumen


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'bio', 'web')
    
admin.site.register(campus)
admin.site.register(carreras)
admin.site.register(periodoslectivos)
admin.site.register(estudiantesresumen)
admin.site.register(asignaturasresumen)