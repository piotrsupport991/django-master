
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Welcome to our Home Page</h1>")


def about(request):
    return HttpResponse('<h1> Welcome to our about page.... </h1>')


def contact(request):
    return HttpResponse('<h1> Welcome to our contact page.... </h1>')