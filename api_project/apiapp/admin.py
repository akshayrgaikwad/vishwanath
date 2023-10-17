from django.contrib import admin
from .models import EmployeeModel

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_id','employee_name','gender','designation','mobile','salary']

admin.site.register(EmployeeModel,EmployeeAdmin)
