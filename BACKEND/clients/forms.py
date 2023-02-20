from django import forms
from .models import UserInfoModel
from django.utils.translation import gettext as _


class SignupForm(forms.Form):
    first_name = forms.CharField(
        max_length=30, required=True, label=_("First name"), widget=forms.TextInput(
            attrs={'placeholder': _('First name')}))
    last_name = forms.CharField(
        max_length=30, required=True, label=_("Last name"), widget=forms.TextInput(
            attrs={'placeholder': _('Last name')}))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()


class ClientInfoForm(forms.ModelForm):
    date_of_birth = forms.DateField(label="", widget=forms.DateTimeInput(attrs={
        'type': "date", 'class': "form datepicker"
    }))
    gender = forms.ChoiceField(choices=UserInfoModel.GENDER_CHOICE,
                               label="", widget=forms.Select(attrs={'class': 'form', 'placeholder': 'Select Gender'}))
    phone_number = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form', 'placeholder': 'Enter phone number'}))
    address = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form', 'placeholder': 'Enter address'}))
    state = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form', 'placeholder': 'Enter your state'}))

    city = forms.CharField(label="", widget=forms.TextInput(
        attrs={'class': 'form', 'placeholder': 'Enter Your city'}))

    class Meta:
        model = UserInfoModel
        fields = ['phone_number', 'date_of_birth',
                  'gender', 'address', 'country', 'state', 'city']
        widgets = {
            'country': forms.Select(attrs={'class': 'title flex-1 w-full p-4 my-4 bg-white rounded-xl'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
