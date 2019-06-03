from django import template
from django.contrib.staticfiles.storage import staticfiles_storage
from django.utils.safestring import mark_safe
from django.urls import reverse_lazy
from myshop.settings import TIME_ZONE
import pytz

register = template.Library()


@register.filter(expects_localtime=True)
def comment_card(comment, is_manager=True):
    if comment.user.extended.avatar:
        url = comment.user.extended.avatar.url
    else:
        url = staticfiles_storage.url('images/no_avatar.png')
    if is_manager:
        profile = reverse_lazy('auth:manager_user_detail', kwargs={'pk': comment.user.pk})
    else:
        profile = reverse_lazy('auth:customer_user_detail', kwargs={'pk': comment.user.pk})
    return mark_safe(f'''<div class="clearfix border border-secondary rounded py-1 mt-1">
            <div class="float-left px-3">
                    <img src="{url}" style="width: 5rem">
            </div>
            <div class="px-3">
                <a href="{profile}"><strong>{comment.user.username}</strong></a><br>
                {comment.date_create.astimezone(pytz.timezone(TIME_ZONE)).strftime('%d.%m.%Y %H:%M')}
                <p>{comment.comment_text}</p>
            </div>
            <div>
                
            </div>

        </div>''')
