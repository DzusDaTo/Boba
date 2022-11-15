from django.http import StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Video
from .services import open_file
from video_hosting.models import Ip


def get_list_video(request):
    return render(request, 'index.html', {'video_list': Video.objects.all()})


# Метод для получения айпи
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')  # В REMOTE_ADDR значение айпи пользователя
    return ip


# Страница самого поста
def get_video(request, pk: int):
    _video = get_object_or_404(Video, id=pk)
    ip = get_client_ip(request)

    if Ip.objects.filter(ip=ip).exists():
        _video.views.add(Ip.objects.get(ip=ip))
    else:
        Ip.objects.create(ip=ip)
        _video.views.add(Ip.objects.get(ip=ip))
    return render(request, "video_hosting/video.html", {"video": _video})


def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response