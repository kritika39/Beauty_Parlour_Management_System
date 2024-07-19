from django.urls import path
from . import views
from account.views import logout_view



urlpatterns = [
   
    path('search_salons/', views.search_salons, name='search_salons'),
    path('salons/', views.salon_list, name='salon_list'),
    path('salons/<int:salon_id>/', views.salon_detail, name='salon_detail'),
    path('salons/<int:salon_id>/book/', views.book_appointment, name='book_appointment'),
    path('booking_history/', views.booking_history, name='booking_history'),
    path('notifications/', views.notifications, name='notifications'),
   path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.update_profile, name='update_profile'),
    path('logout/', logout_view, name='user_logout'),
]

