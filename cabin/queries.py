from .models import *
from django.db.models import Sum, Q, Exists, OuterRef, Count, F


def query_0():
    q = Driver.objects.all()
    return q


def query_1():
    q = Payment.objects.aggregate(income=Sum("amount"))
    return q


def query_2(x):
    q = Ride.objects.filter(id=x).aggregate(payment_sum=Sum("payment__amount"))
    return q


def query_3():
    drivers_with_class_a_cars = Car.objects.filter(car_type="A", owner=OuterRef("pk"))
    has_class_a_car = Exists(drivers_with_class_a_cars)
    q = (
        Driver.objects.annotate(has_class_a_car=has_class_a_car)
        .filter(has_class_a_car=True)
        .count()
    )
    return q


# not sure for this query!
def query_4():
    q = RideRequest.objects.filter(rider=None)
    return q


def query_5(t):
    q = Rider.objects.annotate(
        total_payment=Sum("riderequest__ride__payment__amount")
    ).filter(total_payment__gte=t)
    return q


def query_6():
    q = (
        Driver.objects.values("account__last_name")
        .annotate(car_amount=Count("car"))
        .order_by("-car_amount", "account__last_name")
    )
    return q


def query_7():
    cars = Car.objects.values_list("id", flat=True).filter(car_type="A")
    rides = Ride.objects.filter(car__in=cars).values_list("id", flat=True)
    q = (
        Rider.objects.filter(riderequest__ride__in=rides)
        .annotate(n=Count("riderequest__ride"))
        .values("n")
    )
    # q = Rider.objects.filter(riderequest__ride__car__car_type = 'B').annotate(n = Count('riderequest__ride'))
    return q


def query_8(x):
    q = Driver.objects.values("account__email").filter(car__car_type=x)
    return q


def query_9():
    q = Driver.objects.all().annotate(n=Count("car__ride"))
    return q


def query_10():
    q = (
        Driver.objects.annotate(n=Count("car__ride"))
        .order_by("account__first_name")
        .distinct()
        .values("n", "account__first_name")
    )
    return q


def query_11(n, c):
    q = Driver.objects.filter(car__color=c, car__model__gt=n)
    return q


def query_12(n, c):
    q = Driver.objects.filter(car__color=c).filter(car__model__gt=n).distinct()
    return q


def query_13(n, m):
    q = (
        Ride.objects.prefetch_related("car")
        .filter(
            car__owner__account__first_name=n, request__rider__account__first_name=m
        )
        .annotate(sum_duration=Sum(F("dropoff_time") - F("pickup_time")))
        .values("sum_duration")
    )
    return q


def query_14(x, y, r):
    q = "your query here"
    return q


def query_15(n, c):
    q = "your query here"
    return q


def query_16(x, t):
    q = "your query here"
    return q


def query_17():
    q = "your query here"
    return q


def query_18():
    q = "your query here"
    return q


def query_19(n, t):
    q = "your query here"
    return q


def query_20():
    q = "your query here"
    return q
