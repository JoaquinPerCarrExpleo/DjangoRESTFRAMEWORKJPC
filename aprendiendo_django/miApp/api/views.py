from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from miApp.api.serializers import ProjectSerializer
from miApp.models import Category, Project
from django.shortcuts import get_object_or_404

class ProjectListAPI(APIView):
    
    def get_project(self, request, pk):
        project = get_object_or_404(Project, pk = pk)
        return project

    def get(self, request):
        project = self.get_project(request, pk) 
        serializer = ProjectSerializer(instance = project)
        return Response(serializer.data)

    def post(self, request):     
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)