from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import *
from django.contrib.auth.models import User
from django.forms import ModelForm

import datetime


class USER(models.Model):
    USER_REF = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="USER")
    NAME = models.CharField(max_length=100)
    PROFILE_LINK = models.CharField(max_length=100)
    EXPERIENCE_UPVOTE = models.IntegerField()
    ANSWER_UPVOTE = models.IntegerField()
    GUIDE_UPVOTE = models.IntegerField()
    NUM_QUESTION_ASKED = models.IntegerField()
    BADGE1 = models.BooleanField(default=False)
    BADGE2 = models.BooleanField(default=False)
    BADGE3 = models.BooleanField(default=False)
    BADGE4 = models.BooleanField(default=False)
    BADGE5 = models.BooleanField(default=False)

    def __str__(self):
		return self.NAME + '\tKarma Score: ' + str(self.EXPERIENCE_UPVOTE + self.ANSWER_UPVOTE + self.GUIDE_UPVOTE)


class CARDDETAILS(models.Model):
    fullname = models.CharField(max_length = 250)
    cardnumber = models.CharField(max_length = 20)
    mm=models.IntegerField()
    yy=models.IntegerField()
    cvv=models.IntegerField()

    def __str__(self):
        return self.fullname




