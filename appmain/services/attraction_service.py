# ---------------------------------------------------------------------------
#                    L e B o n P l a n T e x a s   ( 2 0 2 4 )
# ---------------------------------------------------------------------------
# File   : appmain/services/customer_service.py
# Author : Morice
# ---------------------------------------------------------------------------


def upload_to_file_for_image(instance, filename):
    if instance.file and instance.file.file_name:
        return f"best_of_cities/{instance.file.file_name}/{filename}"
    return f"best_of_cities/unknown/{filename}"
