from django.db import models
from django.contrib.auth.models import User

class Subscriber(models.Model):
    user_rec = models.ForeignKey(User,
    on_delete=models.CASCADE,)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    stripe_id = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name_plural = 'subscribers'

    def __str__(self):
        return u"%s " % self.user_rec

class Teacher(models.Model):
    user_rec = models.ForeignKey(User,
    on_delete=models.CASCADE,)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    stripe_id = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name_plural = 'Teacher'

    def __str__(self):
        return u"%s " % self.user_rec


class Student(models.Model):
    user_rec = models.ForeignKey(User,
    on_delete=models.CASCADE,)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    stripe_id = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name_plural = 'Student'

    def __str__(self):
        return u"%s " % self.user_rec


class Project(models.Model):
    user_rec = models.ForeignKey(User,
    on_delete=models.CASCADE,)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    stripe_id = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name_plural = 'Project'

    def __str__(self):
        return u"%s " % self.user_rec

class ProjectGroup(models.Model):
    user_rec = models.ForeignKey(User,
    on_delete=models.CASCADE,)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    stripe_id = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name_plural = 'ProjectGroup'

    def __str__(self):
        return u"%s " % self.user_rec



class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication, related_name="articles")

    class Meta:
        ordering = ('headline',)

    def __str__(self):
        return self.headline

class Agenda(models.Model):
    title = models.CharField(max_length=30)
    