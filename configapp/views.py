from django.contrib.auth import authenticate, login
from django.contrib import messages
import qrcode
from io import BytesIO
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *

def index(request):
    student = Student.objects.all()
    fanlar = Fanlar.objects.all()
    context = {
        'student': student,
        'fanlar': fanlar,
        'title': 'Students',
    }
    return render(request, "index.html", context)



def student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    context = {
        'student': student
    }
    return render(request, 'student.html', context)

def fanlar(request, fanlar_id):
    fanlar = get_object_or_404(Fanlar, id=fanlar_id)
    context = {
        'fanlar': fanlar
    }
    return render(request, 'fanlar.html', context)

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)  # <-- request.FILES qo‘shildi!
        if form.is_valid():
            form.save()
            messages.success(request, "Talaba muvaffaqiyatli qo‘shildi!")
            return redirect('index')
        else:
            messages.error(request, "Xatolik yuz berdi, iltimos tekshirib qaytadan urinib ko‘ring.")
    else:
        form = StudentForm()

    return render(request, 'add.html', {'form': form})

# def add(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Talaba muvaffaqiyatli qo‘shildi!")
#             return redirect('index')
#         else:
#             messages.error(request, "Xatolik yuz berdi, iltimos tekshirib qaytadan urinib ko‘ring.")
#
#     else:
#         form = StudentForm()
#
#     return render(request, 'add.html', {'form': form})
#


def generate_student_pdf(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{student.name}_info.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter


    p.setFont("Helvetica-Bold", 16)
    p.drawString(200, height - 50, "Student Ma'lumotlari")


    p.setFont("Helvetica", 12)
    p.drawString(100, height - 100, f"Ismi: {student.name}")
    p.drawString(100, height - 120, f"Familyasi: {student.surname}")
    p.drawString(100, height - 140, f"Yoshi: {student.yili}")
    p.drawString(100, height - 160, f"Email: {student.email}")
    p.drawString(100, height - 180, f"Fanlar: {student.fanlar}")


    if student.photo:
        student_image_path = student.photo.path
        student_img = ImageReader(student_image_path)
        p.drawImage(student_img, 100, height - 400, width=150, height=180)


    telegram_url = "https://t.me/najottalim"
    qr = qrcode.make(telegram_url)
    qr_io = BytesIO()
    qr.save(qr_io)
    qr_io.seek(0)


    qr_image = ImageReader(qr_io)
    p.drawImage(qr_image, 300, height - 400, width=150, height=150)

    p.showPage()
    p.save()

    return response

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
    else:
        form=UserLoginForm()
    return render(request,'login.html',{'form':form})


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)  # <-- `news` emas, `student`
    student.delete()
    messages.success(request, "Talaba muvaffaqiyatli o‘chirildi!")
    return redirect('index')

# def delete_news(request, student_id):
#     news = get_object_or_404(Student, id=student_id)  # News modelidan ob'ektni olish
#     news.delete()
#     messages.success(request, "Yangilik o‘chirildi!")
#     return redirect('index')