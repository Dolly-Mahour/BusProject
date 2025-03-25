# from ast import arg
from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
class post(TranslatableModel):
    translation = TranslatedFields(
        title = models.CharField(_('title'),max_length=255),
        content = models.TextField(_('content')),
    )
    def __str__(self):
        return self.title