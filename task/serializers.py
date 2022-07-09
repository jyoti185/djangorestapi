from rest_framework import serializers
from task.models import EmployeeModels


class EmployeeSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    phone_no = serializers.IntegerField()
    gender = serializers.CharField(max_length=20)
    address = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return EmployeeModels.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id=validated_data.get('id',instance.id)
        instance.name=validated_data.get('name',instance.name)
        instance.email=validated_data.get('email',instance.email)
        instance.phone_no=validated_data.get('phone_no',instance.phone_no)
        instance.gender=validated_data.get('gender',instance.gender)
        instance.address=validated_data.get('address',instance.address)
        instance.save()
        return instance