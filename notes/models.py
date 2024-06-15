from django.db import models

# Create your models here.

class Note(models.Model):
    title=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Entry(models.Model):
    note=models.ForeignKey(Note,on_delete=models.CASCADE)
    text=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text



