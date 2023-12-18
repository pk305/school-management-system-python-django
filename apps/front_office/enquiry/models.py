from django.db import models


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    address = models.TextField()
    reference = models.CharField(max_length=20)
    date = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    follow_up_date = models.DateTimeField()
    note = models.TextField()
    source = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    assigned = models.CharField(max_length=100)
    school_class = models.IntegerField()
    no_of_child = models.CharField(max_length=11)
    status = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "enquiries"

    def __str__(self):
        return self.name
