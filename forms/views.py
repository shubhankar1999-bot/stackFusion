from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
def test(request):
    stck_obj=StackFusion.objects.all()
    serializer= FromSerializer(stck_obj,many=True)
    return Response({'status':200, 'payload':serializer.data})

@api_view(['POST'])
def add_Form(request):
    data=request.data
    print(data)
    serializer=FromSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'status':403, 'errors':serializer.errors, 'message':'Error Sending Data'})
    serializer.save()
    return Response({'status':200, 'payload':serializer.data, 'message':'Sent Successfully'})

@api_view(['DELETE'])
def delete_form_data(request,id):
    try:
        form_obj=StackFusion.objects.get(id=id)
        form_obj.delete()
        return Response({'status':200, 'message':'Deleted'})
    except Exception as e:
        return Response({'status':200, 'message':'Invalid id'})

