import math
from rest_framework import serializers
from .models import *

class FromSerializer(serializers.ModelSerializer):
    class Meta:
        model=StackFusion
        fields='__all__'

        def validate(self, data):
            if len(str(data['phone'])) !=10:
                raise serializers.ValidationError({'error': 'Phone Number Must be equal to 10 digits'})

            return data