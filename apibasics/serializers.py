from django.db.models import fields
from django.db.models.base import Model
from rest_framework import routers, serializers, viewsets
from .models import Loan

# here we used our model in serializer
#we are importing all the fields to serializer from our Models
class loanSerializers(serializers.ModelSerializer):
    class Meta:
        model=Loan
        fields='__all__'
        extra_kwargs={
            "starting_date":{"required":False},
            "ending_date":{"required":False},
        }
        # you can make a list of fields that you want to add


    # typeof = serializers.CharField(max_length=50)
    # agent= serializers.CharField(max_length=50)
    # starting_date= serializers.DateField()
    # ending_date= serializers.DateField()
    # interest_rate=serializers.IntegerField()
    # def create(self,validated_data):
    #     return Loan.objects.create(validated_data)
    # def update(self,instance,validated_data):
    #     instance.typeof=validated_data.get('typeof',instance.typeof)
    #     instance.agent=validated_data.get('agent',instance.agent)
    #     instance.starting_date=validated_data.get('starting_date',instance.starting_date)
    #     instance.ending_date=validated_data.get('ending_date',instance.ending_date)
    #     instance.interest_rate =validated_data.get('interest_rate',instance.interest_rate)
    #     instance.save()
    #     return instance