# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - Knowledge of Things
"""

from flask import Blueprint

blueprint = Blueprint(
    'authentication_blueprint',
    __name__,
    url_prefix=''
)
