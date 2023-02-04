from django.urls import path


# importing views from views..py
from .views import TopicCreate, TopicList, TopicDetailView, TopicUpdateView,TopicDeleteView,CommentList,ContactList
urlpatterns = [
    path('TopicCreate',TopicCreate.as_view() ),
    path('', TopicList.as_view()),
    path('<pk>/', TopicDetailView.as_view()),
    path('<pk>/update', TopicUpdateView.as_view()),
    path('<pk>/delete/', TopicDeleteView.as_view()),
    path('ContactList', ContactList.as_view()),
    path('CommentList', CommentList.as_view()),
]