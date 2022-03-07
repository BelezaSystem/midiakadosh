from django.views.generic import FormView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Funcionario, Servico
from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('core:index')

    # sobreescrevendo o método de obtenção do contexto
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['servicos'] = Servico.objects.order_by('?').all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request,'E-mail enviado com sucesso!!!')
        return super(IndexView, self).form_valid(form, *args, *kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o E-mail.')
        return super(IndexView, self).form_invalid(form, *args, *kwargs)


class DetalharServicoView(DetailView):
    template_name = 'detalhe_servico.html'
    model = Servico
