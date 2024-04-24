import django_filters;
from .models import GenusModel


#Inclusion Filter
class GenusFilters(django_filters.FilterSet):
    class Meta:
        model = GenusModel
        fields = {
            "id" : ('exact',),
            'name' : ["exact" ,"icontains"],
        }



