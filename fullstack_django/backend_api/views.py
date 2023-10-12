from django.shortcuts import render
from rest_framework.views import APIView
from .models import YouTubeVideo
from .serializer import YoutubeVideoSerializer  # Исправлен импорт
from rest_framework.response import Response

class YoutubeVideoView(APIView):  # Заменена ошибка с регистром
    def get(self, request):
        videos = YouTubeVideo.objects.all()  # Исправлена переменная (output -> videos)
        output = [
            {
                "title": video.title,  # Исправлено имя переменной (output -> video)
                "channel": video.channel  # Исправлено имя переменной (output -> video)
            } for video in videos
        ]
        return Response(output)
    
    def post(self, request):
        serializer = YoutubeVideoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):  # Исправлена опечатка (raise_exceptions -> raise_exception)
            serializer.save()
            return Response(serializer.data)
