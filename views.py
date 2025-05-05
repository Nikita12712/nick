from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .authentication import JWTAuthentication

def input_view(request):
    if request.method == "POST":
        request.session['user_input'] = request.POST.get('user_input', '')
        return redirect('output_view')
    return render(request, 'members_app/input.html')

def output_view(request):
    user_input = request.session.get('user_input', 'Немає даних')
    return render(request, 'members_app/output.html', {'user_input': user_input})

def session_view(request):
    count = request.session.get('count', 0)
    request.session['count'] = count + 1
    return render(request, 'members_app/session.html', {'count': count})


class ObtainTokenView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed("Невірні дані.")

        tokens = JWTAuthentication.generate_tokens(user)
        return Response(tokens)

class RefreshTokenView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            raise AuthenticationFailed("Рефреш токен обов'язковий.")

        tokens = JWTAuthentication.refresh_token(refresh_token)
        return Response(tokens)