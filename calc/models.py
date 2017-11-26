from django.db import models


class MediaType(models.Model):
    media_type = models.CharField(max_length=60)

    def __str__(self):
        return self.media_type


class CustomerType(models.Model):
    customer_type = models.CharField(max_length=30)

    def __str__(self):
        return  self.customer_type


class SquareFeetRange(models.Model):
    media = models.ForeignKey(MediaType, on_delete=models.CASCADE)
    customer = models.ForeignKey(CustomerType, on_delete=models.CASCADE)
    square_feet = models.CharField(max_length=50)
    cost_per_sqft = models.FloatField()

    def __str__(self):
        return self.square_feet

# class CustomerType(models.Model):
#     CUSTOMER_TYPE_CHOICES = (
#         ('cl', 'Client'),
#         ('re', 'Regular'),
#         ('ad', 'Ad. Farm'),
#     )
#     SQUARE_FEET_CHOICES = (
#         ('1-100', '01-100'),
#         ('101-200', '101-200'),
#         ('201-300', '201-300'),
#         ('301-400', '301-400'),
#         ('401-500', '401-500'),
#         ('500+', '500+'),
#     )
#     type = models.CharField(max_length=2, choices=CUSTOMER_TYPE_CHOICES)
#     square_feet = models.CharField(max_length=7, choices=SQUARE_FEET_CHOICES)
#     cost = models.FloatField()
#     media_type = models.ForeignKey('MediaTypes',
#                                    on_delete=models.CASCADE,
#                                    verbose_name='Media Type')

#     def __str__(self):
#         return self.type, self.square_feet, self.media_type, self.cost


# class TestDB(models.Model):
#     name = models.CharField(max_length=23)
#
#     def __str__(self):
#         return self.name
