from django.contrib import admin
from .models import Tenants
# Register your models here.

class TenantsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}

admin.site.register(Tenants,TenantsAdmin)