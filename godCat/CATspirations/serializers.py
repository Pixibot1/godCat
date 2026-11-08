from rest_framework import serializers
from .models import Theocat

class TheocatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theocat
        fields = '__all__'
    