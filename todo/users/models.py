from django.db import models


class SchemeData(models.Model):
    department_uid = models.CharField(max_length=255)
    department_name = models.CharField(max_length=255)
    scheme_uid = models.CharField(max_length=255, primary_key=True)
    scheme_name = models.CharField(max_length=255)
    year = models.CharField(max_length=50)
    quarter = models.CharField(max_length=50)
    total_indicators = models.IntegerField()
    ontrack_indicators = models.IntegerField()
    offtrack_indicators = models.IntegerField()
    notapplicable_indicators = models.IntegerField()
    target_achieved = models.BooleanField()
    scheme_status = models.CharField(max_length=255)
    budget_alloted = models.FloatField()
    budget_revised = models.FloatField()
    budget_utilized = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    budget_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'scheme_data'
