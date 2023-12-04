from django.urls import path

from hr import views

urlpatterns=[
    path("signin",views.SignInView.as_view(),name="login")
]