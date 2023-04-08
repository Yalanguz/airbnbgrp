from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userProfil(models.Model):
    user=models.OneToOneField(User, verbose_name=(""), on_delete=models.CASCADE)
    name=models.CharField(("isim"), max_length=50)
    surname=models.CharField(("soyisim"), max_length=50)
    username=models.CharField(("kullanıcı adı"), max_length=50)
    katilim=models.DateTimeField(("katılma tarihi"), auto_now=False, auto_now_add=False)
    profil_image=models.FileField(("profil foto"), upload_to=None, max_length=100) 
    phone=models.IntegerField(("telefon numarası"))
    
    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    name =models.CharField(("Kategori İsmi"), max_length=50)
    cimage = models.FileField(("kategori ico"), upload_to=None, max_length=100,null=True)


    def __str__(self) -> str:
        return self.name
    
class House(models.Model):
    ev_sahibi=models.ForeignKey(User, verbose_name=("Ev Sahibi"), on_delete=models.CASCADE)
    ev_ismi=models.CharField(("Ev Adı"), max_length=50)
    ülke=models.CharField(("Ülke"), max_length=50)
    lokasyon=models.TextField(("Konum Bilgisi"))
    yayin_tarihi=models.DateTimeField(("Yayın Tarihi"), auto_now=False, auto_now_add=False)
    foto_1=models.FileField(("Ev Foto1"), upload_to=None, max_length=100)
    foto_2=models.FileField(("Ev Foto2"), upload_to=None, max_length=100)
    foto_3=models.FileField(("Ev Foto3"), upload_to=None, max_length=100)
    günlük_ücret=models.FloatField(("Günlük Ücret"))
    kategori=models.ForeignKey(Category, verbose_name=("Kategori"), on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.ev_ismi