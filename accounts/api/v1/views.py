from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer, LoginSerializer, ChangePasswordSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def get(self, request):
        # Delete the JWT tokens from the client-side storage
        if 'access_token' in request.COOKIES:
            response = Response()
            response.delete_cookie('access_token')
        if 'refresh_token' in request.COOKIES:
            response = Response()
            response.delete_cookie('refresh_token')

        # Return a JSON response indicating that the user has been logged out
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)


class ChangePasswordView(GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)
    model = User

    def get_object(self):
        return self.request.user

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        self.object = self.get_object()

        if serializer.is_valid():
            if not self.object.check_password(serializer.data['old_password']):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            response = {
                'status': status.HTTP_200_OK,
                'message': 'Password updated successfully',
            }

            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
