from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


numbers = "1"


def validate_time(value):
    if not value in numbers:
        raise ValidationError(_("incorect time"))
    return value
