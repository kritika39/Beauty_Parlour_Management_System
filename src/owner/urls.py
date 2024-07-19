from django.urls import path
from . import views
from account.views import logout_view

urlpatterns = [
    path('owner_dashboard/', views.owner_dashboard, name='owner_dashboard'),
    path('logout/', logout_view, name='owner_logout'),
    path('manage_salon/', views.manage_salon, name='manage_salon'),
    path('manage_appointments/', views.manage_appointments, name='manage_appointments'),
     path('notifications/', views.notifications, name='notification'),
    path('mark_notification_as_read/<int:notification_id>/', views.mark_notification_as_read, name='mark_notification_as_read'),
    path('calendar/', views.calendar_view, name='calendar'),
    path('api/events/', views.calendar_events, name='calendar_events'),
    # path('appointment/accept/<int:appointment_id>/', views.accept_appointment, name='accept_appointment'),
    # path('appointment/reject/<int:appointment_id>/', views.reject_appointment, name='reject_appointment'),
    path('appointments/update/<int:appointment_id>/<str:status>/', views.update_appointment_status, name='update_appointment_status'),
]