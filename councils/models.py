from django.db import models

# Create your models here.
class Councils(models.Model):
    council_name=models.CharField(max_length=100)
    def __str__(self):
        return self.council_name


class Clubs(models.Model):
    council=models.ForeignKey(Councils,on_delete=models.CASCADE)
    club_name=models.CharField(max_length=100)
    club_title=models.CharField(max_length=50)
    club_description=models.CharField(max_length=2000,default='No data available')

    def __str__(self):
        return self.club_name

class Achievements(models.Model):
    council=models.ForeignKey(Councils,on_delete=models.CASCADE)
    achievement_title=models.CharField(max_length=100)
    achievement_detail=models.CharField(max_length=500)
    achievement_image=models.CharField(max_length=300)

    def __str__(self):
        return self.achievement_title

class Clubevents(models.Model):
    club=models.ForeignKey(Clubs,on_delete=models.CASCADE)
    event_title=models.CharField(max_length=100)
    event_detail=models.CharField(max_length=2000)
    event_image=models.CharField(max_length=300)

    def __str__(self):
        return self.event_title

class Clubgallery(models.Model):
    club=models.ForeignKey(Clubs,on_delete=models.CASCADE)
    clubgallery_image=models.CharField(max_length=300)
    clubgallery_title=models.CharField(max_length=200)

    def __str__(self):
        return self.clubgallery_title