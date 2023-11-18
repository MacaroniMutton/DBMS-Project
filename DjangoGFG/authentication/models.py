from django.db import models

# Create your models here.

class Player(models.Model):                         #anytime we want to have a table in our database we need to have model for that
    username=models.CharField(max_length=20, unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=255)
    
    
    class Meta:
        db_table = "Player"

class PlayerProfile(models.Model):
    # Foreign key referencing the Player model's username
    username = models.OneToOneField(Player, on_delete=models.CASCADE, primary_key=True, to_field='username')

    # Other attributes specific to PlayerProfile
    level = models.IntegerField(default=1)
    rank = models.CharField(max_length=255, default='Iron')
    games_played = models.IntegerField(default=0)
    matches_won = models.IntegerField(default=0)
    matches_lost = models.IntegerField(default=0)
    matches_won_curr_lvl = models.IntegerField(default=0)

    def level_up(self):
        # Define the number of matches required to level up
        matches_to_level_up = self.level

        # Check if the player has won enough matches to level up
        if self.matches_won_curr_lvl >= matches_to_level_up:
            # Level up
            self.level += 1
            self.matches_won_curr_lvl = 0  # Reset matches_won for the new level
            self.save()

    class Meta:
        db_table = "PlayerProfile"