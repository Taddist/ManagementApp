from django.contrib import admin
from log.models import UserProfile , Conge ,Raison ,Synthese ,Nonactivite,Typedocument,Document, Pole ,Contrat,Role,Situation,Souspole,TrashConge,Salaire
# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Conge)
admin.site.register(Raison)
admin.site.register(Nonactivite)
admin.site.register(Synthese)
admin.site.register(Typedocument)
admin.site.register(Document)
admin.site.register(Pole)
admin.site.register(Contrat)
admin.site.register(Role)
admin.site.register(Situation)
admin.site.register(Souspole)
admin.site.register(TrashConge)
admin.site.register(Salaire)

