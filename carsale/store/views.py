from django.shortcuts import render

# Create your views here.
def home(reques):
    test = "Hello Django!"
    return render(reques, 'store/index.html', {'test':test})