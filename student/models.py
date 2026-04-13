from django.db import models
import uuid
from datetime import date


GENDER_CHOICES=(
('Male','Male'),
('Female','Female'),
)

STANDARD_CHOICES=(
('5th','5th'),
('6th','6th'),
('7th','7th'),('8th','8th'),('9th','9th'),('10th','10th'),
)
ENROLLMENT_STATUS_CHOICES=(
('active','Active'),
('inactive','Inactive'),
('graduated','Graduated'),
('transferred','Transferred'),
('dropped','Dropped'),
)

RELIGION_CHOICES=(
('Hindu','Hindu'),('Christian','Christian'),('Buddhist','Buddhist'),('Jain','Jain'),('Others','Others'),
)


# Create your models here.
CASTE_CHOICES=(
    ('SC','SC'),('ST','ST'),('OBC','OBC'),('OTHER','OTHER'),
)

OCCUPATION_CHOICES=(
('Farmer','Farmer'), ('Teacher','Teacher'),('Doctor','Doctor'),('Engineer','Engineer'),('Govt Employee','Govt Employee'),
('Pvt Employee','PvtEmployee'),('Businessman','Businessman'),('Shopkeeper','Shopkeeper'),('Driver','Driver'),('Police Officer','Police Officer'),('Army','Army'),('Lawyer','Lawyer'),('Accountant','Accountant'),('Labour','Labour'),('Self Employed','Self Employed'),('Homemaker','Homemaker'),('Retired','Retired'),('Unemployed','Unemployed'),)


class Father(models.Model):
    father_name=models.CharField(max_length=200)
    mother_name=models.CharField(max_length=200)
    birth_date=models.DateField()
    address=models.TextField()
    occupation=models.CharField(max_length=200,choices=OCCUPATION_CHOICES)
    mobile_no=models.CharField(max_length=20)
    caste=models.CharField(max_length=200,choices=CASTE_CHOICES)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.father_name

    class Meta:
        verbose_name_plural='Father'


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    father=models.ForeignKey(Father,on_delete=models.CASCADE,related_name="students")
    birth_date=models.DateField('Birth Date')
    caste=models.CharField(max_length=150,choices=CASTE_CHOICES)
    gender=models.CharField(max_length=20,choices=GENDER_CHOICES,default="M")
    religion=models.CharField(max_length=50,choices=RELIGION_CHOICES)
    standard=models.CharField(max_length=150,choices=STANDARD_CHOICES)
    enrollment_status=models.CharField(max_length=150,choices=ENROLLMENT_STATUS_CHOICES)
    photo=models.ImageField(upload_to='Students_images',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    class Meta:
        verbose_name_plural="Student"

