from django.urls import reverse_lazy
from django.views import generic
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'




from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, CustomUser
from .serializers import CustomUserSerializer
from rest_framework.generics import get_object_or_404


class CustomUserView(APIView):
    def get(self, request):
        articles = CustomUser.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = CustomUserSerializer(articles, many=True)
        return Response({"articles": serializer.data})

    def post(self, request):
        article = request.data.get('article')
        # Create an article from the above data
        serializer = CustomUserSerializer(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({"success": "CustomUser '{}' created successfully".format(article_saved.email)})

    def put(self, request, pk):
        saved_article = get_object_or_404(CustomUser.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = CustomUserSerializer(instance=saved_article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({
            "success": "CustomUser '{}' updated successfully".format(article_saved.email)
        })