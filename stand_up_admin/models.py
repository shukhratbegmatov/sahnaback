from django.db import models
class Menu(models.Model):
    title = models.CharField(verbose_name="Title",max_length=50,blank=True, null=True)
    link=models.CharField(max_length=100)

    def __str__(self):
            return self.title



class Comic(models.Model):
     first_name=models.CharField(max_length=100,blank=True, null=True)
     last_name=models.CharField(max_length=100,blank=True, null=True)
     bio=models.TextField(max_length=1000,blank=True, null=True)
     telegram=models.CharField(max_length=100,blank=True, null=True)
     instagram=models.CharField(max_length=100,blank=True, null=True)
     images=models.ImageField(upload_to='files/covers',unique=True, null=True,help_text='Image')



     def __str__(self):
             return self.first_name

class Banner(models.Model):
     name=models.CharField(max_length=100,blank=True, null=True)
     description=models.TextField(max_length=100,blank=True, null=True)
     type=models.CharField(max_length=100,blank=True, null=True)
     price=models.CharField(max_length=100,blank=True, null=True)
     url=models.CharField(max_length=100,blank=True, null=True)
     date_time=models.CharField(max_length=100,blank=True, null=True)
     images=models.ImageField(upload_to='files/covers',unique=True, null=True,help_text='Image')
     status=models.BooleanField(default=True)
     comic=models.ForeignKey(
             Comic, on_delete=models.PROTECT, default=1
             )


     def __str__(self):
             return self.name

class Partner(models.Model):
     name=models.CharField(max_length=100,blank=True, null=True)
     url=models.CharField(max_length=100,blank=True, null=True)
     images=models.ImageField(upload_to='files/covers',unique=True, null=True,help_text='Image')

     def __str__(self):
             return self.name
# Create your models here.

class Food(models.Model):
     name=models.CharField(max_length=100,blank=True, null=True)
     description=models.CharField(max_length=100,blank=True, null=True)
     price = models.DecimalField(max_digits=10, decimal_places=2)

     def __str__(self):
             return self.name


class About(models.Model):
     title=models.CharField(max_length=100,blank=True, null=True)
     description=models.TextField(max_length=100,blank=True, null=True)
     address=models.CharField(max_length=100,blank=True, null=True)
     work_time=models.CharField(max_length=100,blank=True, null=True)
     phone=models.CharField(max_length=100,blank=True, null=True)
     messenger_url=models.CharField(max_length=100,blank=True, null=True)


     def __str__(self):
             return self.title



class Drink_Category(models.Model):
     title=models.CharField(max_length=100,blank=True, null=True)


     def __str__(self):
             return self.title


class Drink(models.Model):
     title=models.CharField(max_length=100,blank=True, null=True)
     description=models.TextField(max_length=100,blank=True, null=True)
     price=models.CharField(max_length=100,blank=True, null=True)
     category=models.ForeignKey(
                  Drink_Category, on_delete=models.PROTECT, default=1
                  )

     def __str__(self):
             return self.title



class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name