from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

# class RegistrationForm(UserCreationForm):
#   email = forms.EmailField(required=True)

#   class Meta:
#     model = User
#     fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
#     #based on order

#   def save(self, commit=True):
#     user = super(RegistrationForm, self).save(commit=False)
#     user.first_name = self.cleaned_data['first_name']
#     user.last_name = self.cleaned_data['last_name']
#     user.email = self.cleaned_data['email']

#     if commit:
#       user.save()
#     return user


class RegistrationForm(forms.Form):
  first_name = forms.CharField()
  last_name = forms.CharField()
  username = forms.CharField(max_length=30)
  email = forms.EmailField(required=True)
  password1 = forms.CharField(widget=forms.PasswordInput)
  password2 = forms.CharField(widget=forms.PasswordInput)
  

  def clean_password2(self):
    password1 = self.cleaned_data.get("password1", "")
    password2 = self.cleaned_data["password2"]
    if password1 != password2:
      raise forms.ValidationError("The two password fields didn't match.")
    return password2