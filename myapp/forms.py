from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.TextField()
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    quantity = forms.IntegerField()
    date_added = forms.DateField(auto_now_add=True)

# форму для редактирования товаров в базе
# данных, Измените модель продукта, добавьте поле для хранения
# фотографии продукта.
# Создайте форму, которая позволит сохранять фото.
