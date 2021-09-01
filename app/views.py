from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings

from .forms import ContatoForm
from .models import Projeto, Foto

def send_email(subject, message):
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, [settings.EMAIL_PESSOAL], fail_silently=True)
        except BadHeaderError:
            return HttpResponse('Bad Header Error.')

class ProjetoListView(ListView):
    model = Projeto
    context_object_name = 'projetos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fotos'] = []
        context['form'] = ContatoForm()
        for p in Projeto.objects.all():
            foto = Foto.objects.filter(projeto=p.id).first()
            if foto:    
                context['fotos'].append(foto)
        return context

    #post method
    def post(self, request, *args, **kwargs):
        form = ContatoForm(request.POST)
        if form.is_valid():
            send_email(form['titulo'].value(), form['corpo'].value())

        fotos = []
        for p in Projeto.objects.all():
            foto = Foto.objects.filter(projeto=p.id).first()
            if foto:    
                fotos.append(foto)
        return render(request, 'app/projeto_list.html', {'projetos':Projeto.objects.all(), 'fotos':fotos, 'form':ContatoForm()})

class ProjetoDetailView(DetailView):
    model = Projeto
    context_object_name = 'projeto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fotos'] = Foto.objects.filter(projeto=self.get_object().id)
        context['form'] = ContatoForm()
        return context

    #post method
    def post(self, request, *args, **kwargs):
        form = ContatoForm(request.POST)
        if form.is_valid():
            send_email(form['titulo'].value(), form['corpo'].value())

        fotos = Foto.objects.filter(projeto=self.get_object().id)
        return render(request, 'app/projeto_detail.html', {'projeto':Projeto.objects.get(id=self.get_object().id), 'fotos':fotos, 'form':ContatoForm()})