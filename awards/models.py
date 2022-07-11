from django.db import models

# Create your models here.

class Award(models.Model):
    award_title = models.CharField(max_length=200)
    description_text = models.CharField(max_length=200, default="an award")
    upload = models.ImageField(upload_to = 'awards/static/awards/useruploads', default='midyearsotbawards/awards/static/awards/img/mdb-favicon.ico')

    def __str__(self):
        return self.award_title
    
    

class Options(models.Model):
    option = models.ForeignKey(Award, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
    nominee_image= models.ImageField(upload_to = 'awards/static/awards/img/nominees', default='midyearsotbawards/awards/static/awards/img/mdb-favicon.ico')

    def __str__(self):
        return self.option_text