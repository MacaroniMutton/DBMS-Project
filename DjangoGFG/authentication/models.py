from django.db import models

# Create your models here.

class Player(models.Model):                         #anytime we want to have a table in our database we need to have model for that
    username=models.CharField(max_length=20, unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20)
    
    
    class Meta:
        db_table = "Player"
