
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from .models  import Product
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['username'] = user.username
        # ...
 
        return token
 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
def register(request):
    user = User.objects.create_user(
                username=request.data['username'],
                email=request.data['email'],
                password=request.data['password']
            )
    user.is_active = True
    user.is_staff = True
    user.save()
    return Response("new user born")

 
def index(req):
    return JsonResponse('hello', safe=False)

@api_view(['GET','POST'])
def products(request):
    print(request)
    tempAr=[]
    for pro in Product.objects.all():
        tempAr.append({"price":pro.price,"desc":pro.desc,"id":pro.id})
    return Response(tempAr)

