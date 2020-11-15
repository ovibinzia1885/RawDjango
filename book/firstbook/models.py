from django.db import models


class licence(models.Model):
    name=models.CharField(max_length=240,blank=False)
    email=models.EmailField(unique=True,max_length=250)
    postcode=models.CharField(max_length=250)
    type=models.CharField(max_length=250)
    ammount=models.CharField(max_length=222)
    payment=models.CharField(max_length=250)

    def __str__(self):
        return self.name
class application (models.Model):
    name=models.CharField(blank=False,max_length=240)
    phone=models.CharField(max_length=24)
    postcode=models.CharField(max_length=23)
    type=models.CharField(max_length=250)
    price=models.CharField(max_length=250)
    payment=models.CharField(max_length=250)

    def __str__(self):
        return self.name
class Apply(models.Model):
    throwby = models.CharField(max_length=300)
    a_name = models.CharField(max_length=100)
    a_email = models.EmailField()
    a_phone = models.PositiveIntegerField()
    a_type = models.CharField(max_length=100)
    a_adress = models.CharField(max_length=100)
    a_ward= models.PositiveIntegerField()
    a_messur= models.CharField(max_length=100)
    a_pyment = models.CharField(max_length=100)
    list_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.a_name


class FilesAdmin(models.Model):
	adminupload=models.FileField(upload_to='media')
	title=models.CharField(max_length=50)

	def __str__(self):
		return self.title


