from django.db import models

class shoe(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=150)
    cat=models.CharField(max_length=150)
    size=models.CharField(max_length=150)
    color=models.CharField(max_length=150)
    price=models.IntegerField()
    image=models.FileField(upload_to='images',null=True)


    class Meta:
        db_table='shoex_table'
