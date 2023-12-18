from django.urls import path
from jobseeker import views

urlpatterns = [
   path("register/",views.SignupView.as_view(),name="signup"),
   path("index/",views.StudentindexView.as_view(),name="seeker-index"),
   path("profile",views.ProfileCreateView.as_view(),name="profile-add"),
   path("profile/<int:pk>/",views.ProfileDetailView.as_view(),name="profile-detail"),
   path("profile/<int:pk>/change",views.ProfileEditView.as_view(),name="profile-edit"),
   path("jobs/<int:pk>",views.JobDetailView.as_view(),name="job-detail")
]
