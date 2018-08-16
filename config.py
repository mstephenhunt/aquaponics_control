"""Class-based application configuration."""

import os

class ConfigClass(object):
    """Flask configuration."""

    # Flask settings
    SECRET_KEY = "This is an INSECURE secret!! DO NOT use this in production!!"

    # Flask-User settings
    USER_APP_NAME = "fishprison"  # Shown in and email templates and footers
    USER_ENABLE_EMAIL = False    # Disable email authentication
    USER_ENABLE_USERNAME = True  # Enable username authentication
    USER_REQUIRE_RETYPE_PASSWORD = False    # Simplify register form

    # local settings
    LOCAL_PATH = os.path.dirname(__file__)

