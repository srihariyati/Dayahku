from django.db import models
# Create your models here.

from django.db import models

class Tugas(models.Model):
	judul_tugas = models.CharField('Judul Tugas', max_length=50)
	deskripsi_tugas = models.CharField('Deskripsi Tugas', max_length =100)
	batas_waktu = models.DateField("Batas Waktu")
	input_file = models.FileField('File')

	def __str__(self):
		return self.judul_tugas

class Materi(models.Model):
	judul_materi = models.CharField('Judul Matri', max_length=50)
	deskripsi_materi = models.CharField('Deskripsi Materi', max_length =100)
	input_file = models.FileField('File')

	def __str__(self):
    		return self.judul_materi
