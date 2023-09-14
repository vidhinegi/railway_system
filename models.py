#from django.db import models

#class Train(models.Model):
 #   train_id = models.IntegerField(primary_key=True)
  #  station1 = models.TextField()
   # station2 = models.TextField()
    #station3 = models.TextField()
    #station4 = models.TextField()
    #station5 = models.TextField()
    #station6 = models.TextField()
    #station7 = models.TextField()
    #station8 = models.TextField()
    #station9 = models.TextField()
    #station10 = models.TextField()
    #class Meta:
     # db_table="train"
    #def __str__(self):
     #   return self.train_id
from django.db import models


class Train(models.Model):
    train_id = models.IntegerField(primary_key=True)
    station1 = models.TextField()
    station2 = models.TextField()
    station3 = models.TextField()
    station4 = models.TextField()
    station5 = models.TextField()
    station6 = models.TextField()
    station7 = models.TextField()
    station8 = models.TextField()
    station9 = models.TextField()
    station10 = models.TextField()

    class Meta:
        db_table = "train"

    def __str__(self):
        return str(self.train_id)


class Station(models.Model):
    station_name = models.TextField(primary_key=True)
    train1 = models.TextField(max_length=100)
    train2 = models.TextField(max_length=100)
    train3 = models.TextField(max_length=100)
    train4 = models.TextField(max_length=100)
    train5 = models.TextField(max_length=100)
    

    class Meta:
        db_table = "station_schedule"
        
    def __str__(self):
        return str(self.station_name)


class Seat(models.Model):
    seat_id = models.IntegerField(primary_key=True)
    coach_no = models.IntegerField()
    seat_no = models.IntegerField()

    class Meta:
       db_table = "seat"

    def __str__(self):
        return self.seat_id

