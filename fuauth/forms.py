from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm, UserChangeForm as AuthUserChangeForm
from django import forms
from django.utils.translation import ugettext_lazy as _ 
from django.views.generic.edit import CreateView, ModelFormMixin


from fuauth.models import User

class AjaxTemplateMixin(object):
 
	def dispatch(self, request, *args, **kwargs):
		if not hasattr(self, 'ajax_template_name'):
			split = self.template_name.split('.html')
			split[-1] = '_inner'
			split.append('.html')
			self.ajax_template_name = ''.join(split)
		if request.is_ajax():
			self.template_name = self.ajax_template_name
		return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)

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

class PublicUserCreation(CreateView, ModelFormMixin): #AjaxTemplateMixin

    model = User
    template_name = 'index.html'
    success_url = '/signup-success/'
    fields = ['name', 'email', 'phone_number', 'carrier', 'user_timezone', 'password']
    labels = {
        'name': _('what can we call you? Pete? Cindy?'),
        'email': _('what\'s your email address?'),
        'phone_number': _('phone number:'), 
        'carrier': _('your mobile carrier'),
        'user_timezone': _('your time zone')
    }

    def form_valid(self, form):
        """
        If the form is valid, save the associated model.
        """
        new_user = form.save(commit=False)
        new_user.save()
        self.object = new_user

        return super(ModelFormMixin, self).form_valid(form)

 #    def get_absolute_url(self):
 #    	''' returns a reference for the added user '''
 #    	return reverse('signup-success')

	# # def get_absolute_url(self):
	# # 	''' returns a reference for the message'''
	# # 	# TODO Create message detail view
	# # 	return reverse('signup-success') #, kwargs={'pk': self.id} ?



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


