from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=150)
    bic = models.CharField(max_length=150, blank=True)


class Contact(models.Model):
    company = models.ForeignKey(
        Company, related_name="contacts", on_delete=models.PROTECT)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField()


class Order(models.Model):
    order_number = models.CharField(max_length=150, db_index=True)
    company = models.ForeignKey(Company, related_name="orders",
                                on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, related_name="orders",
                                on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=18, decimal_places=9, db_index=True)
    order_date = models.DateTimeField(null=True, blank=True)
    # for internal use only
    added_date = models.DateTimeField(auto_now_add=True)
    # for internal use only
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.order_number}"
