from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileSerializer
import processing

# function for API
class FileUploadView(APIView):
    # parser term
    parser_class = (FileUploadParser,)

    # post request processing
    def post(self, request, *args, **kwargs):
        # call the serilizer
        file_serializer = FileSerializer(data=request.data)

        # check file validation
        if file_serializer.is_valid():
            # save the image
            file_serializer.save()
            # get card Number
            cardNo = processing.getCardNO(file_serializer.data['file'][1:])
            # get company type like ('orange, vodafon, etc...')
            company = processing.NameC(file_serializer.data['file'][1:])

            # create json dictionary for the output data
            outputData = {}
            # the card serial number
            # print(type(str(cardNo)))
            outputData['cardNo'] = str(cardNo)
            # the company type
            outputData['company'] = company
            # the path of the image uploaded
            outputData['path'] = file_serializer.data['file']
            # print(file_serializer.data['file'][1:])
            # send response
            return Response(outputData, status=status.HTTP_201_CREATED)
        # handle the exception errors
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)