from django.db import models
from django.utils import timezone
from bigml.api import BigML
from .Util import list_teams, prediction, list_referees

api = BigML('felmarlop', '0b4b8f7e1c73500796bc00b974518b571abf752f')

# Create your models here.
class Match(models.Model):
    dataset = api.get_dataset('dataset/5638ac833cd257473c00011a')
    model = api.get_ensemble("ensemble/5638acb33cd25747350000dd")
    teams = list_teams(dataset)
    referees = list_referees(dataset)
    
    PLACE = (
        ('Home', 'Home'),
        ('Away', 'Away'),
    )
    TEAMS = ( [('','Select team...')] +teams )
    REFEREES = ([('','Select referee...')] + referees)
    DAYS_WEEK = (
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday'),
    )
    
    author = models.ForeignKey('auth.User')
    Real_Madrid = models.CharField(blank= False, default='Home' ,max_length = 30, choices = PLACE)
    away_team = models.CharField(blank=False, max_length = 30, choices = TEAMS)
    match_day = models.CharField(blank=False, default='6', max_length = 30, choices = DAYS_WEEK)
    referee = models.CharField(blank=False, max_length = 30, choices = REFEREES)
    created_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(
            blank=True, null=True) 
    prediction = models.CharField(max_length = 10, blank =True, null=True)
    confidence = models.CharField(max_length = 10, blank =True, null=True)
    
    def publish(self):
        pred = prediction(self.Real_Madrid, self.away_team, self.match_day, self.referee, self.model)
        self.prediction = pred [0]
        self.confidence = pred [1]
        self.published_date = timezone.now()
        self.save()
        
    
    def __str__(self):
        return "Real Madrid ("+self.Real_Madrid+") vs "+self.away_team
    