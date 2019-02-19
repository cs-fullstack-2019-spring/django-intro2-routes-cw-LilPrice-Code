# setting the routes
from django.http import HttpResponse


def gogetthegood(request):
    return HttpResponse("Here you go!")

def happyhappyjoyjoy(request):
    return HttpResponse("A Ren & Stimpy song.")

