from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView

from .models import Funcionario, Servico


class IndexView(FormView):
    template_name = 'index.html'
    success_url = reverse_lazy('core:index')

    # sobreescrevendo o método de obtenção do contexto
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['servicos'] = Servico.objects.order_by('?').all()
        return context


class DetalharServicoView(DetailView):
    template_name = 'detalhe_servico.html'
    model = Servico
