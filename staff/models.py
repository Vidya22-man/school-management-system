from django.db import models
import uuid


GENDER_CHOICES=(
    ('Male','Male'),
    ('Female','Female'),)

QULIFICATION_CHOICES=(
('B.A,B.Ed - Marathi','B.A,B.Ed - Marathi'),
('B.A,B.Ed - Hindi','B.A,B.Ed - Hindi'),
('B.A,B.Ed - English','B.A,B.Ed - English'),
('B.Sc,B.Ed- Maths','B.Sc,B.Ed- Maths'),
('B.Sc,B.Ed- Science','B.Sc,B.Ed- Science'),
('B.Sc,B.E/B.Tech- IT','B.Sc,B.E/B.Tech- IT'),
('B.A,B.Ed - History','B.A,B.Ed - History'),
('BFA,A.T.D / G.D Art-Art','BFA,A.T.D / G.D Art-Art'),('12th Pass','12th Pass'),)

ROLE_CHOICES=(
('Teaching', 'Teaching'),
    ('Non-Teaching', 'Non-Teaching'),)

NON_TEACHING_CHOICES = (
    ('Clerk', 'Clerk'),
    ('Accountant', 'Accountant'),
    ('Peon', 'Peon'),
    ('Librarian', 'Librarian'),
    ('Principal', 'Principal'),
)
SUBJECT_CHOICES=(
('Marathi ','Marathi '),('English','English'),('Hindi','Hindi'),('Mathematics','Mathematics'),('Science & Technology','Science & Technology'),
('History','History'),('Civics','Civics'),('Geography','Geography'),('Art Education','Art Education'),)

STATUS_CHOICES=(
('Active',"Active"),('Inactive','Inactive'),('Retired','Retired'),)



# Create your models here.
class Staff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_id=models.CharField(max_length=100,null=True,blank=True,help_text='emp101')
    full_name=models.CharField(max_length=150,null=True,blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    gender=models.CharField(max_length=12,choices=GENDER_CHOICES,default='Male')
    birth_date=models.DateField()
    address=models.CharField(max_length=150)
    email=models.EmailField()
    mobile_no=models.CharField(max_length=15)
    qualification=models.CharField(max_length=150,choices=QULIFICATION_CHOICES)
    experience = models.PositiveIntegerField(help_text="In Years")
    joining_date=models.DateField()
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    subject=models.CharField(max_length=150,choices=SUBJECT_CHOICES,blank=True,null=True)
    designation =models.CharField(max_length=150,choices=NON_TEACHING_CHOICES,blank=True,null=True)
    status=models.CharField(max_length=150,choices=STATUS_CHOICES,null=True,blank=True)
    profile_image=models.ImageField(upload_to='Staff_images',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural="Staff"

ATTENDANCE_STATUS = (
    ('Present', 'Present'),
    ('Absent', 'Absent'),
    ('Leave', 'Leave'),
    ('Half Day', 'Half Day'),
)

class StaffAttendance(models.Model):
    staff=models.ForeignKey(Staff,on_delete=models.CASCADE,related_name='attendance')
    date=models.DateField()
    status=models.CharField(max_length=150,choices=ATTENDANCE_STATUS,null=True,blank=True)
    remark=models.CharField(max_length=150,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.staff.full_name} -{self.date}- {self.status}"

    class Meta:
        unique_together=('staff','date')      # same staff same date duplicate entry nahi