from django.db import models
import uuid

def generate_unique_code():
    while True:
        code = str(uuid.uuid4())
        if User.objects.filter(id=code).count() == 0:
            break

    return code


# Create your models here.
class User(models.Model):
    id = models.CharField(primary_key=True,max_length=255, default=generate_unique_code)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    birthDate = models.DateTimeField()
    city = models.CharField(max_length=255)
    egn = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    accomodation = models.BooleanField(default=False)
    licensePlate = models.CharField(max_length=255)
    phoneNumber = models.CharField(max_length=255)

    def __str__(self):
        return self.firstName  + "  "+ self.lastName + "  " + self.city + "  " + str(self.accomodation)
    