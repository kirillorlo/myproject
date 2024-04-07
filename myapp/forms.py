from django import forms
import datetime


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    quantity = forms.IntegerField()
    date_added = forms.DateField(widget=forms.HiddenInput, initial=datetime.date.today)

# форму для редактирования товаров в базе
# данных, Измените модель продукта, добавьте поле для хранения
# фотографии продукта.
# Создайте форму, которая позволит сохранять фото.
