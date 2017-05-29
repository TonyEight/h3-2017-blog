from django.db import models


class Category(models.Model):
    label = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.label

    
class Entry(models.Model):
    title = models.CharField(max_length=600)
    content = models.TextField()
    category = models.ForeignKey(
    	Category,
    	on_delete=models.CASCADE,
    	related_name='entries'
    )

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"

    def __str__(self):
        return self.title

    
