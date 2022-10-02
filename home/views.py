from django.shortcuts import render, HttpResponse

# Create your views here.
def landing_view(request):
    return HttpResponse("<h1>This is our Landing page</h1>")
def signupop_view(request):
    return HttpResponse("<h1>This is our SignUp option page</h1>")
def signuppassenger_view(request):
    return HttpResponse("<h1>This is our SignUp as passenger page</h1>")
def signupcompany_view(request):
    return HttpResponse("<h1>This is our SignUp as company page</h1>")
def login_view(request):
    return HttpResponse("<h1>This is our Login page</h1>")
def homec_view(request):
    return HttpResponse("<h1>This is our Homepage</h1>")
def about_view(request):
    return HttpResponse("<h1>This is our About Us page</h1>")
def contact_view(request):
    return HttpResponse("<h1>This is our Contact Us page</h1>")
def faq_view(request):
    return HttpResponse("<h1>This is our FAQ page</h1>")
def term_view(request):
    return HttpResponse("<h1>This is our Terms & Conditions page</h1>")
