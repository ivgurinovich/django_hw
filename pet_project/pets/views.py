from django.shortcuts import render
from pets.models import Dog

def index(request):
    test_pet = Dog.objects.get(id=1)
    return render(request, 'index.html',
                  context={'dog': test_pet})
