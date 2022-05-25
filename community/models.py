from django.db import models
# Create your models here.

class Tag(models.Model): # 태그 모델
    name = models.CharField(max_length=12)
    value = models.FloatField(blank=True)

class User(models.Model): # 유저 모델
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)
    age = models.IntegerField(null=True)
    GENDERS = (
        ('M', '남성'),
        ('W', '여성'),
    )
    gender = models.CharField(verbose_name='성별', max_length=2, choices=GENDERS, default = '')
    date = models.DateField(null=True)
    time = models.TimeField(null=True)


class Input(models.Model): # 처음 입력 모델
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)
    startperiod = models.DateTimeField(null=True)
    endperiod = models.DateTimeField(null=True)
    area = models.CharField(max_length=20)
    def __str__(self):
        return self.tag

class Tour(models.Model): # 관광지 모델
    name = models.CharField(max_length=30)
    tourTime = models.IntegerField(null=True)
    tourLatitue = models.FloatField(blank=True)
    tourLongitude = models.FloatField(blank=True)
    tour_url = models.URLField('관광지 URL', max_length=400, blank=True,null=True,default='')
    image_file = models.ImageField('관광지 이미지', upload_to='tours', blank=True, null=True)
    cnt = models.IntegerField(null=True)

class Restaurant(models.Model): # 식당 모델
    name = models.CharField(max_length = 20)
    restaurantTime = models.IntegerField(null=True)
    restaurantLatitue = models.FloatField(blank=True)
    restaurantLognitude = models.FloatField(blank=True)
    restaurant_url = models.URLField('식당 URL', max_length=400, blank=True,null=True,default='')
    image_file = models.ImageField('식당 이미지', upload_to='restaurants', blank=True, null=True)


class Stay(models.Model): # 숙소 모델
    name = models.CharField(max_length=20)
    stayLatitue = models.FloatField(blank=True)
    stayLognitude = models.FloatField(blank=True)
    restaurant_url = models.URLField('숙소 UR', max_length=400, blank=True,null=True, default='')
    image_file = models.ImageField('숙소 이미지', upload_to='stays', blank=True, null=True)


class Schedule(models.Model): # 일정리스트 모델
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)
    tour = models.ManyToManyField(Tour, blank=True)
    restaurant = models.ManyToManyField(Restaurant, blank=True)
    stay = models.ManyToManyField(Stay, blank=True)
