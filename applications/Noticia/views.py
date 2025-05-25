
from django.shortcuts import render, redirect
from django.views.generic import ( 
    ListView,
      CreateView,
        UpdateView,
            DeleteView,
                TemplateView,
    )
from django.urls import reverse_lazy
from .models import Noticia
from .forms import NoticiaForm

from django.contrib.auth.models import User
from django.contrib.auth import login
from django import forms

from django.contrib.auth.mixins import LoginRequiredMixin





class CrearNoticia(LoginRequiredMixin, CreateView):
    model = Noticia
    form_class = NoticiaForm
    template_name = 'noticia/crear_noticia.html'
    success_url = reverse_lazy('listar_noticias')

    def form_valid(self, form):
        form.instance.autor = self.request.user  
        return super().form_valid(form)


from django.views.generic import ListView

class Base(CreateView):
    form_class = NoticiaForm
    model = Noticia
    template_name = 'noticia/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noticias'] = Noticia.objects.order_by('-Fecha_Publicacion')[:3]  
        return context

    


class ListarNoticias(ListView):
    model = Noticia
    template_name = 'noticia/listar_noticias.html'
    context_object_name = 'noticias'
    queryset = Noticia.objects.all().order_by('-Fecha_Publicacion')  

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password']) 
            user.save()
            login(request, user)  
            return redirect('/')  
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})



class UpdateNoticia(LoginRequiredMixin, UpdateView):
    model = Noticia
    template_name = 'noticia/update_noticia.html'
    fields = 'Titulo','Parrafo','Fecha_Publicacion','imagen'
    success_url = reverse_lazy('proceso_correcto')
    

    def get_queryset(self):
        return Noticia.objects.filter(autor=self.request.user)


class DeleteNoticia(LoginRequiredMixin, DeleteView):
    model = Noticia
    template_name = "noticia/delete_noticia.html"
    success_url = reverse_lazy('proceso_correcto')

    def get_queryset(self):
        return Noticia.objects.filter(autor=self.request.user)

    

class Success(TemplateView):
    template_name = "noticia/success.html"


class EditarMisNoticias(ListView):
    model = Noticia
    template_name = 'noticia/editar_mis_noticias.html'
    
    def get_queryset(self):
        return Noticia.objects.filter(autor=self.request.user)

class EliminarMisNoticias(ListView):
    model = Noticia
    template_name = 'noticia/eliminar_mis_noticias.html'
    
    def get_queryset(self):
        return Noticia.objects.filter(autor=self.request.user)