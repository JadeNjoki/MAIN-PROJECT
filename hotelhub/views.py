from django.shortcuts import render
from .models import Service, Room, Team, Testimonial, About


def index(request):
    services = Service.objects.all()
    rooms = Room.objects.all()[:3]  # Show 3 featured rooms
    testimonials = Testimonial.objects.all()
    team = Team.objects.all()
    return render(request, 'index.html', {
        'services': services,
        'rooms': rooms,
        'testimonials': testimonials,
        'team': team,
    })

def about(request):
    about = About.objects.all()
    return render(request, 'about.html', {'about': about})

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def rooms(request):
    rooms = Room.objects.all()
    return render(request, 'rooms.html', {'rooms': rooms})

def team(request):
    team = Team.objects.all()
    return render(request, 'team.html', {'team': team})

def testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonials.html', {'testimonials': testimonials})

def contact(request):
    if request.method == 'POST':
        # Save contact message
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        'ContactMessage'.objects.create(name=name, email=email, subject=subject, message=message)
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')

def booking(request):
    if request.method == 'POST':
        # Save booking details
        room_id = request.POST['room_id']
        guest_name = request.POST['guest_name']
        email = request.POST['email']
        check_in_date = request.POST['check_in_date']
        check_out_date = request.POST['check_out_date']
        message = request.POST['message']
        room = Room.objects.get(id=room_id)
        'Booking'.objects.create(
            room=room, guest_name=guest_name, email=email,
            check_in_date=check_in_date, check_out_date=check_out_date, message=message
        )
        return render(request, 'booking.html', {'success': True})
    rooms = Room.objects.all()
    return render(request, 'booking.html', {'rooms': rooms})


def room_view(request):
    rooms = [
        {'name': 'Deluxe Room', 'rating': 3},
        {'name': 'Executive Suite', 'rating': 5},
    ]

    for room in rooms:
        room['filled_stars'] = range(room['rating'])  # Range for filled stars
        room['empty_stars'] = range(5 - room['rating'])  # Range for empty stars

    context = {'rooms': rooms}
    return render(request, 'your_template.html', context)



def slider_view(request):
    sliders = Sliders.objects.all()  # Fetch all Slider objects
    return render(request, 'slider.html', {'sliders': sliders})






