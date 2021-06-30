from django.contrib import admin

from profil.models import *

from django.core.paginator import Paginator
from django.core.cache import cache

@admin.register(Winker)
class WinkerAdmin(admin.ModelAdmin):
    pass

@admin.register(FilesWinker)
class FilesWinkerAdmin(admin.ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(FilesEvent)
class FilesEventAdmin(admin.ModelAdmin):
    pass

@admin.register(SignalerArticle)
class SignalerArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(RamenerEvent)
class RamenerEventAdmin(admin.ModelAdmin):
    pass

@admin.register(NotePlayer)
class NotePlayerAdmin(admin.ModelAdmin):
    pass

@admin.register(ReactionEvent)
class ReactionEventAdmin(admin.ModelAdmin):
    pass

@admin.register(PublicChatRoom)
class PublicChatRoomAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    search_fields = ['id','title']
    list_display = ['id',]

    class Meta:
        model = PublicChatRoom

# Modified version of a GIST I found in a SO thread
class CachingPaginator(Paginator):
    def _get_count(self):

        if not hasattr(self, "_count"):
            self._count = None

        if self._count is None:
            try:
                key = "adm:{0}:count".format(hash(self.object_list.query.__str__()))
                self._count = cache.get(key, -1)
                if self._count == -1:
                    self._count = super().count
                    cache.set(key, self._count, 3600)

            except:
                self._count = len(self.object_list)
        return self._count

    count = property(_get_count)

@admin.register(PublicChatRoomMessage)
class PublicChatRoomMessageAdmin(admin.ModelAdmin):
    list_display = ['eventComment', 'winkerComment','timestamp']
    list_display = ['eventComment','winkerComment','timestamp','message']
    search_fields = ['winkerComment__username','message']
    redonly_fields = ['id','winkerComment__username','eventComment','timestamp']

    show_full_result_count = False
    paginator = CachingPaginator

    class Meta:
        model = PublicChatRoomMessage
