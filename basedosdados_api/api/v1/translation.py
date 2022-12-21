from modeltranslation.translator import translator, TranslationOptions, register
from .models import Organization


@register(Organization)
class OrganizationsTranslationOptions(TranslationOptions):
    fields = ('name2',)
