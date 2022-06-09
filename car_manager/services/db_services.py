from car_manager.models import Car


def get_all_car_obj_from_db():
    return Car.objects.all()
