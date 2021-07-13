from django.contrib import admin
from .models import excel
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(excel)
class excelSheet(ImportExportModelAdmin):
    pass
