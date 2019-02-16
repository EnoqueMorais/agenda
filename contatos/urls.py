from django.urls import path
from . import views

urlpatterns = [
    path ('',views.home),
    path('empresas/', views.empresa_list),
    path('empresas/<int:empresa_id>/', views.empresa_show),
    path('empresas/form/', views.empresa_form),
    path('empresas/<int:empresa_id>/edit/',views.empresa_edit),
    path('contato/', views.contato_show)
]