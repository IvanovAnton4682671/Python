
from django.db import models


class Users(models.Model):
    type = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=32)


class Subjects(models.Model):
    name_subject = models.CharField(max_length=30)
    id_creator = models.IntegerField()


class Teachers(models.Model):
    surname_teacher = models.CharField(max_length=30)
    name_teacher = models.CharField(max_length=30)
    patronymic_teacher = models.CharField(max_length=30)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name="teachers")
    id_creator = models.IntegerField()


class Listeners(models.Model):
    surname_listener = models.CharField(max_length=30)
    name_listener = models.CharField(max_length=30)
    patronymic_listener = models.CharField(max_length=30)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name="listeners")
    id_creator = models.IntegerField()


class AcademicRecords(models.Model):
    surname_listener = models.CharField(max_length=30)
    name_listener = models.CharField(max_length=30)
    patronymic_listener = models.CharField(max_length=30)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, related_name="academic_records")
    mark = models.IntegerField()
    id_creator = models.IntegerField()


class Group1(models.Model):
    surname_listener = models.CharField(max_length=30)
    name_listener = models.CharField(max_length=30)
    patronymic_listener = models.CharField(max_length=30)
    listener = models.ForeignKey(Listeners, on_delete=models.CASCADE, related_name="group1")
    id_creator = models.IntegerField()


class Group2(models.Model):
    surname_listener = models.CharField(max_length=30)
    name_listener = models.CharField(max_length=30)
    patronymic_listener = models.CharField(max_length=30)
    listener = models.ForeignKey(Listeners, on_delete=models.CASCADE, related_name="group2")
    id_creator = models.IntegerField()


class Group3(models.Model):
    surname_listener = models.CharField(max_length=30)
    name_listener = models.CharField(max_length=30)
    patronymic_listener = models.CharField(max_length=30)
    listener = models.ForeignKey(Listeners, on_delete=models.CASCADE, related_name="group3")
    id_creator = models.IntegerField()


class Group4(models.Model):
    surname_listener = models.CharField(max_length=30)
    name_listener = models.CharField(max_length=30)
    patronymic_listener = models.CharField(max_length=30)
    listener = models.ForeignKey(Listeners, on_delete=models.CASCADE, related_name="group4")
    id_creator = models.IntegerField()


class Group5(models.Model):
    surname_listener = models.CharField(max_length=30)
    name_listener = models.CharField(max_length=30)
    patronymic_listener = models.CharField(max_length=30)
    listener = models.ForeignKey(Listeners, on_delete=models.CASCADE, related_name="group5")
    id_creator = models.IntegerField()
