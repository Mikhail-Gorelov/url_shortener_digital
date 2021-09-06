from django import forms

from shortener.models import URL
from shortener.validators import validate_short_url


class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ['url', 'short_url']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['short_url'].validators = [validate_short_url]

    def save(self, commit=True, session_key=None):
        self.instance.session = session_key
        return super().save(commit=commit)
