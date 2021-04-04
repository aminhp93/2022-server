from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import SoftDeletableModel, TimeStampedModel


class Post(TimeStampedModel):
    content = models.TextField(_('content'), blank=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = _('post')
        verbose_name_plural = _('posts')
    
    def __str__(self):
        return self.id
