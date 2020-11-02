from django.http import HttpResponse


def order_coffee(request):
    return HttpResponse(status=200)
