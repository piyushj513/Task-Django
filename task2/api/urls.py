from django.urls import path
from .views import TaskList,TaskComplete,TaskDetail

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('tasks/<int:pk>/complete/', TaskComplete.as_view(), name='task-complete'),
]

#Approach 2
# from .views import TaskCreate, TaskRetrieve, TaskUpdate, TaskDelete
# urlpatterns = [
#     path('tasks/', TaskList.as_view(), name='task-list'),
#     path('tasks/', TaskCreate.as_view(), name='task-create'),
#     path('tasks/<int:pk>/', TaskRetrieve.as_view(), name='task-retrieve'),
#     path('tasks/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
#     path('tasks/<int:pk>/complete/', TaskComplete.as_view(), name='task-complete'),
#     path('tasks/<int:pk>/delete/', TaskDelete.as_view(), name='task-delete'),
# ]