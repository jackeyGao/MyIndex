from __future__ import unicode_literals

from django.db import models

# Create your models here.

class APP(models.Model):
    name = models.CharField(max_length=200)
    repo = models.CharField(max_length=100, null=True, blank=True)
    demo = models.CharField(max_length=100, null=True, blank=True)
    desc = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Skill(models.Model):
    SKILL_TYPES = (
        ('SL', 'Skill'),
        ('FM', 'Framework'),
    )
    name = models.CharField(max_length=45)
    level = models.CharField(max_length=10)
    start = models.IntegerField()
    s_type = models.CharField(max_length=2,
        choices=SKILL_TYPES,        
    )

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Profile(models.Model):
    key = models.CharField(max_length=45)
    value = models.CharField(max_length=100)

    @staticmethod
    def get_profile():
        profile = {}
        for i in Profile.objects.all():
            profile[i.key] = i.value

        return profile

    def __str__(self):
        return self.key

    def __unicode__(self):
        return self.key

