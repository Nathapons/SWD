from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .serializers import EmailSerializer
from .models import EmailModel


class ComposeEmail(generics.ListCreateAPIView):
    queryset = EmailModel.objects.all()
    serializer_class =EmailSerializer

    def post(self, request):
        to_mail = request.data.get('to_mail', None)
        topics = request.data.get('topics', None)
        mail_detail = request.data.get('mail_detail', None)

        if not to_mail or not topics:
            return Response(
                {'error': 'data not have to_mail or detail or both'}, 
                status=status.HTTP_404_NOT_FOUND
                )

        try:
            # ---- Create email text
            receiver = to_mail.split('@')[0]
            message = """
                <p>
                    ถึง คุณ {}<br/>
                    <br/>
                    {}<br/>
                    <br/>
                    ด้วยความเคารพอย่างสูง<br/>
                    mail test
                </p>
            """.format(
                receiver,
                mail_detail
            )

            # Send mail in gmail
            email = EmailMultiAlternatives(
                subject=topics,
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=[to_mail]
            )
            email.attach_alternative(message, 'text/html')
            email.send()

            message_resp = 'Please see message at {}'.format(to_mail)
            return Response({'message': message_resp}, status=status.HTTP_201_CREATED)
        except Exception:
            return Response({'error': 'Send mail incomplete'}, status=status.HTTP_404_NOT_FOUND)