from django.shortcuts import render
from core.models import *
import os
from datetime import date, datetime
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders



def viewConfigs(request):
    return render(request, "visuConfig.html")


def render_pdf_view(request):
    hoje = date.today()
    dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
    hj = dias[hoje.weekday()]
    hora_agora = datetime.now()
    hora = hora_agora.strftime('%H:%M')
    acertivos = Escolha.objects.filter(sorteado=True).count()
    pessoa = Pessoa.objects.all()

    template_path = 'pdf_template/invoice.html'
    context = {
        'hj':hj,
        'hora':hora,
        'hoje':hoje,
        'pessoa': pessoa,
        'acertivos':acertivos,
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response )
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response