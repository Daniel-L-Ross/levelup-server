from django.core.exceptions import ValidationError
from django.db.models import Count, Q
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.fields import CreateOnlyDefault
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from levelupapi.models import Game, Genre, Gamer

class GameView(ViewSet):

    def create(self, request):
        gamer = Gamer.objects.get(user=request.auth.user)

        game = Game()
        game.title = request.data["title"]
        game.maker = request.data["maker"]
        game.number_of_players = request.data["numberOfPlayers"]
        game.skill_level = request.data["skillLevel"]
        game.gamer = gamer

        # Use the Django ORM to get the record from the database
        # whose `id` is what the client passed as the
        # `gameTypeId` in the body of the request.

        genre = Genre.objects.get(pk=request.data["genreId"])
        game.genre = genre

        try:
            game.save()
            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game, context={'request', request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        gamer = Gamer.objects.get(user=request.auth.user)

        game = Game.objects.get(pk=pk)
        game.title = request.data["title"]
        game.maker = request.data["maker"]
        game.number_of_players = request.data["numberOfPlayers"]
        game.skill_level = request.data["skillLevel"]
        game.gamer = gamer

        genre = Genre.objects.get(pk=request.data["genreId"])
        game.genre = genre

        game.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        try:
            game = Game.objects.get(pk=pk)
            game.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        # get the current user for use with Q
        gamer = Gamer.objects.get(user=request.auth.user)

        games = Game.objects.annotate(
            # use COUNT annotate method to add a count 
            # of how many events exist for this game
            event_count=Count('events'),
            # use Q to run a query. Here we get a count
            # of how many events the current user has created 
            # for the game
            user_event_count=Count(
                'events',
                filter=Q(events__organizer=gamer)
            ))

        genre = self.request.query_params.get('type', None)
        if genre is not None:
            games = games.filter(genre__id=genre)

        serializer = GameSerializer(
            games, many=True, context={'request': request})
        return Response(serializer.data)


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'maker', 'number_of_players', 'skill_level', 'genre', 'event_count', 'user_event_count')
        depth = 1