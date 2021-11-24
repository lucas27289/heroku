from django.http import HttpResponse

# Create your views here.
def index(requst):
    return HttpResponse('esta en el index de app')