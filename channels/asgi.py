"""
ASGI config for channels project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path,re_path
from ch import consumer
from channels.auth import AuthMiddlewareStack
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "channels.settings")
application=get_asgi_application()

ws_pattern=[path("ws/main/",consumer.MainConsumer.as_asgi())]
application = ProtocolTypeRouter(
    {  "websocket":({
        URLRouter(ws_pattern)}
        # Just HTTP for now. (We can add other protocols later.)
)}
)