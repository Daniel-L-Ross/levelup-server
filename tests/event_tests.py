import json
from levelupapi.models import Event, Game, Genre, 
from rest_framework import status
from rest_framework.test import APITestCase

class EventTests(APITestCase):
    def setUp(self):
        """
        Create a new account and sample: genre, game
        """
        url = "/register"
        data = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "bio": "Love those gamez!!"
        }
        # Initiate request and capture response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Store the auth token
        self.token = json_response["token"]
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

        # Assert that a user was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # SEED DATABASE WITH ONE GAME TYPE
        # This is needed because the API does not expose a /gametypes
        # endpoint for creating game types
        genre = Genre()
        genre.label = "Board game"
        genre.save()

        self.game = Game()
        self.game.genre_id = 1
        self.game.skill_level = 5
        self.game.title = "Monopoly"
        self.game.maker = "Milton Bradley"
        self.game.number_of_players = 4
        self.game.gamer_id = 1

        self.game.save()

    def test_create_event(self):
        """
        Ensure we can create a new event.
        """
        # DEFINE EVENT PROPERTIES
        url = "/events"
        data = {
            "description": "Welcome To at lunch",
            "game": 1,
            "date": "2021-10-04",
            "time": "12:00"
        }

        # Make sure request is authenticated
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["title"], data["title"])
        self.assertEqual(json_response["maker"], data["maker"])
        self.assertEqual(json_response["skill_level"], data["skillLevel"])
        self.assertEqual(json_response["number_of_players"], data["numberOfPlayers"])