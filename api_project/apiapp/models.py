from django.db import models

class EmployeeModel(models.Model):
    gender_list = [('M', 'Male'), ('F', 'Female')]
    designation_list = [('JE', 'Junior Engineer'), ('ER', 'Engineer'), ('TL', 'Team Lead'), ('PM', 'Project Manager'),
                        ('MG', 'Manager')]

    employee_id = models.IntegerField(primary_key=True)
    employee_name = models.CharField(max_length=25)
    gender = models.CharField(max_length=1, choices=gender_list)
    designation = models.CharField(max_length=2, choices=designation_list)
    mobile = models.BigIntegerField()
    salary = models.IntegerField()
