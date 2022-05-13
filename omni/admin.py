from django.contrib import admin

# Register your models here.
from omni.models import PedigreeNode,Pigeon, Pedigree,StatutPedigree
admin.site.register(Pedigree)
admin.site.register(Pigeon)
admin.site.register(PedigreeNode)
admin.site.register(StatutPedigree)
