from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse    
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView
from django.views.generic.base import TemplateView
from BlogAdmin.models import BlogMaster
from vanilla import DetailView
from .forms import  ContactForm
from .models import CommentMaster
from django.views import View



class DiscussionList(ListView):
    model = BlogMaster
    template_name= 'Users/Topic.html'


class Discussion(View):
    
  def post(self,request):
      obj = CommentMaster(Blogid=BlogMaster.objects.get(pk=request.POST["txtID"]),
      Emailid=request.POST["txtEmail"],Comments=request.POST["Comments"])
      obj.save()
      pk=request.POST["txtID"]
      return redirect('/Discussion?q='+pk)
      #return redirect('Discussion')
  def get(self,request):
      data =  BlogMaster.objects.filter(pk=request.GET["q"])
      data2 = CommentMaster.objects.filter(Blogid=request.GET["q"])
      return render(request,"Users/Discussion.html",{'res':data, 'result':data2})

class ContacFormView(CreateView):
    form_class = ContactForm
    template_name = "Users/ContactMaster_form.html"
    success_url ="AboutUs"

class AboutUs(TemplateView):
    template_name = 'Users/aboutus.html'

'''class DiscussionDetailView(DetailView):
   
# Vanilla View Refrence www.agiliq.com/  Working =true
    def get(self, request, *args, **kwargs):
        topic = get_object_or_404(BlogMaster, pk=kwargs['pk'])
        context = {'object':topic}
        return render(request, 'Users/Discussion.html', context)
#Generic Deatils View  Refrence Site Geeks For Geeks Working =true
    model = BlogMaster
    def get_context_data(self, *args, **kwargs):
        context = super(DiscussionDetailView,
             self).get_context_data(*args, **kwargs)        
        return context
    template_name= 'Users/Discussion.html''' 
    #fghrfghfg
'''class CommentCreateView(CreateView):
    #form_class = CommentCreateForm
    #template_name= 'Users/Discussion.html'
    def get(self, request, *args, **kwargs):
        context = {'form': CommentCreateForm()}
        return render(request, 'Users/Discussion.html', context)

    def post(self, request, *args, **kwargs):
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            CommentMaster = form.save()
            CommentMaster.save()
            return HttpResponse("Data Submitted Sucessfully")
        return render(request, 'Users/Discussion.html', {'form': form})'''
# Vanilla View Refrence www.agiliq.com/  Working =true
#class CommentCreateView(CreateView):
   # model = CommentMaster
  #  fields = ['Emailid','Comments']
  #  template_name = 'Users/1/?q=1'
'''class CommentCreateView(CreateView,DetailView):
    model = CommentMaster
    form_class = CommentCreateForm

    def get_context_data(self, **kwargs):
        context = super(DiscussionDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


    def post(self, request, *args, **kwargs):
        return CreateView.post(self, request, *args, **kwargs)'''

'''def get(self, request, *args, **kwargs):
        context = {'form':CommentCreateForm()}
        return render(request, 'Users/Discussion.html', context)

    def post(self, request, *args, **kwargs):
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            CommentMaster = form.save()
            CommentMaster.save()
            return HttpResponse("Data Submitted Sucessfully")
           # return HttpResponseRedirect(reverse_lazy('books:detail', args=[book.id]))
        return render(request, 'Users/Discussion.html', {'form': form})

class CommentPostView(CreateView):
    model = YourModel
    template_name = "your-template.html"

    def get_context_data(self. **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context'''