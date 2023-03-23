# -*- coding: utf-8 -*-
from basedosdados_api.settings.base import *  # noqa

from django.utils.log import DEFAULT_LOGGING

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "api.sqlite3",  # noqa
    }
}

LOGGING = DEFAULT_LOGGING
