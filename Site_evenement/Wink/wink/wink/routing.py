from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack 
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator



from .consumers import ChatConsumer 
application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        AllowedHostsOriginValidator(
            URLRouter(
                [
                    url(r'profil/Chat/idUser=(?P<idUser>[0-9]+)/$', ChatConsumer()),
                ]
            )
        )
    )
})