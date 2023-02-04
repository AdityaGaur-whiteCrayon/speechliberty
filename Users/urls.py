from django.urls import path

from . import views
from .views import DiscussionList,Discussion,ContacFormView,AboutUs

urlpatterns = [
    path('', DiscussionList.as_view()),
    path('Discussion',Discussion.as_view(), name='Discussion'),
    path('ContacFormView',ContacFormView.as_view()),
    path('AboutUs',AboutUs.as_view(),name="aboutus")
    #path('<pk>/',DiscussionDetailView.as_view()),
    #path('CommentPostView',CommentPostView.as_view(),),
    #path('create', views.CommentCreateView.as_view(), name='create'),
    #path('1/?q=1', CommentCreateView.as_view() ),
    #url(r"^$", ListNotes.as_view(), name="list_notes"),
]