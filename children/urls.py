from django.urls import path
from .views import ChildrenListView, ChildrenDetailView, ChildrenCreateView, ChildrenUpdateView, ChildrenDeleteView
from . import views

urlpatterns = [
    path('', ChildrenListView.as_view(), name='children-list'),
    path('children/<int:pk>/', ChildrenDetailView.as_view(), name='children-detail'),
    path('children/new/', ChildrenCreateView.as_view(), name='children-create'),
    path('children/<int:pk>/update/', ChildrenUpdateView.as_view(), name='children-update'),
    path('children/<int:pk>/delete/', ChildrenDeleteView.as_view(), name='children-delete'),
]