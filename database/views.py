from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import QuoteSerializer, TaskSerializer,ComplteTasksSerializer


# Create your views here.
@api_view(['GET'])
def Quote_list_api(request):
    Quotes= Quote.objects.all()
    serializer = QuoteSerializer(Quotes, many=True)
    return Response(serializer.data)



@api_view(["GET", "POST"])
def task_list_api(request):
    if request.method == 'POST':
        if request.data.get('status')=="on progress":
            serializer = TaskSerializer(data=request.data)
        else:
            serializer = ComplteTasksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    if request.method == 'GET':
        tasks = DailyTasks.objects.all()
        serializer = TaskSerializer(tasks,many=True)
        return Response(serializer.data)

