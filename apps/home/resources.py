from import_export import resources
from .models import Aso,Colaborador
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

class AsoResource(resources.ModelResource):
    class Meta:
        model = Aso
        import_id_fields = ('id',)
        aso = fields.Field(
            column_name='nome',
            attribute='nome',
            widget=ForeignKeyWidget(Colaborador, 'nome'))