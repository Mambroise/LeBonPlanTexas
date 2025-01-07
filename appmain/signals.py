# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/signals.py
# Author : Morice
# ---------------------------------------------------------------------------


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from .models import Invoice

@receiver(post_save, sender=Invoice)
def set_invoice_number(sender, instance, created, **kwargs):
    if created and not instance.invoice_number:
        today_str = now().strftime('%Y%m%d')
        instance.invoice_number = f"{instance.pk}{instance.customer.id}{today_str}"
        instance.save()

