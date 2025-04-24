from authlib.integrations.django_oauth2 import ResourceProtector
from . import validator
from django.conf import settings

require_auth = ResourceProtector()
api_validator = validator.Auth0JWTBearerTokenValidator(
        settings.AUTH0_DOMAIN,
        settings.AUTH0_AUDIENCE
)
require_auth.register_token_validator(api_validator)