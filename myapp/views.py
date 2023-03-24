from .models import Drink, User, Food
from .serializers import DrinkSerializer, UserSerializer, FoodSerializer
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# class UserAuthToken(ObtainAuthToken):

#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'id': user.pk,
#             'username': user.email
#         })

@api_view(['POST']) # only accepts post
def sign_up(request):
    # post required fields - email, password
    # create user
    try:
        User.objects.create_user(username= request.data['email'], password=request.data['password'], email=request.data['email']) # all models have create method; create_user from AbstractUser, hashes password
        # also login
        user = authenticate(username=request.data['email'], password=request.data['password'])
        print(request._request)
        try:
            login(request._request, user)
            return JsonResponse({
                'token': user.auth_token.key,
                'id': user.pk,
                'username': user.email
            })
        except Exception as e:
            print(str(e))
            return JsonResponse({'success':'False', 'reason': 'cannot login'})

    except Exception as e:
        print(str(e))
        return JsonResponse({'success':'False', 'reason':'cannot create'})

@api_view(['POST'])
def log_in(request):
    print('login')
    print(request.data)
    # authenticate check valid user
    user = authenticate(username=request.data['email'], password=request.data['password'])
    if user is not None:
        if user.is_active:
            try:
                login(request._request, user)
                token = Token.objects.get(user=user)
                return JsonResponse({
                    'token': token.key,
                    'id': user.pk,
                    'username': user.email
                })
            except Exception as e:
                print(str(e))
                return JsonResponse({'success': False, 'reason': 'login failed'})
        else:
            return JsonResponse({'success': False, 'reason': 'user is not active'})
    else:
        return JsonResponse({'success': False, 'reason': 'user does not exist'})


@api_view(['POST'])
def log_out(request):
    try:
        logout(request)
        return JsonResponse({'success': True})
    except:
        return JsonResponse({'success': False, 'reason': 'logout failed'})

@api_view(['POST'])
def who_am_i(request):
    print(request.user)
    if request.user.is_authenticated:
        return JsonResponse({
                        'token': request.user.auth_token.key,
                        'id': request.user.pk,
                        'username': request.user.email
                    })
    return JsonResponse({'success': False}) 




# class UserLogIn(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         print(request.data)
#         serializer = self.serializer_class(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token = Token.objects.get(user=user)
#         return Response({
#             'token': token.key,
#             'id': user.pk,
#             'username': user.username
#         })