from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import gettext as _

GENDER_MALE = 0
GENDER_FEMALE = 1
GENDER_NOT_SPECIFIED = 2

GENDER_CHOICES = (
    (GENDER_MALE, _('male')),
    (GENDER_FEMALE, _('female')),
    (GENDER_NOT_SPECIFIED, _('not specified')),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    birth_date = models.DateField(null=True, blank=True)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, default=GENDER_NOT_SPECIFIED,
                                              blank=False, null=False)
    height = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(300)])
    weight = models.PositiveSmallIntegerField(blank=True, null=True, validators=[MaxValueValidator(500000)])

    # TODO: create other models
