from django.shortcuts import render
from .models import Tenants
from django.views.generic import DetailView,CreateView,DeleteView,UpdateView
from .forms import TenantCreateForm , TenantUpdateForm

# Create your views here.
def home(request):
    infos=Tenants.objects.all().order_by('-created_on')
    context={'infos':infos}
    return render(request,'delta/home.html',context)

class Detail(DetailView):
    model = Tenants


class Create(CreateView):
    model= Tenants
    form_class = TenantCreateForm
    success_url = "/"

class UpdateTenant(UpdateView):
    model= Tenants
    form_class =TenantUpdateForm
    template_name = 'delta/tenants_edit.html'

class Delete(DeleteView):
    model= Tenants
    success_url = "/"