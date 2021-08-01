from django.db import models
from django.core.validators import RegexValidator
from django import forms
from django.contrib.auth.models import User
from datetime import datetime,date



class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)#additional
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    branches = ( ("CSE","CSE"),("IT","IT"),("ICT","ICT"),("ECE","ECE"),("EEE","EEE"),
                    ("EIE","EIE"),("Mechanical","Mechanical"),("Mechatronics","Mechatronics"),
                    ("Civil","Civil"),("Bio-Technology","Bio-Technology")   )
    statuses = (("Verified","Verified"),("Not-Verified","Not-Verified"))

    register_no = models.CharField(max_length=9, unique = True)
    branch = models.CharField(max_length=254, choices = branches )
    mobile_no = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    id_card_pic = models.ImageField()
    status = models.CharField(max_length= 254, default= 'Not-Verified', choices = statuses )

    def __str__(self):
        return self.user.username


#item name, Expected place of lost , picture , item details ,

class Items_lost(models.Model):
    usernamee = models.ForeignKey(User,on_delete=models.CASCADE)
    emaill =models.CharField(max_length = 254,blank = True)
    item_name = models.CharField(max_length = 254)
    item_details = models.TextField()
    expected_place = models.CharField(max_length = 254,default = 'None')
    #item_pic = models.ImageField(blank = True)
    timestamp=models.DateTimeField(default=datetime.now, blank= True)
    catogeory = models.CharField(default = "Lost", max_length = 50)
    # IDEA: Status field : default = item not yet found / item found / item found and recieved


class Contact_us(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=300)
    message = models.TextField()















# class User_details(models.Model):
#     phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
#     branches = ( ("CSE","CSE"),("IT","IT"),("ICT","ICT"),("ECE","ECE"),("EEE","EEE"),
#                     ("EIE","EIE"),("Mechanical","Mechanical"),("Mechatronics","Mechatronics"),
#                     ("Civil","Civil"),("Bio-Technology","Bio-Technology")   )
#     statuses = (("Verified","Verified"),("Not-Verified","Not-Verified"))
#
#     Name = models.CharField(max_length=254)
#     Register_no = models.CharField(max_length=9, unique = True)
#     Branch = models.CharField(max_length=254, choices = branches )
#     Sastra_email_id = models.EmailField(unique = True )
#     Password = models.CharField(max_length=254) #note some change is needed in forms
#     Mobile_no = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
#     Id_card_pic = models.ImageField()
#     Status = models.CharField(max_length= 254, default= 'Not-Verified', choices = statuses )
