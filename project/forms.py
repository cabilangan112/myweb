from django import forms
from .models import ItemLost, LocationLost, OwnerInfo, ReturnerInfo

class LostUpdateForm(forms.ModelForm):
	class Meta:
		model = ItemLost
		fields = [
			'Category',
			'Item_name',
			'Item_description',
			'Location',
			'Owner',
			'Returned',
			'Returner',

			
		]
	def __init__(self, User=None, *args, **kwargs):
		super(LostUpdateForm, self).__init__(*args, **kwargs)
		self.fields['Location'].queryset = LocationLost.objects.all()
		self.fields['Owner'].queryset = OwnerInfo.objects.all()


	def __init__(self, User=None, *args, **kwargs):
		super(LostUpdateForm, self).__init__(*args, **kwargs)
		self.fields['Location'].queryset = LocationLost.objects.all()
		self.fields['Owner'].queryset = OwnerInfo.objects.all()

	def save(self, commit=True):
		#Save the provided password in hashed format
		User = super(LostUpdateForm, self).save(commit=False)

		if commit:
			User.save()
			#create a new user hash for activating email
			User.send_claim_email()
			
		return user