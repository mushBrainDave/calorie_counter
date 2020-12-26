from datetime import datetime

from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


@csrf_exempt
@api_view(['GET', 'POST'])
def setting_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        setting = Setting.objects.filter(user=request.user)
        serializer = SettingSerializer(setting, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SettingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getSetting(request, pk):
    """
    Retrieve, update or delete a customer instance.
    """
    try:
        settings = Setting.objects.get(pk=pk)
    except Setting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SettingSerializer(settings, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        request.data["user"] = request.user.id
        serializer = SettingSerializer(settings, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        settings.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST'])
def intake_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        intake = DailyIntake.objects.filter(user=request.user)
        serializer = IntakeSerializer(intake, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        request.data["user"] = request.user.id
        serializer = IntakeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST'])
def intake_list_date(request, date):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        #start_date = datetime(2020, 10, 27)
        #end_date = datetime(2020, 10, 28)
        start_date = datetime(date[0])
        end_date = datetime(date[1])
        intake = DailyIntake.objects.filter(user=request.user).filter(intake_date__range=(start_date, end_date))
        serializer = IntakeSerializer(intake, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        request.data["user"] = request.user.id
        serializer = IntakeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def getIntake(request, pk):
    """
    Retrieve, update or delete a customer instance.
    """
    try:
        intake = DailyIntake.objects.get(pk=pk)
    except DailyIntake.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IntakeSerializer(intake, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = IntakeSerializer(intake, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        intake.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)