

from django.shortcuts import render
from .models import Store, Photo, CustomUser, User,CardProduct
from .forms import UserForm, StoreForm, AvatarUpdateForm, CardProductForm
from .serializers import StoreSerializer, UserSerializer, PhotoSerializer,CardProductSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate, logout
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import  re
from django.contrib.auth.forms import PasswordChangeForm
from rest_framework import viewsets



@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return Response({'message': 'data added'})
        else:
                return Response({'errors': form.errors})



##
@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'})
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'})

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    request.user.auth_token.delete()
    logout(request)
    return Response({'msg': 'logout successfully'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    return Response({'user': UserSerializer(request.user).data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product(request):
    request.data['user'] = request.user
    if request.method =='POST':
        form = StoreForm(request.data, request.FILES)
        if form.is_valid():
            form.save()
            return  Response()
        else:
            return Response({'errors': form.errors})



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_UserPhoto(request):
    if request.method == 'POST':
        form = AvatarUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return Response({'msg': 'Avatar updated successfully'})
        else:
            return Response({'errors': form.errors})





@api_view(['GET'])
def getStore(request):
    data = Store.objects.all()
    return Response({'products': StoreSerializer(data, many=True).data})




@api_view(['GET'])
def getPhoto(request):
    data = Photo.objects.all()
    return Response({'Photo': PhotoSerializer(data, many =True).data})


@api_view(['GET'])
def getProductById(request,id):
    data = Store.objects.get(pk=id)
    return  Response({'product':StoreSerializer(data).data})



@api_view(['GET'])
def getMenu(request):
    categories = list(Store.objects.values_list('category', flat=True).distinct())
    return Response({'category': categories})


@api_view(['GET'])
def getMenuFilter(request,category):
    data = Store.objects.filter(category__istartswith= category)
    categories = StoreSerializer(data, many=True)
    return Response({'store': categories.data})



@api_view(['GET'])
def Search_Market(request, product_name):
    data = Store.objects.filter(product_name__istartswith=product_name)
    serializer = StoreSerializer(data, many = True)
    return Response({'store' : serializer.data})







@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_username(request):
    if request.method == "PUT":
        user = request.user
        username = request.data.get('username')

        if username is not None and username != '':
            user.username = username
            user.save()

            return Response({'message': 'user name updated successfully'})
        else:
            return Response({'error': 'user name cannot be empty'})



@api_view(['PUT'])
def change(request):
    try:
        user = CustomUser.objects.get(username=request.data['username'])  ## CustomUser view
    except:
        return Response({'errors': 'User not found'})
    form = PasswordChangeForm(user=user, data=request.data)
    if form.is_valid():
        form.save()
        return Response({'msg': 'ok'})
    else:
        return Response({'errors': form.errors})



@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_last_name(request):
    if request.method == "PUT":
        user = request.user
        last_name = request.data.get('last_name')

        if last_name is not None and last_name != '':
            user.last_name = last_name
            user.save()

            return Response({'message': 'Last name updated successfully'})
        else:
            return Response({'error': 'Last name cannot be empty'})

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_first_name(request):
    if request.method == "PUT":
        user = request.user
        first_name = request.data.get('first_name')

        if first_name is not None and first_name != '':
            user.first_name = first_name
            user.save()

            return Response({'message': 'First name updated successfully'})
        else:
            return Response({'error': 'First name cannot be empty'})




@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_email(request):
    if request.method == "PUT":
        user = request.user
        email = request.data.get('email')

        if email is not None and email != '' and re.match(r'^[\w\.-]+@[\w\.-]+$', email):
            user.email = email
            user.save()

            return Response({'message': 'Email updated successfully'})
        else:
            return Response({'error': 'Invalid email format or email cannot be empty'})




@api_view(['POST'])
def add_Cardproduct(request):
    print('Received data:', request.data)
    if request.method == 'POST':
        form = CardProductForm(request.data)
        if form.is_valid():
            form.save()
            return Response({'msg': 'CardProduct added'})
        else:
            return Response({'errors': form.errors})



@api_view(['GET'])
def getCard(request):
    data = CardProduct.objects.all()
    return Response({'CardProduct': CardProductSerializer(data, many=True).data})


@api_view(['DELETE'])
def del_Card(request,id):
    try:
        Card = CardProduct.objects.get(product_id=id)
        Card.delete()
        return Response({'message': 'Card Product delete successfuly'})
    except Card.DoesNotExist:
        return Response({'error': 'Card Product Not Found'})
