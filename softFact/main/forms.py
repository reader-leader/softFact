from django.forms import ModelForm
from .models import Comments

class CommentForm(ModelForm):

    class Meta:
        model = Comments
        fields = ('created_date', 'comment')

