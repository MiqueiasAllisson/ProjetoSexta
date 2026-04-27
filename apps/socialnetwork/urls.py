from django.urls import path
from . import views
from rest_framework import routers

app_name = 'socialnetwork'

router = routers.SimpleRouter()
router.register('', views.SocialNetworkViewSet, basename='socialnetworks')

urlpatterns = [
    path('listar/', views.list_socialnetworks, name='list_socialnetworks'),
    path('adicionar/', views.add_socialnetwork, name='add_socialnetwork'),
    path('editar/<int:id_socialnetwork>/', views.edit_socialnetwork, name='edit_socialnetwork'),
    path('excluir/<int:id_socialnetwork>/', views.delete_socialnetwork, name='delete_socialnetwork'),
]