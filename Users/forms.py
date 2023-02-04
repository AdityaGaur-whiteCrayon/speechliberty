from django import forms

from .models import CommentMaster,ContactMaster


class CommentCreateForm(forms.ModelForm):
    class Meta:
        #model = CommentMaster
        fields = ["Emailid","Comments"]



class ContactForm(forms.ModelForm):
    
    class Meta:
        model =  ContactMaster
        fields = ("FullName","Emailid","Subject","Comments")
