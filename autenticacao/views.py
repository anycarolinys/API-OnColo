# from rest_framework import viewsets
# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from rest_framework.authtoken.models import Token
# from django.contrib.auth import authenticate, login

# class LoginViewSet(viewsets.ViewSet):
    
#     def create(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')
        
#         user = authenticate(request, email=email, password=password)
        
#         login(request, user)
#         return redirect('/fisioterapeuta/')