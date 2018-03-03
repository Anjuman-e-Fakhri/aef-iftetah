from django.contrib import admin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from .models import Task, Committee
# Register your models here.

class TaskResource(resources.ModelResource):
    committee = fields.Field(
        column_name='committee',
        attribute='committee',
        widget=ForeignKeyWidget(Committee, 'name'))

    class Meta:
        model = Task
        skip_unchanged = True
        report_skipped = False
        fields =('committee', 'description', 'status','due_date')

class TaskAdmin(ImportExportModelAdmin):
    list_display = ['description','committee', 'status','due_date']
    list_filter = ['committee', 'status']
    search_fields = ['committee', 'description', 'status','due_date']
    resource_class = TaskResource

admin.site.register(Task, TaskAdmin)

admin.site.register(Committee)