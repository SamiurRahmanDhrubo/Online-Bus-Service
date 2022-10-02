from django.shortcuts import render, HttpResponse

# Create your views here.
def adminp_view(request):
    return HttpResponse("<h1>This is admin page</h1>")