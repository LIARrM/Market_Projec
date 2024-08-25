
from rest_framework.serializers import ModelSerializer
from .models import Store, Photo, CustomUser, CardProduct

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'



class StoreSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class PhotoSerializer(ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'





class ProductSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class CardProductSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CardProduct
        fields = '__all__'



# class  getMenuSerializer(ModelSerializer):
