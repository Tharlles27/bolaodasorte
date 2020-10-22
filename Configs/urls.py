from django.urls import path
from .views import viewConfigs, render_pdf_view

app_name="teste"

urlpatterns = [
    path('', viewConfigs),
    path('gerado/', render_pdf_view, name="gerado")
]