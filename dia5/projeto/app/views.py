from django.shortcuts import render
from .models import EnderecoCep
from .forms import EnderecoCepForm
from django.views.generic import ListView, FormView, DeleteView, DetailView
from django.urls import reverse_lazy
import requests

# Create your views here.
def base(request):
    return render(request, 'base.html')

class EnderecoListView(ListView):
    model = EnderecoCep
    template_name = 'crud/enderecolist.html'
    context_object_name = "ceps"

class EnderecoFormView(FormView):
    template_name = 'crud/enderecoform.html'
    form_class = EnderecoCepForm
    success_url = reverse_lazy('listar_endereco')

    def form_valid(self, form):
        cep = form.cleaned_data['cep'].replace("-", "").strip()
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                cep_obj, created = EnderecoCep.objects.update_or_create(
                    cep=cep,
                    defaults={
                        "cep": data.get("cep"),
                        "rua": data.get("logradouro"),
                        "bairro": data.get("bairro"),
                        "cidade": data.get("localidade"),
                        "estado": data.get("uf"),
                    }
                )
            else:
                form.add_error("cep", "CEP não encontrado pela API do ViaCep.")
                return self.form_invalid(form)
        else:
            form.add_error("cep", "CEP consultado não encontrado!")
            
        return super().form_valid(form)


class EnderecoDeleteView(DeleteView):
    model = EnderecoCep
    template_name = 'crud/enderecodelete.html'
    success_url = reverse_lazy('listar_endereco')

class EnderecoDetailView(DetailView):
    model = EnderecoCep
    template_name = 'crud/enderecodetail.html'
    context_object_name = "cep"
