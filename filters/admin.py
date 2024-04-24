from django.contrib import admin
from .models import GenusModel,ScientificNameModel,SpeciesModel,AnimalModel
# Register your models here.

@admin.register(GenusModel)
class Genus(admin.ModelAdmin):
    pass


@admin.register(SpeciesModel)
class Species(admin.ModelAdmin):
    pass


@admin.register(ScientificNameModel)
class Scientific(admin.ModelAdmin):
    pass


@admin.register(AnimalModel)
class Animal(admin.ModelAdmin):
    pass
