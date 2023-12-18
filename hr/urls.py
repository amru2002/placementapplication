from django.urls import path

from hr import views

urlpatterns=[
    path("",views.SignInView.as_view(),name="signin"),
    path("index",views.DashboardView.as_view(),name="index"),
    path("signout",views.SignoutView.as_view(),name="signout"),
    path("category",views.CategoryListCreateView.as_view(),name="category"),
    path("category/<int:pk>/remove",views.CategoryDeleteView.as_view(),name="category-delete"),
    path("job-add",views.JobsCreateView.as_view(),name="job-add"),
    path("jobs/all",views.JoblistView.as_view(),name="job-list"),
    path("jobs/<int:pk>/remove",views.JobDeleteView.as_view(),name="job-delete"),
    path("jobs/<int:pk>/change",views.JobUpdateView.as_view(),name="job-edit")
]