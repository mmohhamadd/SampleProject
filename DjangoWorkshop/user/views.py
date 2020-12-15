from user.serializers import UserListSerializer,UpdateProfileSerializer,AddUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login 
from rest_framework import status
from django.contrib.auth.models import User

class UserLoginView(APIView):
    authentication_classes = []
    def post(self,request):
        user = authenticate(
            username=request.data['username'],
            password=request.data['password']
        ) 
        if user:
            login(request,user)
            return Response({
                "message": "logged in"
                }
            )
        else:
            return Response({
                "message": "wrong input"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        

class UserSignupView(APIView):
    def post(self,request):
        u = AddUserSerializer(
            data=request.POST
        )
        if u.is_valid():
            u.save()
            user = User.objects.get(
                username=request.POST['username']
            )
            login(request,user)
            return Response({
                "message": "welcome!"
                }
            )
        else:
            return Response(
                u.errors,
                status=status.HTTP_400_BAD_REQUEST
            )



class ProfileView(APIView):
    def get(self,request):
        if request.user.is_authenticated is False:
            return Response(
                {
                    "message": "You should login first"
                })
        users = User.objects.all()
        a = UserListSerializer(users,many=True)
        return Response(a.data)
        
    def put(self,request):
        if request.user.is_authenticated is False:
            return Response(
                {
                    "message": "You should login first"
                })    
        data = request.data.copy()        
        if(request.data.get('username') is None):
            data.update({'username':request.user.username})
        
        if(request.data.get('password') is None):
            Updating_password = False
            data.update({'password':request.user.password})
        else:
            Updating_password = True
        
        p = UpdateProfileSerializer(
            data=data,
            instance=request.user,
            context={
                'Updating_password': Updating_password
            })

        if p.is_valid():
            p.save()
            login(request,request.user)
            return Response(
                {
                    "message": "Your Profile updated successfully"
                }
        )
        else:
            return Response(
                {
                    "errors": p.errors
                }
            )    


