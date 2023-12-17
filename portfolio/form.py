import datetime

from django import forms
from portfolio.models import Order


class OrderFrom(forms.ModelForm):
    purpose1 = forms.ChoiceField(widget=forms.Select,
                                 choices=Order.type_choices)

    class Meta:
        model = Order
        fields = ["name", "phone_number", "email", "vk_url", "is_vk_answer", "message", "purpose1"]
        labels = {
            "name": "Имя и фамилия",
            "phone_number": "Номер телефона (необязательно)",
            "email": "Email",
            "vk_url": "Ссылка на вк (необязательно)",
            "is_vk_answer": "Отвечать в вк?",
            "message": "Сообщение",
        }
        widgets = {
            "name": forms.TextInput(attrs={
                'placeholder': 'Комолов Тимур', 'required': 'required',
                "id": "name"
            }),
            "phone_number": forms.TextInput(attrs={
                "type": "tel", 'placeholder': '+7-900-000-00-00',
                "maxlength": '16', "minlength": "11",
                "id": "phone"
            }),
            "email": forms.TextInput(attrs={
                "type": "email", 'placeholder': 'komolov.timurka@mail.ru', 'required': 'required',
                "id": "mail"

            }),
            "vk_url": forms.TextInput(attrs={
                "type": "url", 'placeholder': 'https://vk.com/timik232',
                "id": "vk"
            }),
            "is_vk_answer": forms.CheckboxInput(attrs={
                "id": "is_vk_answer",
            }),
            "message": forms.Textarea(attrs={
                'placeholder': 'Введите сообщение', 'required': 'required',
                "rows": "10",
                "cols": "70",
                "minlength": "10",
                "maxlength": "5000",
                "id": "message"
            }),
            "purpose1": forms.Select(attrs={"id": "topic"})
        }

    def __str__(self):
        vk_url = self.cleaned_data.get('vk_url', '')
        phone_number = self.cleaned_data.get('phone_number', '')
        is_vk = self.cleaned_data.get('is_vk_answer', '')
        purpose_label = dict(self.fields['purpose1'].choices).get(self.cleaned_data['purpose1'])
        return (f"Поступило сообщение в {datetime.datetime.now().strftime('%H:%M:%S %d:%m:%Y')}\n"
                f"Имя и фамилия: {self.cleaned_data.get('name', '')},\n"
                f"Email: {self.cleaned_data.get('email', '')},\n"
                f"Страница ВК: {'не указана' if vk_url is None else vk_url}\n"
                f"Телефон: {'не указан' if phone_number is None else phone_number},\n"
                f"Отвечать в вк: {'да' if is_vk else 'нет'},\n"                
                f"Цель: {purpose_label}\n"
                f"Сообщение: {self.cleaned_data.get('message', '')}")

    def get_purpose_label(self):
        return dict(self.fields['purpose1'].choices).get(self.cleaned_data['purpose1'])

