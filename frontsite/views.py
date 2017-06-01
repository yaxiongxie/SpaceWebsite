from django.shortcuts import render


def test(request):
    context = {"nav_flag": 4}
    return render(request, 'frontsite/services.html', context)