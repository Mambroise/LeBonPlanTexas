# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/signals.py
# Author : Morice
# ---------------------------------------------------------------------------


import os
from django.db.models.signals import post_save
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.timezone import now
from django.conf import settings
from .models import Invoice,FileForImage,Attraction,CompanyInfo,Price

@receiver(post_save, sender=Invoice)
def calculate_invoice_totals(sender, instance, created, **kwargs):
    # Calcul des totaux seulement si une modification ou une création a eu lieu
    if created or any([
        instance.mobile_service,
        instance.driver_service,
        instance.platinum_service
    ]):
        # Récupération des données nécessaires depuis l'instance
        mobile_total = (instance.nbr_days_mobile or 0) * (instance.mobile_price_excl_tax or 0) if instance.mobile_service else 0
        driver_total = (instance.nbr_days_driver or 0) * (instance.driver_price_excl_tax or 0) if instance.driver_service else 0
        platinum_total = (instance.nbr_days_platinum or 0) * (instance.platinum_price_excl_tax or 0) if instance.platinum_service else 0

        # Calcul des totaux
        price = Price.objects.get(service_name='autonome')
        total_excl_tax = mobile_total + driver_total + platinum_total
        tax_rate = float(price.main_tax_info.strip('%')) / 100  # Convertir le taux TVA en décimal
        instance.total_excl_tax = total_excl_tax
        if instance.discount:
            discount_rate = float(instance.discount.rate.strip('%')) / 100
            instance.total_incl_discount = round(instance.total_excl_tax - (instance.total_excl_tax * discount_rate),2)
            tax_amount = round(instance.total_incl_discount * tax_rate, 2)
            total_incl_tax = instance.total_incl_discount + tax_amount
        else:
            tax_amount = round(total_excl_tax * tax_rate, 2)
            total_incl_tax = total_excl_tax + tax_amount

        instance.tax_rate = tax_rate
        instance.tax_amount = tax_amount
        instance.total = total_incl_tax


        # Sauvegarde pour appliquer les calculs
        Invoice.objects.filter(pk=instance.pk).update(
            total_excl_tax=total_excl_tax,
            tax_rate=tax_rate,
            tax_amount=tax_amount,
            total=total_incl_tax
        )

@receiver(post_save, sender=Invoice)
def set_invoice_number(sender, instance, created, **kwargs):
    if created and not instance.invoice_number:
        today_str = now().strftime('%Y%m%d')
        Invoice.objects.filter(pk=instance.pk).update(
            invoice_number=f"{instance.pk}{instance.customer.id}{today_str}"
        )

@receiver(post_save, sender=FileForImage)
def create_directory(sender, instance, created, **kwargs):
    if created:
        # Location where to create file
        directory_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'best_of_cities', instance.file_name)
        
        # Create file if not exists
        os.makedirs(directory_path, exist_ok=True)


@receiver(post_delete, sender=FileForImage)
def delete_directory(sender, instance, **kwargs):
    # Location where to delete file
    directory_path = os.path.join(settings.BASE_DIR, 'static', 'images', 'best_of_cities', instance.file_name)
    
    # delete file if exists
    if os.path.exists(directory_path):
        os.rmdir(directory_path) 

@receiver(post_delete, sender=Attraction)
def delete_attraction_image(sender, instance, **kwargs):
    """Supprime le fichier d'image associé à une Attraction lorsqu'elle est supprimée."""
    if instance.image_url and os.path.isfile(instance.image_url.path):
        try:
            os.remove(instance.image_url.path)  # Supprime le fichier
            # Supprime également le dossier si nécessaire
            folder_path = os.path.dirname(instance.image_url.path)
            if not os.listdir(folder_path):  # Vérifie si le dossier est vide
                os.rmdir(folder_path)
        except Exception as e:
            print(f"Erreur lors de la suppression du fichier ou dossier: {e}")
