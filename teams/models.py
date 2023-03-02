from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    ovr = models.IntegerField(default=50)
    image = models.ImageField(upload_to='images/',null=True)
    shortname = models.CharField(max_length=3,null=True)
    def __str__(self):
        return self.name


class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    ovr = models.IntegerField(default=50)
    POSITION_CHOICES = [
        ('GK', 'Goalkeeper'),
        ('RB', 'Right back'),
        ('CB', 'Center back'),
        ('LB', 'Left back'),
        ('RWB', 'Left wing back'),
        ('LWB', 'Right wing back'),
        ('RM', 'Right midfielder'),
        ('LM', 'Left midfielder'),
        ('CDM', 'Center defensive midfielder'),
        ('CM', 'Center midfielder'),
        ('CAM', 'Center attack midfielder'),
        ('RW', 'Right winger'),
        ('LW', 'Left winger'),
        ('CF', 'Center forward'),
        ('ST', 'Striker'),
    ]
    position = models.CharField(
        max_length=3,
        choices=POSITION_CHOICES,
        default= 'GK',
    )
    def __str__(self):
        return self.name
        return self.team.name