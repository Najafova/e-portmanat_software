from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from portmanat_app.serializers import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

class MobileDataViewSet(viewsets.ModelViewSet):
    queryset = MobileData.objects.all()
    serializer_class = MobileDataSerializer


def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = MobileData.objects.all()
        serializer = MobileDetailSerializer(snippets, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def mobile_detail(request, imei_code):
    try:
        snippet = MobileData.objects.get(imei_code=imei_code)
    except MobileData.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if  request.method == 'GET':
        serializer = MobileDetailSerializer(snippet)
        return Response(serializer.data)


@csrf_exempt
def data(request):
    incoming_data = request.body.decode().strip()
    print(incoming_data)
    
    if ',' in incoming_data:
        parsed_data = incoming_data.split(',')
    else:
        parsed_data = incoming_data

    print(parsed_data[1][0])
    if parsed_data[1][0]=="0" or parsed_data[2][0]=="0":
        print("if e girdi")
        return HttpResponse("nothing")
        
    else:
        print("else e girdi")
        temp = parsed_data[1]
        long_first = int(temp[0:2]) #bunu sonda elave edessen - longitude
        long_second = round(float(temp[2:])/60,6) #bunu sonda elave edeceksen - longitude
        parsed_data[1] = round(long_first + long_second,6)

        temp = parsed_data[2]
        lat_first = int(temp[0:2])
        lat_second = round(float(temp[2:])/60,6)
        print(lat_second)
        print(lat_first)
        parsed_data[2] = round(lat_first + lat_second,6)
        print(parsed_data[2])
        # print(parsed_data[1])
        # print(parsed_data[2])

        Data.objects.create(imei_code=parsed_data[0], latitude=parsed_data[1], longitude=parsed_data[2], battery=parsed_data[3])
        print ("elave oldu")
        if MobileData.objects.filter(imei_code=parsed_data[0]):
            MobileData.objects.filter(imei_code=parsed_data[0]).update(latitude=parsed_data[1], longitude=parsed_data[2], battery=parsed_data[3])
        else:
            MobileData.objects.filter(imei_code=parsed_data[0]).create(imei_code=parsed_data[0], latitude=parsed_data[1], longitude=parsed_data[2], battery=parsed_data[3])
        
        # print(parsed_data)
        return HttpResponse(parsed_data)