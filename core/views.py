from django.views.generic import FormView, DetailView, ListView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Funcionario, Servico, EventosDias, Eventos
from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('core:index')

    # sobreescrevendo o método de obtenção do contexto
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['servicos'] = Servico.objects.all()
        context['eventos'] = Eventos.objects.all()

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!!!')
        return super(IndexView, self).form_valid(form, *args, *kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o E-mail.')
        return super(IndexView, self).form_invalid(form, *args, *kwargs)


class DetalharServicoView(DetailView):
    template_name = 'detalhe_servico.html'
    model = Eventos

    def get_context_data(self, **kwargs):
        #Pega o contexto da página
        context = super(DetailView, self).get_context_data(**kwargs)
        context['eventosdias'] = EventosDias.ativosG.filter(evento=kwargs.get('object').id)
        return context
