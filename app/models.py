from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User_profile(models.Model):
    USER_ID=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    age=models.IntegerField(null=True, blank=True)
    gender=models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    phone=models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address=models.TextField(blank=True)
    status=models.CharField(max_length=20, default='Active')


class Doctor(models.Model):
    USER_ID = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.TextField(max_length=255)
    status = models.CharField(max_length=20, default='Pending Approval')
    regno= models.CharField(max_length=50, unique=True)
    smc= models.CharField(max_length=50)


class Doctor_schedule(models.Model):
    DOCTOR_ID=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='schedules')
    date=models.CharField(max_length=100)
    start_time= models.CharField(max_length=100)
    end_time= models.CharField(max_length=100)
    fees= models.DecimalField(max_digits=8, decimal_places=2)
    max_patients = models.IntegerField(default=20)

class Booking(models.Model):
    PATIENT_ID=models.ForeignKey(User_profile,on_delete=models.CASCADE)
    shedule_id=models.ForeignKey(Doctor_schedule,on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    token_number = models.IntegerField(null=True, blank=True)

class Payment(models.Model):
    PAYMENT_ID= models.CharField(max_length=100)
    BOOKING_ID=models.ForeignKey(Booking,on_delete=models.CASCADE)
    amount= models.CharField(max_length=100)
    payment_date= models.CharField(max_length=100)
    status= models.CharField(max_length=100)

class Complaint(models.Model):
    USER_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    Complaint_text=models.TextField(max_length=500)
    Reply=models.TextField(max_length=500, blank=True, null=True)
    Date=models.CharField(max_length=100)

class Feedback(models.Model):
    PATIENT_ID = models.ForeignKey(User_profile, on_delete=models.CASCADE, null=True,blank=True)
    DOCTOR_ID = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True,blank=True)
    Feedback_text=models.TextField()
    Date=models.CharField(max_length=100)

class Chat(models.Model):
    SENDER_ID = models.ForeignKey(User,on_delete=models.CASCADE,related_name="sent_chats")
    RECIEVER_ID = models.ForeignKey(User,on_delete=models.CASCADE,related_name="received_chats")
    message = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='chat_images/', blank=True, null=True)
    timestamp = models.CharField(max_length=100)
    is_read = models.BooleanField(default=False)


class SkinChatMessage(models.Model):
    USER_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=[('user', 'User'), ('bot', 'Bot')])
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class SkinPredictionHistory(models.Model):
    USER_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    image_path = models.CharField(max_length=500)
    label = models.CharField(max_length=200)
    confidence = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    DOCTOR_ID = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    PATIENT_ID = models.ForeignKey('User_profile', on_delete=models.CASCADE,default='1')
    stars = models.IntegerField(default=0)  # 1 to 5
    review = models.TextField(max_length=500,default='pending')
    date = models.CharField(max_length=100)