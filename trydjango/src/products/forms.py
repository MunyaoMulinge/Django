from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    email = forms.EmailField()
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "placeholder": "Your description",
        "class": "new-class-name-two",
        "rows": 20,
        "cols": 120
    }))
    price = forms.DecimalField(initial=76.77)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


def clean_title(self, *args, **kwargs):
    title = self.cleaned_data.get("title")
    if not "CFE" in title:
        raise forms.ValidationError("Not a valid title")
    if not "news" in title:
        raise forms.ValidationError("Not a valid title")
    return title


def clean_email(self, *args, **kwargs):
    email = self.cleaned_data.get("email")
    if not email.endswith("edu"):
        raise forms.ValidationError("Invalid Email")
    return email


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "placeholder": "Your description",
        "class": "new-class-name-two",
        "rows": 20,
        "cols": 120
    }))
    price = forms.DecimalField(initial=76.77)
