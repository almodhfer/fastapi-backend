import secrets
SECRET_KEY: str = secrets.token_urlsafe(32)
# 60 minutes * 24 hours * 8 days = 8 days
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
FIRST_SUPERUSER: str = "almodhfer"
FIRST_SUPERUSER_EMAIL: str = "mokhtarmodhfer@gmail.com"
FIRST_SUPERUSER_PASSWORD: str = "09620692"
API_V1_STR  = '/api'
EMAILS_ENABLED=False
