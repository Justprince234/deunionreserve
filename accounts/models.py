from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.urls import reverse
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail  
# Create your models here.

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="DeunionReserve Customer account"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@deunionreserve.com",
        # to:
        [reset_password_token.user.email]
    )


SEX = (
    ('M', 'Male'),
    ('F', 'Female'),
)

ACCOUNT_TYPE = (
    ('Savings', 'Savings'),
    ('Current', 'Current'),
)

class UpdateUser(models.Model):
    """Update user credentials"""
    passport = models.ImageField(upload_to='photos/%Y/%m/%d/')
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    sex = models.CharField(choices=SEX, max_length=1)
    dob = models.DateField()
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    valid_ID_frontview = models.ImageField(upload_to='photos/%Y/%m/%d/')
    valid_ID_backview = models.ImageField(upload_to='photos/%Y/%m/%d/')
    account_type = models.CharField(choices=ACCOUNT_TYPE, default='Savings', max_length=7)
    next_of_kin = models.CharField(max_length=100)
    relationship_nok = models.CharField(max_length=50)
    phone_nok = models.CharField(max_length=50)
    date_updated = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "User Data"
  
    def __str__(self):
        return self.first_name