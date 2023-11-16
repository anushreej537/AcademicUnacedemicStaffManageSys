from django.db import models


class Designation(models.Model):
    designation = models.CharField(max_length=250)
    is_classteacher = models.BooleanField(default=True)
    is_academic = models.BooleanField(default=True)
    is_nonacademic = models.BooleanField(default=True)


class User_registration(models.Model):
    usertype = models.CharField(max_length=250)
    names = models.CharField(max_length=250)
    contact = models.CharField(max_length=250, null=True,blank=True)
    email = models.EmailField(max_length=250)
    designation_master = models.ForeignKey(Designation,on_delete=models.CASCADE,null=True,blank=True)
    education = models.CharField(max_length=250,null=True,blank=True)
    joiningdate = models.DateField(null=True,blank=True)
    subject = models.CharField(max_length=250,null=True,blank=True)
    password = models.CharField(max_length=250)
    profileimg = models.ImageField(upload_to='pic',null=True,blank=True)

# class Result():
#     totalscore = models.FloatField()
#     number_of_subject = models.IntegerField()
#     score = models.FloatField()

# class Student(models.Model):
#     # sid 
#     sname = models.CharField(max_length=250)
#     scourse = models.ForeignKey(Academicstaff,on_delete=models.CASCADE)
#     classteacher = models.ForeignKey(Academicstaff,on_delete=models.CASCADE)
#     result_show= models.ForeignKey(Result,on_delete=models.CASCADE)
#     stuclass = models.CharField(max_length=2500)

# class subject_master(models.Model):
#     subname = models.CharField(max_length=250)
#     # subteacher = models.ForeignKey()

# class class_master(models.Model):
#     classes =models.CharField(max_length=250)
#     subject = models.ForeignKey(subject_master,on_delete=models.CASCADE)
#     teachernm= models.ForeignKey(Academicstaff,on_delete=models.CASCADE)

