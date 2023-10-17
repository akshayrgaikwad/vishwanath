from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from .models import EmployeeModel
from .forms import EmployeeForm
from .serializer import EmployeeSerializer
from rest_framework.response import Response
# Create your views here.

def form_data(request):
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            form = EmployeeForm()
    return render(request,'apiapp/employee_form.html',{'form':form})


def fetch_data(request):
    qs = EmployeeModel.objects.all()
    return render(request,'apiapp/data.html',{"employees":qs})



class Fetch_Api(APIView):
    def get(self,request,*args,**kwargs):
        qs = EmployeeModel.objects.all()
        serializer_object = EmployeeSerializer(qs,many=True)
        return Response(serializer_object.data, status=status.HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        serializer_object = EmployeeSerializer(data=request.data)
        if serializer_object.is_valid():
            serializer_object.save()
            return Response(serializer_object.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_object.errors, status=status.HTTP_400_BAD_REQUEST)



class ModifyApi(APIView):
    def get(self,request,pk,*args,**kwargs):
        try:
            io = EmployeeModel.objects.get(employee_id=pk)
        except EmployeeModel.DoesNotExist:
            return Response('Employee ID not Registered', status=status.HTTP_404_NOT_FOUND)
        serializer_object = EmployeeSerializer(io)
        return Response(serializer_object.data,status=status.HTTP_200_OK)

    def put(self,request,pk,*args,**kwargs):
        io = EmployeeModel.objects.get(employee_id=pk)
        serializer_object = EmployeeSerializer(io,data=request.data)
        if serializer_object.is_valid():
            serializer_object.save()
            return Response(serializer_object.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_object.errors,status=status.HTTP_400_BAD_REQUEST)


    def patch(self,request,pk,*args,**kwargs):
        io = EmployeeModel.objects.get(employee_id=pk)
        serializer_object = EmployeeSerializer(io,data=request.data,partial=True)
        if serializer_object.is_valid():
            serializer_object.save()
            return Response(serializer_object.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_object.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,*args,**kwargs):
        io = EmployeeModel.objects.get(employee_id=pk)
        if io:
            io.delete()
        return Response('object deleted Successfully',status=status.HTTP_200_OK)