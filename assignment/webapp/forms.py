from django import forms  


class IFSC_Form(forms.Form):
    ifsc_field = forms.CharField(label='IFSC: ', max_length=100)

class BNAME_BCITY_Form(forms.Form):
    bname_field = forms.CharField(label='Bank Name: ', max_length=100)
    bcity_field = forms.CharField(label='City: ', max_length=100)

