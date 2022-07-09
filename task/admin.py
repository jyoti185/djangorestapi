from django.contrib import admin
from task .models import EmployeeModels
@admin.register(EmployeeModels)
class EmployeeModel(admin.ModelAdmin):
    list_display = ['id','name','email','phone_no','gender','address']
