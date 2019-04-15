from django.views.generic import ListView, DetailView
from .models import Job


class JobList(ListView):
    model = Job
    paginate_by = 10
    queryset = Job.objects.filter(complete=False)
