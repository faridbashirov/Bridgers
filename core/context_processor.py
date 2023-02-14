from .models import Services

def service_renderer(request):
    return {
       'services': Services.objects.all()
    }