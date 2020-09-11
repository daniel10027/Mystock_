from django.contrib import admin
from .models import Article , Categorie, ArrivageExistant, Sortie
# Register your models here.
# Register your models here.

def Pass_true(ModelAdmin, request,queryset):
    queryset.update(active=True)
Pass_true.short_description = "Activer les elements sélectionnés"

def Pass_false(ModelAdmin, request,queryset):
    queryset.update(active=False)
Pass_false.short_description = "Désactiver les elements sélectionnés"


class sd(admin.ModelAdmin):
    search_fields = ["nom"]
    actions = [Pass_true, Pass_false]
    list_display = ('nom', 'categorie','quantite','active','created', 'date_update')

class sds(admin.ModelAdmin):
    search_fields = ["nom"]
    actions = [Pass_true, Pass_false]
    list_display = ('nom','active','created', 'date_update')

class sdss(admin.ModelAdmin):
    search_fields = ["article"]
    actions = [Pass_true, Pass_false]
    list_display = ('article','quantite','active','created', 'date_update')

class sor(admin.ModelAdmin):
    search_fields = ["article"]
    actions = [Pass_true, Pass_false]
    list_display = ('article','quantite','active','created', 'date_update')

admin.site.register(Categorie, sds)

admin.site.register(Article,sd)

admin.site.register(ArrivageExistant,sdss)

admin.site.register(Sortie,sor)