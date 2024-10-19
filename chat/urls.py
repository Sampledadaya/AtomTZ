from django.urls import path
from .views import ChannelListCreateView, ChannelDetailView, MessageListCreateView, MessageDetailView

urlpatterns = [
    path('channels/', ChannelListCreateView.as_view(), name='channel-list-create'),
    path('channels/<int:pk>/', ChannelDetailView.as_view(), name='channel-detail'),
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),
]
