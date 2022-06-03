from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.

def User(request):
    if request.method == 'POST':
        user = Users()
        user.name = request.POST['name']

        if(request.POST.get('man')=='on'):
            user.gender = 'M'
        else:
            user.gender = 'W'

        user.email = request.POST['email']
        user.password = request.POST['password']
        user.save()
        # print(user.name,'\n')

        return redirect('user')
    else:
        user = Users.objects.all()
        return render(request, 'community/index.html', {'user':user})
#
# def Input(request):
#     if request.method == 'POST':
#         input = Input()
#         input.startperiod = request.POST['startperiod']
#
#     else:
#         input = Input.objects.all()
#         return render(request, 'community/input.html', {'input':input})

