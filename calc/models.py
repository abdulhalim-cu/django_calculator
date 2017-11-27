from django.db import models


class MediaType(models.Model):
    media_type = models.CharField(max_length=60)

    class Meta:
        db_table = '"calc_mediatype"'

    def __str__(self):
        return self.media_type


class CustomerType(models.Model):
    customer_type = models.CharField(max_length=60)

    class Meta:
        db_table = '"calc_customertype"'

    def __str__(self):
        return  self.customer_type


class SquareFeetRange(models.Model):
    media = models.ForeignKey(MediaType, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerType, on_delete=models.CASCADE)
    square_feet = models.CharField(max_length=60)
    cost_per_sqft = models.FloatField()

    class Meta:
        db_table = '"calc_squarefeetrange"'

    def __str__(self):
        return str(self.cost_per_sqft)

