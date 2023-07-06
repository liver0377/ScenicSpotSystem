from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class ScenicSpot(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="scenic_spots/")
    province = models.ForeignKey(Province, related_name="scenic_spots", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
