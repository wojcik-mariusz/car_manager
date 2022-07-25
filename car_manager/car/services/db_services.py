from car.models import Car


def get_all_car_obj_from_db() -> "QuerrySet":
    """Get all cars saved from db.
        :return: Queryset of all cars saved from db.
        :rtype: QuerySet
    """
    return Car.objects.all()


def get_car_obj_filter_by_id(id) -> "QuerrySet":
    """Get car saved from db, filter by id.
        :return: Queryset of car saved from db.
        :rtype: QuerySet
    """
    return Car.objects.filter(id=id)
