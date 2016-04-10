from django.contrib import admin
from models import BLEDevice, BLEData


class BLEDataAdmin (admin.TabularInline):
    model = BLEData

class BLEDeviceAdmin(admin.ModelAdmin):
   	inlines = [ BLEDataAdmin ]

class BLEDataAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(BLEData, BLEDataAdmin)
admin.site.register(BLEDevice, BLEDeviceAdmin)
