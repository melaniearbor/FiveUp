from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm, UserChangeForm as AuthUserChangeForm
from django import forms

from fuauth.models import User

class FUserCreationForm(forms.ModelForm):
	password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['name', 'email', 'phone_number', 'carrier', 'user_timezone', 
		'is_staff', 'is_active', 'receive_newsletter']

	def clean_password2(self):
		password1= self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			msg = "Passwords don't match"
			raise forms.ValidationError("Password mismatch")
		return password2

	def save(self, commit=True):
		user = super(FUserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user

# class FUserCreationForm(AuthUserCreationForm):

# 	#TODO - Determine if newsletter line is needed
# 	receive_newsletter = forms.BooleanField(required=False)

# 	class Meta:
# 		model = User
# 		fields = ['name', 'email', 'phone_number', 'carrier', 'user_timezone', 
# 		'is_staff', 'is_active', 'receive_newsletter']

# 	# def clean_username(self):
# 	# 	username = self.cleaned_data['username']
# 	# 	try:
# 	# 		User.default_manager.get(username=username)
# 	# 	except User.DoesNotExist:
# 	# 		return username
# 	# 	raise forms.ValidationError(
# 	# 		self.error_messages['duplicate_username'],
# 	# 		code='duplicate_username',
# 	# 	)

	# def is_valid(self):
	# 	import ipdb; ipdb.set_trace()

# class FUserChangeForm(AuthUserChangeForm):

# 	#TODO - Determine if newsletter line is needed
# 	receive_newsletter = forms.BooleanField(required=False)

# 	class Meta:
# 		model = User
# 		fields = ['name', 'email', 'phone_number', 'carrier', 'user_timezone', 
# 		'is_staff', 'is_active', 'receive_newsletter']


		