from rest_framework import serializers
from miApp.models import Category, Project

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField() 
    title = serializers.CharField()
    content = serializers.CharField()
    fechaIni = serializers.DateField()

    def create(self, validated_data):
        instance = Project()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):  
        instance.title = validated_data.get("title")
        instance.content = validated_data.get("content")    
        instance.fechaIni = validated_data.get("fechaIni")    

        instance.save()    
        return instance
    

