from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa, Escolha
from .models import Rodadas, Dezenas, Config
from .forms import PessoaForm, EscolhaForm
from .forms import RodadasForm, DezenasForm
from django.forms.models import inlineformset_factory
from django.db.models import Count, Max 
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required()
def viewPendencias(request):
    pessoa = Pessoa.objects.filter(pagamento=False)
    context = {
        'pessoa':pessoa,
    }
    return render(request, 'pendentes.html', context)

@login_required()
def viewHome(request):
    teste = Config.objects.first()
    if teste != None:
        valor_jogada=teste.valor_jogada
        porcent_maior=teste.v_max_ponto
        porcent_menor=teste.v_min_ponto
    else:
        valor_jogada=0
        porcent_maior=0
        porcent_menor=0

    
    jogos_pago = Pessoa.objects.filter(pagamento=True).count() * valor_jogada 
    # maior = Escolha.objects.all().aggregate(Max('acertos'))['acertos__max']
    pd = Pessoa.objects.filter(pagamento=False).count()
    total_jogador = Pessoa.objects.all().count()
    jogos_a_pagar = Pessoa.objects.filter(pagamento=False).count()
    premio_maior = jogos_pago*porcent_maior/100
    premio_menor = jogos_pago*porcent_menor/100
    meu_premio = jogos_pago - premio_maior - premio_menor   
    maiorais = Pessoa.objects.all().order_by('-acertos') 
    
    context = {
        'maiorais': maiorais,
        'meu_premio':meu_premio,
        'premio_menor':premio_menor,
        'premio_maior':premio_maior,
        'porcent_maior':porcent_maior,
        'porcent_menor':porcent_menor,
        'valor_jogada':valor_jogada,
        'pd':pd,
        'jogos_pago': jogos_pago,
        'jogos_a_pagar':jogos_a_pagar,
        'total_jogador': total_jogador,
    }
    return render(request, "dashboard.html", context)

@login_required()
def DeleteConfig(request):
    config = Config.objects.all()
    config.delete()
    return redirect('core:configuracoes')

@login_required()
def teste(self):
    var = Escolha.objects.all()
    # print(var)
    return redirect('/listagem/')

@login_required()
def viewLista(request):
    
    search = request.GET.get('search')
    if search:
        pessoa = Pessoa.objects.filter(nome__icontains=search)
    else:
        pessoa = Pessoa.objects.order_by('-data_cadastro')
    lista = 0
    context = {
            'lista': lista,
            'pessoa': pessoa,
            }
    
    return render(request, 'lista.html', context)

@login_required()
def viewDelete(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    pessoa.delete()
    return redirect('/listagem/')

@login_required()
def DeleteAll(request):
    pessoa = Pessoa.objects.filter(repeticao=False)
    pessoa.delete()
    return redirect('/listagem/')

@login_required()
def DeleteAllRodada(request):
    pessoa = Rodadas.objects.all()
    pessoa.delete()
    return redirect('../')

@login_required()    
def exluirRodada(request, id):
    rodada = get_object_or_404(Rodadas, pk=id)
    rodada.delete()
    return redirect('../../')


@login_required()
def jogadorPago(request, id):
    pessoa = get_object_or_404(Pessoa, pk=id)
    pessoa.pagamento = True
    pessoa.save()
    return redirect('../../')

@login_required()
def RodadaCadastro(request):
    objects = Rodadas.objects.all()
    if request.method == 'GET':
        form = RodadasForm()
        form_dezenas_factory = inlineformset_factory(Rodadas, Dezenas, form=DezenasForm, extra=10)
        form_dezenas = form_dezenas_factory()
        context = {
            'objects':objects,
            'form': form,
            'form_dezenas':form_dezenas,
        }
        return render(request, 'rodadas.html', context)


    if request.method == 'POST':
        objects = Rodadas.objects.all()
        escolha = Escolha.objects.all()
        form = RodadasForm(request.POST)
        form_dezenas_factory = inlineformset_factory(Rodadas, Dezenas, form=DezenasForm)
        form_dezenas = form_dezenas_factory(request.POST)

        if form.is_valid() and form_dezenas.is_valid():
            rodadas = form.save(commit=False)
            rodadas.save()
            
            form_dezenas.instance = rodadas
            dezenas = form_dezenas.save(commit=False)
            for var in dezenas:
                for esc in escolha:
                    if var.dezena == esc.numeros:
                        esc.acertos = esc.numeros
                        esc.save()
            form_dezenas.save()
            return redirect ('../rodadas')
    
    else:
        context = {
            'objects': objects,
            'form': form,
            'form_dezenas':form_dezenas,
        }
        return render(request, 'cadastro.html', context)    

@login_required()
def viewCadastro(request):
    pessoa = Pessoa.objects.all()
    last = Pessoa.objects.last()
    if request.method == 'GET':
        form = PessoaForm()
        form_numeros_factory = inlineformset_factory(Pessoa, Escolha, form=EscolhaForm, extra=10)
        form_numeros = form_numeros_factory()

        context = {
            'pessoa': pessoa,
            'form': form,
            'last': last,
            'form_numeros':form_numeros,
        }
        return render(request, 'cadastro.html', context)
    if request.method == 'POST':
        valor_jog = Config.objects.last()
        last = Pessoa.objects.last()
        form = PessoaForm(request.POST)
        form_numeros_factory = inlineformset_factory(Pessoa, Escolha, form=EscolhaForm)
        form_numeros = form_numeros_factory(request.POST)

        if form.is_valid() and form_numeros.is_valid():
            pessoa = form.save()
            pessoa.save()
            
            form_numeros.instance = pessoa 
            # print('==========================')
            # print(len(Escolha.objects.filter(sorteado=True)h) + 20)
            # print('==========================')       
            form_numeros.save()

            
            return redirect('../cadastro')
    
    else:
        context = {
            'last': last,
            'form': form,
            'form_numeros':form_numeros,
        }
        return render(request, 'cadastro.html', context)

class CreateConfig(LoginRequiredMixin ,CreateView):
    login_url = reverse_lazy('authenticate:login')
    model = Config
    fields = ['v_max_ponto', 'v_min_ponto', 'valor_jogada']
    template_name = 'configuracoes.html'
    success_url = reverse_lazy('core:home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['configuracao'] = Config.objects.all()
        return context
    
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

@login_required()
def reiniciar_config(request):
    config = Config.objects.all()
    config.delete()
    return redirect('core:configuracoes')

