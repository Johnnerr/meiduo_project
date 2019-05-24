from django.shortcuts import render

# Create your views here.
from django.views import View


# 1. 注册页面 功能
class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
