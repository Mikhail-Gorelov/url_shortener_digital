from django.core.validators import RegexValidator, slug_re
from django.utils.translation import gettext_lazy as _


validate_short_url = RegexValidator(
    slug_re,
    _('Enter a valid “Short URL” consisting of letters, numbers, underscores or hyphens.'),
    'invalid'
)
