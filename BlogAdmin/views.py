from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import BlogMaster
from Users.models import CommentMaster,ContactMaster
  
class TopicCreate(CreateView):
    model =  BlogMaster
    template_name= 'BlogAdmin/BlogMaster_form.html'
    fields = ['Topic', 'Category','Intro','Description','Varified']
    success_url ="/BlogAdmin"

class TopicList(ListView):
    model = BlogMaster
    template_name= 'BlogAdmin/BlogMaster_list.html'

class TopicDetailView(DetailView):
    model = BlogMaster
    template_name= 'BlogAdmin/BlogMaster_detail.html'
    def get_context_data(self, *args, **kwargs):
        context = super(TopicDetailView,
             self).get_context_data(*args, **kwargs)
        #context["category"] = "MISC"         
        return context

class TopicUpdateView(UpdateView):
    model = BlogMaster
    template_name= 'BlogAdmin/BlogMaster_form.html'
    fields = [
        "Topic", "Category","Intro","Description","Varified"
    ]
    success_url ="/BlogAdmin"

class TopicDeleteView(DeleteView):
    model = BlogMaster
    template_name= 'BlogAdmin/BlogMaster_confirm_delete.html'
    success_url ="/BlogAdmin"


class CommentList(ListView):
    model = CommentMaster 
    template_name= 'BlogAdmin/CommentMaster_list.html'


class ContactList(ListView):
    model = ContactMaster
    template_name= 'BlogAdmin/ContactMaster_list.html'
