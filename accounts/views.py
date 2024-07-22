from django.shortcuts import render
from .serializers import SignUpSerializer, LoginSerializer
from rest_framework import generics, status 
from rest_framework.response import Response 
from rest_framework.request import Request 
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer 
    permission_classes = []

    def get(self, request: Request):
        return Response(
            {
            "message": "Sign Up Today!",
            "detail": "All information asked below are mandatory."
            }, status=status.HTTP_200_OK
        )
    #   return render(request, 'accounts/signup.html')

    def post(self, request: Request):
        data = request.data 
        serializer = self.serializer_class(data = data) 

        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "User Created Successfully!",
                "data": serializer.data
            }
            return Response(data = response, status = status.HTTP_201_CREATED)
        return Response(data = serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes = []

    def get(self, request: Request):
        return Response(
            {
            "user": str(request.user),
            "auth": str(request.auth)
            }, status=status.HTTP_200_OK
        )

    def post(self, request: Request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email = email, password = password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            response = {
                "message": "Login Successful!",
                "token": token.key
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Get the token from the request user
            token = Token.objects.get(user=request.user)
            # Delete the token
            token.delete()
            return Response({"message": "Logout successful!"}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"error": "Invalid token or user not logged in."}, status=status.HTTP_400_BAD_REQUEST)
