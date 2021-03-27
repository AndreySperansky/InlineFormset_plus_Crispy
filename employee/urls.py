from django.urls import path
from . import views


app_name = 'employee'

urlpatterns = [
	path('', views.HomepageView.as_view(), name='homepage'),
	path('<int:pk>/', views.CollectionDetailView.as_view(), name='collection_detail'),
    path('create/', views.CollectionCreate.as_view(), name='collection_create'),
    path('update/<int:pk>/', views.CollectionUpdate.as_view(), name='collection_update'),
    path('delete/<int:pk>/', views.CollectionDelete.as_view(), name='collection_delete'),


	]
