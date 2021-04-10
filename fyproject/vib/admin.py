from django.contrib import admin
from vib.models import  Contact
from vib.models import  extenduser , Count , Extend
# Register your models here.
admin.site.register(Contact)
admin.site.register(extenduser)
admin.site.register(Count)
admin.site.register(Extend)