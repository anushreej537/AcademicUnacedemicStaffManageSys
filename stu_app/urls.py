# from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('registration/',views.registration),
    path('login/',views.login),
    path('signup/',views.signup),
    path('',views.base),
    path('academic_dashboard/',views.academic_dashboard),
    path('nonacademic/',views.nonacademic),
    path('student/',views.student),
    path('login_user/',views.login_user),
    path('home/<int:user_id>/',views.home,name='home'),
    path('logout/',views.logout)
]