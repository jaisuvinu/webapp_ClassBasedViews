from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView, ListView

from myapp1.models import Patient


class View1(View):
    def get(self,request):
        return HttpResponse('<h1>Welcome to CBV1</h1>')


class View2(TemplateView):
    template_name='sample.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='Anitha '
        context['age']= 30
        context['city']=' Tuty'
        return context


class ShowAllPatients(ListView):
    model = Patient
    template_name = 'showallpatients.html'  # Patient_list == Patient.objects.all()