
from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, "home.html")


def about(request):
    student_list = [
        {
            "name": "Jawad",
            "roll": "0011"
        },
         {
            "name": "Umaima",
            "roll": "0012"
        },
         {
            "name": "Shumaila",
            "roll": "0013"
        }
    ]
    return render(request, "about.html", 
                  
                  {'data': student_list}
                  
                  )


def contact(request):
    pass