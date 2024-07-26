from django.urls import path
from .views import TeamViewSet

team_list = TeamViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

team_detail = TeamViewSet.as_view({
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('teams/', team_list, name='team-list'),
    path('teams/<int:pk>/', team_detail, name='team-detail'),
]
