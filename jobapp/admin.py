from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Job_Details


# Register your models here.
@admin.register(Job_Details)
class Job_DetailsAdmin(ImportExportModelAdmin):
	list_display = ('Job_ID','Company_Name','Job_Catagory','Min_Exp','Max_Exp','Company_ID',)

