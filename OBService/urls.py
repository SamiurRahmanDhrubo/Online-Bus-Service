"""OBService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import home.views as h
import passenger.views as pa
import company.views as co
import admin.views as ad
urlpatterns = [
    path('admin/', admin.site.urls),
    path('landing/',h.landing_view ),
    path('signupop/',h.signupop_view ),
    path('signuppassenger/',h.signuppassenger_view ),
    path('signupcompany/',h.signupcompany_view ),
    path('landing/',h.login_view ),
    path('signupop/',h.homec_view ),
    path('signuppassenger/',h.contact_view ),
    path('signupcompany/',h.about_view),
    path('faq/', h.faq_view),
    path('term/', h.term_view),

    path('adminpage/', ad.adminp_view),

    path('busshedule/', pa.busschdule_view),
    path('passenger/', pa.passenger_view),
    path('profile/', pa.passengerprofile_view),
    path('ticket/', pa.passengerpurticket_view),
    path('payment/', pa.payment_view),
    path('sunlight/',pa.sunlight_view ),
    path('track/',pa.track_view ),
    path('reserve/',pa.reserve_view ),

    path('company/',co.company_view ),
    path('cpro/',co.cpro_view ),
    path('registraton/',co.regi_view ),
]
