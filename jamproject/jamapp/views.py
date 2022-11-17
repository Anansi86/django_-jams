from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import Http404
from rest_framework.response import Response
from .models import Jamapp
from .serializers import JamSerializer

class Jamapp(APIView):
    def get_object(self, pk):
        
        try:
            return Jamapp().objects.get(pk=pk)
        except Jamapp.DoesNotExist:
            raise Http404

    def get(self, request, format=None, pk=None):
       if pk:
            data = self.get_object(pk)
            serializer = TodoSeriallizer(data)
      


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
