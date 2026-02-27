from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.
@api_view(['GET'])
def Quote_list_api(request):
    Quotes= Quote.objects.all()
    serializer = QuoteSerializer(Quotes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def Monthly_Goal(request):
    Monthly_Goal= MonthlyGoals.objects.all()
    serializer = MonthlyGoalsSerializer(Monthly_Goal, many=True)
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


@csrf_exempt
def updated_task(request,pk):
    if request.method == 'PATCH':
        data=json.loads(request.body)
        task=DailyTasks.objects.get(id=pk)
        task.status=data["status"]
        task.save()
        return JsonResponse({"message": "updated"})
    return JsonResponse({"error": "Method not allowed"}, status=405)