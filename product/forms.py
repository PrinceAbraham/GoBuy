from django import forms
from .models import Category

class ProductForm(forms.Form):
    CHOICES = [tuple([x.id,x.name]) for x in Category.objects.all()]
    name = forms.CharField()
    price = forms.IntegerField()
    quantity = forms.IntegerField()
    category = forms.ChoiceField(choices=CHOICES)
    image_url = forms.CharField()

    class Meta:
        model = Category
        fields = ('category')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.none()

class CategoryForm(forms.Form):
    name = forms.CharField()
