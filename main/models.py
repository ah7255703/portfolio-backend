from django.db import models


class PortfolioWork(models.Model):
    image_url = models.TextField()
    title     = models.CharField(max_length=50)
    