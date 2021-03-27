from django.db import models
from django.conf import settings


class Collection(models.Model):
    subject = models.CharField(max_length=300, blank=True)
    owner = models.CharField(max_length=300, blank=True)
    note = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True,  on_delete=models.SET_NULL, related_name="collections")
    # dash = request.created_by.collection.all()  для доступа ко всем резюме пользователя

    def __str__(self):
        return str(self.id)


class CollectionTitle(models.Model):
    """
    A Class for Collection titles.
    """
    collection = models.ForeignKey(Collection,
        related_name="has_titles", on_delete=models.CASCADE)
    name = models.CharField(max_length=500, verbose_name="Title")
    language = models.CharField(max_length=3)
