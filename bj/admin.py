from django.contrib import admin
from .models import Job_english,Company,Role,Job_hinglish,Job_hindi
# Register your models here.
admin.site.register(Job_english)
admin.site.register(Job_hinglish)
admin.site.register(Job_hindi)
admin.site.register(Role)
admin.site.register(Company)
