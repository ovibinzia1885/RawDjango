from django.contrib import admin
from .models import FilesAdmin
from .models import application,Apply
admin.site.register(application)
admin.site.register(Apply)
admin.site.register(FilesAdmin)
