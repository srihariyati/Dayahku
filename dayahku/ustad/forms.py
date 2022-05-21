from dataclasses import fields
from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from dataclasses import fields
from logging import PlaceHolder


from .models import Tugas, Materi

class InputTugas(ModelForm):
	class Meta:
		model = Tugas
		fields =('judul_tugas', 'deskripsi_tugas', 'batas_waktu','input_file',)

		widgets={
			'judul_tugas' : forms.TextInput(
				attrs={
					'class' :'form-control',
				}),
			
			'deskripsi_tugas' : forms.Textarea(
				attrs={
					'class' : 'form-control',
				}),

			'batas_waktu' : forms.DateInput(
				attrs={
					'class' : 'form-control',
					'type'	: 'date',
				}
			),

			'input_file' : forms.FileInput(
				attrs={
					'class' : 'form-control',
				})
			
		}

class InputMateri(ModelForm):
	class Meta:
		model = Materi
		fields =('judul_materi', 'deskripsi_materi','input_file',)

		widgets={
			'judul_materi' : forms.TextInput(
				attrs={
					'class' :'form-control',
				}),
			
			'deskripsi_materi' : forms.Textarea(
				attrs={
					'class' : 'form-control',
				}),

			'input_file' : forms.FileInput(
				attrs={
					'class' : 'form-control',
				})
			
		}
