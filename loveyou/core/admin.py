from django.contrib import admin

from .models import Relacionamento


class RelacionamentoAdmin(admin.ModelAdmin):
    list_display = ("description", "done")


admin.site.register(Relacionamento, RelacionamentoAdmin)
