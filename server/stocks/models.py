from django.db import models
from django.utils.translation import ugettext_lazy as _

from model_utils.models import SoftDeletableModel, TimeStampedModel


class Stock(TimeStampedModel):
    symbol              = models.CharField(_('symbol'), max_length=255, blank=True, unique=True, null=False)
    note                = models.TextField(_('note'), blank=True)
    buy_price           = models.CharField(_('buy_price'), max_length=255, blank=True, null=True)
    target_price        = models.CharField(_('target_price'), max_length=255, blank=True, null=True)
    support_price       = models.CharField(_('support_price'), max_length=255, blank=True, null=True)
    percent_target      = models.CharField(_('percent_target'), max_length=255, blank=True, null=True)
    percent_support     = models.CharField(_('percent_support'), max_length=255, blank=True, null=True)
    profit_loss_ratio   = models.CharField(_('profit_loss_ratio'), max_length=255, blank=True, null=True)
    is_high_liquidity   = models.BooleanField(_('is_high_liquidity'), default=False)
    is_good_character   = models.BooleanField(_('is_good_character'), default=False)
    est_buy_tich_san    = models.CharField(_('est_buy_tich_san'), max_length=255, blank=True, null=True)
    est_sell_tich_san   = models.CharField(_('est_sell_tich_san'), max_length=255, blank=True, null=True)
    is_blacklist        = models.BooleanField(_('is_blacklist'), default=False)

    class Meta:
        ordering = ('-id',)
        verbose_name = _('stock')
        verbose_name_plural = _('stocks')
    
    def __str__(self):
        return self.symbol
