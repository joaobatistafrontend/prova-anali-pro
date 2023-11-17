from django.contrib import admin
from .models import ArtModel

@admin.register(ArtModel)
class ModelAdmin(admin.ModelAdmin):
     list_display = ('participacao', 'motivos', 'dados_contratante', 'anexos', 'normas_compliance', 'user', 'created_at')