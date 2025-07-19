from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from .tasks import send_notification_email

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        book = serializer.save()
        send_notification_email.delay(book.title)
