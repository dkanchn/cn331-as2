from django.utils import timezone
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# โมเดลสำหรับข้อมูลวิชา
class Course(models.Model):
    code = models.CharField(max_length=10)  # รหัสวิชา
    name = models.CharField(max_length=100)  # ชื่อวิชา
    semester = models.CharField(max_length=10)  # ภาคการศึกษา (เช่น 1/2564)
    year = models.IntegerField()  # ปีการศึกษา
    #seats = models.IntegerField()  # จำนวนที่นั่ง
    seats = models.IntegerField(default=0)
    available_seats = models.IntegerField()
    #available_seats = models.IntegerField(default=0)
    available = models.BooleanField(default=True)  # เพิ่มฟิลด์นี้

    def __str__(self):
        return f"{self.code} - {self.name}"
    
    def refund_seat(self):
        """คืนที่นั่งเมื่อมีการยกเลิกคำร้องขอโควต้า"""
        self.available_seats += 1
        self.save()

# โมเดลสำหรับการขอโควต้า
#class QuotaRequest(models.Model):
#    STATUS_CHOICES = [
#        ('pending', 'Pending'),
#        ('approved', 'Approved'),
#        ('denied', 'Denied'),
#    ]
    
#    student = models.ForeignKey(User, on_delete=models.CASCADE)  # เชื่อมกับ User (ซึ่งในระบบคือ student)
#    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # เชื่อมกับ Course (วิชาที่ขอโควต้า)
#    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')  # สถานะการขอโควต้า (รอการพิจารณา, อนุมัติ, ปฏิเสธ)

#    def __str__(self):
#        return f"{self.student.username} - {self.course.code} ({self.status})"
    
class QuotaRequest(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)  # ตรวจสอบว่าได้ import User
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending')
    created_at = models.DateTimeField(default=timezone.now)
