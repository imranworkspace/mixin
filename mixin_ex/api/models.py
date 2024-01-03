from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=15)
    email=models.EmailField()

    class Meta:
        db_table='stud'
    def __str__(self) -> str:
        return self.name