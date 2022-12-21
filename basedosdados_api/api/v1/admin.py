# -*- coding: utf-8 -*-
from django.contrib import admin

from basedosdados_api.api.v1.models import (
    Organization,
    Dataset,
    Table,
    BigQueryTypes,
    Column,
    CloudTable,
)


class OrganizationAdmin(admin.ModelAdmin):
    readonly_fields = ("slug2", "created_at", "updated_at")


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Dataset)
admin.site.register(Table)
admin.site.register(BigQueryTypes)
admin.site.register(Column)
admin.site.register(CloudTable)
