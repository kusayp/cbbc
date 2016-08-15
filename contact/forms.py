from django import forms

from .models import Contact

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['name', 'email', 'phone', 'is_prayer_request', 'content'] 
		widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Your Name'}), 
            'email': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Your Email'}), 
            'phone': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Your Mobile Number'}), 
            'is_prayer_request': forms.CheckboxInput(attrs={'class': 'form-control'}), 
            'content': forms.Textarea(attrs={'class': 'form-control', 'required': 'true', 'rows': '3=6', 'placeholder': 'Your Message'}),
        }
# 		fields = ['name', 'email', 'phone', 'is_prayer_request', 'content'] 

# class ContactForm(forms.Form):
# 	name = forms.CharField(label='Your name', max_length=100)
# 	email = forms.EmailField()
# 	phone = forms.CharField(label='phone', max_length=20)
# 	is_prayer_request = forms.BooleanField(label='Prayer Request?')
# 	content = forms.CharField(label='Content', widget=forms.Textarea())

# 	def save(self):
# 		# contacts = Contact(name=self.cleaned_data['name'], email=self.cleaned_data['email'], phone=self.cleaned_data['phone'], is_prayer_request=form.cleaned_data['is_prayer_request'], content=self.cleaned_data['content'])
# 		contacts = Contact()
# 		return contacts
# 	