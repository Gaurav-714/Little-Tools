from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ConvertedFile
from .serializers import ConvertedFileSerializer
from django.core.exceptions import ValidationError
from PIL import Image
from io import BytesIO
import img2pdf


class ConvertImageView(APIView):
    def post(self, request):
        image = request.POST.get('image')
        if not image:
            return Response({'error': 'please provide an image file.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            converted_file = self.convert_to_pdf(image)
            serializer = ConvertedFileSerializer(converted_file)
        except ValidationError as ex:
            return Response({'error': str(ex)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            'status' : status.HTTP_201_CREATED,
            'message' : 'Image is converted successfully.',
            'data' : serializer.data
        })

    def convert_to_pdf(self, image):
        img = Image.open(image)
        if img.mode != 'RGB':
            img = img.convert('RGB')

        pdf_bytes = img2pdf.convert(img)

        converted_file = ConvertedFile(image=image)
        converted_file.pdf.save(image.name.replace('.','_') + '.pdf', BytesIO(pdf_bytes))
        converted_file.save()

        return converted_file
