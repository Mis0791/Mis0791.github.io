from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<User object: {} {} {}>".format(self.first_name, self.last_name, self.email)

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(default=0)
    uploader = models.ForeignKey(User, related_name="uploaded_books")
    user = models.ManyToManyField(User, related_name="likes")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Book object: {}>".format(self.name)    