from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.Base.as_view(), name='home'),
    path('crear/', views.CrearNoticia.as_view(), name='crear_noticia'),
    path('listar/', views.ListarNoticias.as_view(), name='listar_noticias'),
    path('Home/',views.Base.as_view(), name='Home'),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('registro/', views.registro_usuario, name='registro'),

    path('succesempleado/',views.Success.as_view(), name='proceso_correcto'),

    path('updatenoticia/<pk>', views.UpdateNoticia.as_view(),name='update'),
    path('deletenoticia/<pk>', views.DeleteNoticia.as_view(),name='delete'),

    path('mis_noticias_editar/', views.EditarMisNoticias.as_view(), name='editar_mis_noticias'),
    path('mis_noticias_eliminar/', views.EliminarMisNoticias.as_view(), name='eliminar_mis_noticias'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




