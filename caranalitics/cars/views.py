from django.shortcuts import render, redirect, get_object_or_404
from .forms import CarForm
from .models import Car
# Create your views here.

# Create your views here.
def index(request):
    return render(request, 'cars/index.html')

def create_car(request):
    if request.method == "POST":
        form = CarForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = CarForm()

    return render(
        request, 'cars/create.html',{
        "form": form
        })

def car_list(request):
    cars = Car.objects.all()

    return render(
        request, 'cars/list.html',{
            "cars": cars
        }
    )

def update_car(request, id):
    car = get_object_or_404(Car, id=id)

    if request.method == "POST":
        form = CarForm(request.POST, instance=car)

        if form.is_valid():
            form.save()
            return redirect("car_list")

    else:
        form = CarForm(instance=car)

    return render(
        request, 'cars/update.html',{
            "form": form
        
        })

def delete_car(request, id):
    car = get_object_or_404(Car, id=id)
    car.delete()

    return redirect('list')

def detail_car(request, id):
    car = Car.objects.get(id=id)
    return render(request, 'cars/detail.html',{
        "car": car
    })