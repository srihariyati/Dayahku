from django import forms

class PostForm(forms.Form):
    judul   = forms.CharField(max_length=30)
    deskripsi = forms.CharField(
        widget = forms.Textarea
    )
    file = forms.FileField(
        label = 'Pilih File',
        help_text='File maksimal 2MB'
    )