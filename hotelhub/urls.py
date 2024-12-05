from django.urls import path  # Import include to include your app's URLs


from hotelhub import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.about, name='services'),
    path('rooms/', views.about, name='rooms'),
    path('bookings/', views.about, name='bookings'),
    path('teams/', views.about, name='teams'),
    path('testimonial/', views.about, name='testimonial'),
    path('contact/', views.about, name='contact'),
    path('Slider/', views.about, name='slider-view'),



]