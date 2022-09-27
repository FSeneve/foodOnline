from django.core.exceptions import ValidationError
import os

def allow_only_images_validator(value):
      image_extension = os.path.splitext(value.name)[1]
      valid_extensions = ['.png', '.jpg', '.jpeg'] 

      if not image_extension.lower() in valid_extensions:
            raise ValidationError('Unsupported file extension. Allowed extensions: ' + str(valid_extensions))