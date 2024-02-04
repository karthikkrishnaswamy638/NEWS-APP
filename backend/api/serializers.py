from rest_framework import serializers
from . import models

class DateField(serializers.ReadOnlyField):
    def to_representation(self, value):
        return value.strftime('%Y-%m-%d')

class TimeField(serializers.ReadOnlyField):
    def to_representation(self, value):
        return value.strftime('%H:%M:%S')

class UserSerializer(serializers.ModelSerializer):

    join_date = DateField()
    join_time = TimeField()

    class Meta:
        model=models.User
        fields='__all__'
        extra_kwargs={
            'password':{'write_only':True}
        }
    def create(self, validated_data):
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    


class VideoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VideoModel
        fields = '__all__'   

        
        
        
