from django import forms
from .models import UserProfileInfo,Items_lost,Contact_us
from django.contrib.auth.models import User



class User_form(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs={
                    'style': 'width: 400px;height:40px; color:White;border-radius:8px;',
                    'placeholder': '  Enter Password',
                                }) )

    class Meta:
        model = User
        fields=('username','email','password')
        widgets = {
                'username': forms.TextInput(attrs={
                                'style': 'width: 400px;height:40px;border-radius:8px;',
                                'placeholder': '  Enter your Name',
                                            }),
                'email': forms.EmailInput(attrs={
                                'style': 'width: 400px;height:40px;border-radius:8px;',
                                'placeholder': '  Enter Sastra Mail id',
                                            }),
                }

class UserProfileInfo_form(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields=('register_no','mobile_no','branch','id_card_pic')
        widgets = {
                'register_no': forms.TextInput(attrs={
                                'style': 'width: 400px;height:40px;border-radius:8px;',
                                'placeholder': '  Enter Register Number',
                                            }),
                'mobile_no': forms.TextInput(attrs={
                                'style': 'width: 400px;height:40px;border-radius:8px;',
                                'placeholder': '  Enter your Mobile Number',
                                            }),
                'branch' : forms.Select(attrs={
                                'style': 'width: 405px;height:40px;border-radius:8px;',
                                            }),
    }


class Items_lost_form(forms.ModelForm):
    class Meta:
        model = Items_lost
        exclude = ['usernamee','timestamp','catogeory']
        widgets = {
            'item_name' : forms.TextInput(attrs ={
                'style': 'width: 400px;height:40px;border-radius:8px;',
                'placeholder': ' Enter Item Name',
                        }),
            'expected_place' : forms.TextInput(attrs ={
                'style': 'width: 400px;height:40px;border-radius:8px;',
                'placeholder': ' Enter expected place of lost',
                        }),
            'item_details':forms.Textarea(attrs ={
                'style': 'width: 400px;height:170px;border-radius:8px;',
                'placeholder': ' Enter few details of the object like colour, any markings etc.',
                        }),
        }


class Contact_us_form(forms.ModelForm):
    class Meta:
        model = Contact_us
        exclude = ['name']
        widgets = {
                'subject' : forms.TextInput(attrs ={
                    'style': 'width: 400px;height:40px;border-radius:8px;',
                    'placeholder': ' Subject',
                            }),
                'message':forms.Textarea(attrs ={
                    'style': 'width: 400px;height:200px;border-radius:8px;',
                    'placeholder': ' Enter your Message here.',
                            }),

        }
