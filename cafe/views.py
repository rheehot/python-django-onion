from django.http import HttpResponse

from cafe.application_service import order_coffee_service, order_service


def order_coffee(request, cafe_id, customer_id):
    order_coffee_service.order_coffee(cafe_id, customer_id)
    return HttpResponse(status=200)


def get_order(request):
    order = order_service.get_order(order_id=1)
    return HttpResponse(status=200)
