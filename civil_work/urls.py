from django.urls import path
from . import views
app_name ='civil_work'
urlpatterns = [
    path('',views.home,name='home'),
    path('service-1',views.service_one,name='service1'),
    path('service-1-result',views.service_one_result,name='service_one_result'),
    path('service-2',views.service_two,name='service2'),
    path('service-2-result',views.service_two_result,name='service_two_result'),
    path('registration',views.registration,name='registration'),
    path('login',views.login_request,name='login_request'),
    path("logout",views.log_out,name='log_out')
]
