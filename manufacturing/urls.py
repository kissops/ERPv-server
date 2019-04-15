from django.urls import path
from django.views.generic import TemplateView
from .views import JobList

urlpatterns = [
    path(
        "dashboard/",
        TemplateView.as_view(template_name="manufacturing/index.html"),
        name="manufacturing_dashboard",
    ),
    path("jobs/", JobList.as_view(), name="job_list"),
]
