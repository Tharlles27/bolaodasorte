from django.contrib import admin
from .models import Pessoa, Escolha
from .models import Rodadas, Dezenas
from .models import Config, Acertos


admin.site.register(Pessoa)
admin.site.register(Escolha)

admin.site.register(Rodadas)
admin.site.register(Dezenas)


admin.site.register(Config)
admin.site.register(Acertos)

# Register your models here.
