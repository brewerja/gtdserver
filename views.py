from django.http import HttpResponse
from gtdserver.models import Gtd

def hello(request):
    attack = Gtd.objects.all()[22]
    return HttpResponse(attack)
