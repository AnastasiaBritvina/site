from django.db import models

class CategoryOfFB(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Feedback(models.Model):
    guest = models.CharField(max_length=300)
    body = models.TextField()
    category = models.ForeignKey(CategoryOfFB, related_name="category", on_delete=models.SET_NULL, default=None,
                                 null=True,
                                 blank=True)