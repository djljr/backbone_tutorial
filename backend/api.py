from tastypie.resources import ModelResource
from backend.models import Wine

class WineResource(ModelResource):
    class Meta:
        queryset = Wine.objects.all()
        resource_name = 'wines'
