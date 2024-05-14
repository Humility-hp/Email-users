from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re
from django.contrib import messages

# Create your models here.
def contactVal(contact):
 validate = re.findall("^080.{8}$|^081.{8}$|^090.{8}$|091.{8}$|^070.{8}$",contact)
 if not validate:
  raise ValidationError(("%(contact)s must be a nigerian number"),params={"contact":contact})
 

class pendingUser(models.Model):
 created_by = models.ForeignKey()
 first_name = models.CharField('Username', max_length=20)
 last_name = models.CharField(max_length=20)
 contact_info = models.CharField(max_length=11, unique=True, validators=[contactVal])
 def __str__(self):
  return self.first_name