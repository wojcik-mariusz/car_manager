from django.shortcuts import render


from car_manager.services.db_services import get_all_car_obj_from_db
# Create your views here.


def home(request):
    cars = get_all_car_obj_from_db()

    context = {
        "cars": cars
    }

    return render(request, 'home.html', context)


# TODO CRUD
def new_car(request):
    pass

