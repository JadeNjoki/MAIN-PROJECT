from django.urls import path  # Import include to include your app's URLs


from hotelhub import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('rooms/', views.rooms, name='rooms'),
    path('bookings/', views.booking, name='bookings'),
    path('teams/', views.team, name='teams'),
    path('testimonial/', views.testimonials, name='testimonial'),
    path('contact/', views.contact, name='contact'),
    path('Slider/', views.Slider, name='slider-view'),
    path('customers/', views.customers, name='customers'),
    path('layout/' , views.layout, name='layout'),


]