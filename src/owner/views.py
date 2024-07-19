from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SalonForm, AppointmentForm
from .models import Salon, Appointment, Notification
from django.contrib import messages
from django.http import JsonResponse
from datetime import timedelta

@login_required
def owner_dashboard(request):
    salon = Salon.objects.filter(owner=request.user).first()
    appointments = Appointment.objects.filter(salon=salon) if salon else []
    notifications = Notification.objects.filter(user=request.user, is_read=False)  # Filter by user
    return render(request, 'owner_dashboard.html', {'salon': salon, 'appointments': appointments, 'notifications': notifications})



@login_required
def manage_salon(request):
    salon = Salon.objects.filter(owner=request.user).first()
    if request.method == 'POST':
        form = SalonForm(request.POST, request.FILES, instance=salon)
        if form.is_valid():
            salon = form.save(commit=False)
            salon.owner = request.user
            salon.save()
            return redirect('owner_dashboard')
    else:
        form = SalonForm(instance=salon)
    return render(request, 'owner/manage_salon.html', {'form': form})


@login_required#for appointments to be displayed in tabular form
def manage_appointments(request):
   
    owner = request.user
    salons = Salon.objects.filter(owner=owner)  # Get all salons owned by the logged-in user
    appointments = Appointment.objects.filter(salon__in=salons)
    return render(request, 'owner/manage_appointment.html', {'appointments': appointments})

@login_required
def notifications(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    return render(request, 'owner/notification.html', {'notifications': notifications})

@login_required
def mark_notification_as_read(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect('owner_dashboard')

@login_required
def calendar_view(request): # for calender
    return render(request, 'owner/calendar.html')

@login_required
def calendar_events(request):
    appointments = Appointment.objects.filter(salon__owner=request.user)
    events = []
    for appointment in appointments:
        events.append({
            'title': f'Appointment with {appointment.user.username}',
            'start': appointment.date.strftime('%Y-%m-%dT%H:%M:%S'),
            'end': (appointment.date + timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:%S'),  # Assuming 1-hour appointments
        })
    return JsonResponse(events, safe=False)


# def accept_appointment(request, appointment_id):
#     appointment = get_object_or_404(Appointment, id=appointment_id)
#     appointment.status = Appointment.ACCEPTED
#     appointment.save()
#     messages.success(request, 'Appointment accepted.')
#     return redirect('manage_appointment.html')  # Change 'manage_appointments' to the name of your appointments management view

# def reject_appointment(request, appointment_id):
#     appointment = get_object_or_404(Appointment, id=appointment_id)
#     appointment.status = Appointment.REJECTED
#     appointment.save()
#     messages.success(request, 'Appointment rejected.')
#     return redirect('manage_appointment.html') 

# def update_appointment_status(request, appointment_id, status):
#     appointment = get_object_or_404(Appointment, id=appointment_id)
#     appointment.status = status
#     appointment.save()
#     return redirect('manage_appointments')

def update_appointment_status(request, appointment_id, status):
    print(f"Update view called with appointment_id: {appointment_id} and status: {status}")  # Debugging statement
    appointment = get_object_or_404(Appointment, id=appointment_id)
    appointment.status = status
    appointment.save()
    print(f"Appointment {appointment_id} updated to status {status}")  # Debugging statement
    return redirect('manage_appointments') 