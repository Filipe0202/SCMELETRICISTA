from django.contrib import admin
from .models import Produto, Vendedor, Orcamento

admin.site.register(Produto)
admin.site.register(Vendedor)
admin.site.register(Orcamento)