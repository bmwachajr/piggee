from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import PiglatinSerializer, textSerializer
import re

class PigLatinApiView(GenericAPIView):
    serializer_class=textSerializer

    def post(self, request):
        """
        Method to handle post requests for translating a sentence
        :params:
        request:- holds the request a user sends to the server.
        :returns:
        translation:- the translated text.
        endpoints.
        """
        serializer_class=PiglatinSerializer
        try:
            text = request.data.get('text', "")
            pig_latin = self.translate(text)

            resp_data = {
                'text': text,
                'translation': pig_latin,
                'codec': 'Pig Latin'
            }

            return Response(resp_data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {"status": "Bad Request", "error": e}, status.HTTP_400_BAD_REQUEST
            )

    def translate(self, text):
        words = re.split("(\W)", text)
        vowels = "aeiouAEIOU"
        punctuations = "!()-[]{};:'\"\,<>./?@#$%^&*_~"
        output = ""
        
        for word in words:
            char = word.lower()
            # pass if punctuation or space
            if word in punctuations or word.isspace():
                pass

            elif word[0] in vowels:
                word += 'ay'

            else:
                start = 0
                for letter in list(word):
                    if letter in vowels:
                        break
                    else:          
                        start += 1

                word = word[start:] + word[:start] + "ay"
        
            output += self.title_case(word)
        return output

    def title_case(self, word):
        if not word.islower() and not word.isupper():
            word = word.title()

        return word
