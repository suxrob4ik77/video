from django.db import models

class Fanlar(models.Model):
    title = models.CharField(max_length=50)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    yili = models.DateField()
    fanlar = models.ForeignKey('Fanlar', on_delete=models.CASCADE)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)
    photo = models.FileField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    video = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True, null=True)  # <-- Video maydoni qo‘shildi!

    def __str__(self):
        return f"{self.name} {self.surname} {self.lastname} - {self.yili} - {self.phone} - {self.email}"


    # class Student(models.Model):
#     name = models.CharField(max_length=50)
#     surname = models.CharField(max_length=50)
#     lastname = models.CharField(max_length=50)
#     phone = models.CharField(max_length=15)
#     address = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     yili= models.DateField()
#     fanlar = models.ForeignKey(Fanlar, on_delete=models.CASCADE)
#     created_ed = models.DateTimeField(auto_now_add=True)
#     updated_ed = models.DateTimeField(auto_now=True)
#     photo = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True, null=True)
#
#     def __str__(self):
#         return f"{self.name} {self.surname} {self.lastname} - {self.yili} - {self.phone} - {self.email}"
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['-created_ed']

