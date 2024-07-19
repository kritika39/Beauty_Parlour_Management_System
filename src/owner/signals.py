from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Appointment, Notification
from django.utils import timezone


#for notification signal 

@receiver(post_save, sender=Appointment)
def create_appointment_notification(sender, instance, created, **kwargs):
    if created:
        message = f"New appointment request from {instance.user.username} for {instance.date} at {instance.time}."
        Notification.objects.create(user=instance.salon.owner, message=message)

@receiver(post_save, sender=Appointment)
def appointment_status_changed(sender, instance, created, **kwargs):
    if not created:  # Only handle updates, not initial creation
        if instance.status in ['accepted', 'rejected']:
            notification_message = f"Your appointment has been {instance.status}."
            Notification.objects.create(
                user=instance.user,
                message=notification_message,
                created_at=timezone.now(),
                is_read=False
            )