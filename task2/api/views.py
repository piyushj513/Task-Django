from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import Task
from .serializers import TaskSerializer


class BaseClass(APIView):
    model = None  # model in the subclasses
    serializer_class = None  # serializer class in the subclasses

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise NotFound(detail='Object not found')

    def get(self, request, pk):
        instance = self.get_object(pk)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        instance = self.get_object(pk)
        instance.delete()
        return Response({'message': 'Object deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class TaskList(BaseClass):
    model = Task
    serializer_class = TaskSerializer

    def get(self, request):
        instances = self.model.objects.all()
        serializer = self.serializer_class(instances, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(BaseClass):
    model = Task
    serializer_class = TaskSerializer


class TaskComplete(APIView):
    def post(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise NotFound(detail='Task not found')

        task.completed = True
        task.save()
        return Response({'message': 'Task marked as completed'}, status=status.HTTP_200_OK)





#Approach 2
# class TaskList(APIView):
#     def get(self, request):
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)

# class TaskCreate(APIView):
#     def post(self, request):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TaskRetrieve(APIView):
#     def get(self, request, pk):
#         try:
#             task = Task.objects.get(pk=pk)
#         except Task.DoesNotExist:
#             return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = TaskSerializer(task)
#         return Response(serializer.data)

# class TaskUpdate(APIView):
#     def put(self, request, pk):
#         try:
#             task = Task.objects.get(pk=pk)
#         except Task.DoesNotExist:
#             return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

#         serializer = TaskSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TaskComplete(APIView):
#     def post(self, request, pk):
#         try:
#             task = Task.objects.get(pk=pk)
#         except Task.DoesNotExist:
#             return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

#         task.completed = True
#         task.save()
#         return Response({'message': 'Task marked as completed'}, status=status.HTTP_200_OK)

# class TaskDelete(APIView):
#     def delete(self, request, pk):
#         try:
#             task = Task.objects.get(pk=pk)
#         except Task.DoesNotExist:
#             return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

#         task.delete()
#         return Response("Task deleted successfully", status=status.HTTP_204_NO_CONTENT)
