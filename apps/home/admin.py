from importlib import resources
from django.contrib import admin
from django.forms import widgets
from sqlalchemy import ForeignKey
from apps.home.models import *

from django.contrib import admin 

from import_export.admin import ImportExportActionModelAdmin
from .resources import AsoResource


    




class ColaboradorAdmin(ImportExportActionModelAdmin):
    pass

class AsoAdmin(ImportExportActionModelAdmin):
    pass
class EpiAdmin(ImportExportActionModelAdmin):
    pass

admin.site.register(Epi,EpiAdmin)
admin.site.register(Colaborador, ColaboradorAdmin)
admin.site.register(Aso, ColaboradorAdmin)
admin.site.register(Cracha)
admin.site.register(Rac)


