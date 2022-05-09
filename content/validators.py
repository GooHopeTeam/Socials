import os
from django.core.exceptions import ValidationError
from django.core.files import File


def validate_file_extension(value: File) -> None:
    ext = os.path.splitext(value.name)[1]
    valid_ext = ('.jpg', '.png')

    if not ext.lower() in valid_ext:
        raise ValidationError('Unsupported file extension.')
