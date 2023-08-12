from django.urls import path
from app_pricing import views

urlpatterns = [
    path('', views.consulta_veiculo, name='consulta-veiculo'),  # Defina a página de consulta como a primeira
    path('consultar-valor-veiculo/', views.consultar_valor_veiculo, name='consultar-valor-veiculo'),
    path('mostrar-valor/', views.mostrar_valor, name='mostrar-valor'),
    path('processar-prazo/', views.processar_prazo, name='processar-prazo'),

]





