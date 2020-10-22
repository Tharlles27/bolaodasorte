from django.urls import path
from .views import viewHome, viewLista, viewCadastro, viewDelete, DeleteAll
from .views import RodadaCadastro, exluirRodada, DeleteAllRodada, CreateConfig
from .views import DeleteConfig, viewPendencias, teste, jogadorPago

app_name = "core"

urlpatterns = [
    path('', viewHome, name="home"),
    path('cadastro/', viewCadastro, name="cadastro"),

    path('listagem/', viewLista, name="lista"),
    path('listagem/del/<int:id>/', viewDelete, name="deletar"),
    path('listagem/deleteAll/', DeleteAll, name="deletar_tudo"),

    path('rodadas/', RodadaCadastro, name="rodada"),
    path('rodadas/deletar/<int:id>/', exluirRodada, name="exluirRodada"),
    path('rodadas/deletarRodadas/', DeleteAllRodada, name="deletarRodadas"),
    
    path('deleteConfig/', DeleteConfig, name="deletar-config"),
    path('definirConfig/', DeleteConfig, name="deletar-config"),
    path('pendencias/', viewPendencias, name="pendentes"),
    path('pagar/<int:id>/', jogadorPago, name="efetuar-pagamento"),

    path('config/', CreateConfig.as_view(), name="configuracoes"),
    path('testeModelo/', teste, name="testeModelo")

]