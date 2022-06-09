from car.models import Car


def get_all_car_obj_from_db() -> "QuerrySet":
    return Car.objects.all()


def get_car_obj_filter_by_id(id) -> "QuerrySet":
    return Car.objects.filter(id=id)
