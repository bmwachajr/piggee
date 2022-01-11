import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

class BaseTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.piglatin_url = reverse('translate:pig_latin')

    def test_tranlates_to_piglatin(self):
        response = self.client.post(self.piglatin_url,
                                    data=json.dumps(sentence),
                                    content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            json.loads(response.content)['translation'], 
            sentence['translation']
        )

    def test_words_that_begin_with_a_consonant(self):
        response = self.client.post(self.piglatin_url,
                                    data=json.dumps(begin_consonants),
                                    content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            json.loads(response.content)['translation'], 
            begin_consonants['translation']
        )

    def test_when_words_begin_with_consonant_clusters(self):
        response = self.client.post(self.piglatin_url,
                                    data=json.dumps(consonant_clusters),
                                    content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            json.loads(response.content)['translation'], 
            consonant_clusters['translation']
        )

    def test_for_words_that_begin_with_vowels(self):
        response = self.client.post(self.piglatin_url,
                                    data=json.dumps(begin_with_vowels),
                                    content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            json.loads(response.content)['translation'], 
            begin_with_vowels['translation']
        )

sentence = {
    'text': "Hello, my name is Alice.",
    'translation': 'Ellohay, myay amenay isay Aliceay.'
}

begin_consonants = {
    'text': 'pig latin banana',
    'translation': 'igpay atinlay ananabay'
}

consonant_clusters = {
    'text': 'smile string glove',
    'translation': 'ilesmay ingstray oveglay'
}

begin_with_vowels ={
    'text': 'eat omelet are',
    'translation': 'eatay omeletay areay'
}
