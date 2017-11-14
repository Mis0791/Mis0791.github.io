from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    notes = models.TextField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Author object: {} {} {} {}>".format(self.first_name, self.last_name, self.email, self.notes)

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(default=0)
    author = models.ManyToManyField(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Book object: {} >".format(self.name)

