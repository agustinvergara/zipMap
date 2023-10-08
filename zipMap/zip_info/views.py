import googlemaps
from django.shortcuts import render
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework import status
import requests


from .models import *
from .serializers import *
from rest_framework.response import Response

#google maps client api key
# gmaps = googlemaps.Client(key='AIzaSyDt1w_6cwW568fIIlMevgeRD71epjf_c7w')

#view that captures the zipcode
@api_view(['GET', 'POST'])
def zipcode_capture(request):

    if request.method == 'GET' or 'POST':
        try:
            # getting the postalcode number from POST and making the query in the db
            zipcode_form = ZipCode.objects.get(postal_code=request.data.get("postalCode"))
            # getting the province name related to the postal code
            province_name = zipcode_form.province.province_name
            # serializing the query
            zipcode_serializer = zipCodeSerializer(zipcode_form)
            # getting the serialized data to work the format of the response
            zipcode_serializer_data = zipcode_serializer.data
            # using the dict key to change the province id to the actual name
            zipcode_serializer_data["province"] = province_name

            # changing the keys of the data dict to cammelcase
            zipcode_serializer_data['postalCode'] = zipcode_serializer_data['postal_code']
            del zipcode_serializer_data['postal_code']
            zipcode_serializer_data['countryCode'] = zipcode_serializer_data['country_code']
            del zipcode_serializer_data['country_code']

            return Response(zipcode_serializer_data)
        
        except ZipCode.DoesNotExist:
            return Response({"message": "no se encontro informacion"}, status=status.HTTP_404_NOT_FOUND)

  
