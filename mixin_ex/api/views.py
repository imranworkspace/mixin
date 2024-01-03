from django.shortcuts import render
from .models import StudentModel
from .serialization import StudentSerializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
# Create your views here.

class StudentList(ListModelMixin,GenericAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializers

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class StudentCreate(CreateModelMixin,GenericAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializers

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)