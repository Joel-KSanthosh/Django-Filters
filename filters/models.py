from django.db import models
# Create your models here.



class GenusModel(models.Model):
    name = models.CharField(max_length=25,unique=True)

    def __str__(self):
        return self.name


class SpeciesModel(models.Model):
    name = models.CharField(max_length=25,unique=True)

    def __str__(self):
        return self.name


class ScientificNameModel(models.Model):
    genus = models.ForeignKey(GenusModel,on_delete=models.CASCADE,null=True)
    species = models.ForeignKey(SpeciesModel,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.genus} {self.species}"

class AnimalModel(models.Model):
    name = models.CharField(max_length=25)
    scientific_name = models.ForeignKey(ScientificNameModel,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name