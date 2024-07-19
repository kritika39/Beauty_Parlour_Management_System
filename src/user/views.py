# user/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from owner.models import Salon, Appointment, Notification
from .forms import AppointmentForm, ProfileUpdateForm
from django.contrib.auth.models import User


def search_salons(request):
    query = request.GET.get('query')
    salons = Salon.objects.filter(name__icontains=query) if query else Salon.objects.all()
    return render(request, 'user/search_salons.html', {'salons': salons})



salons = Salon.objects.all()
for salon in salons:
    print(salon.image)

def salon_list(request):
    salons = Salon.objects.all()
    query = request.GET.get('q')
    if query:
        salons = salons.filter(name__icontains=query)
    for salon in salons:
        print(f"Image URL: {salon.image.url}")  # Should print something like '/media/salon_images/Dark.png'
    return render(request, 'user/salon_list.html', {'salons': salons})

# def salon_list(request):
#     salons = Salon.objects.all()
#     return render(request, 'user/salon_list.html', {'salons': salons})

def salon_detail(request, salon_id):
    salon = get_object_or_404(Salon, pk=salon_id)
    return render(request, 'user/salon_detail.html', {'salon': salon})
from django.contrib import messages

def book_appointment(request, salon_id):
    salon = get_object_or_404(Salon, pk=salon_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.salon = salon
            appointment.save()
            messages.success(request, 'Appointment successfully made. Please wait for your appointment to be accepted.')
            return redirect('homepage')  # Redirect to home or any other page you prefer
        else:
            print(form.errors)
            messages.error(request, 'There was an error with your booking. Please try again.')
    else:
        form = AppointmentForm()
    return render(request, 'user/book_appointment.html', {'form': form, 'salon': salon})


@login_required
def booking_history(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'user/booking_history.html', {'appointments': appointments})


@login_required

def notifications(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False).order_by('-created_at')
    return render(request, 'user/notifications.html', {'notifications': notifications})




@login_required
def profile(request):
    user = User.objects.get(username=request.user)
    context = {"user": user}
    return render(request, "user/profile.html", context)


@login_required
def update_profile(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Profile update Successfully")
            return redirect("/user/profile")
        else:
            messages.add_message(request, messages.ERROR, "Failed to update profile")
            return render(request, "user/updateprofile.html", {"form": form})

    context = {"form": ProfileUpdateForm(instance=request.user)}

    return render(request, "user/updateprofile.html", context)
