from django.db import models

class Blog(models.Model):
    blogTitle = models.CharField(max_length=128)
    blogBody = models.TextField()
    blogDesc = models.TextField()
    blogPhoto = models.ImageField(upload_to="image/%Y/%m/%d", blank=True)

    def __str__(self):
        return self.blogTitle