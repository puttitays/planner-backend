from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import QuoteSerializer, TaskSerializer


# Create your views here.
@api_view(['GET'])
def Quote_list_api(request):
    Quotes= Quote.objects.all()
    serializer = QuoteSerializer(Quotes, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def task_list_api(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)