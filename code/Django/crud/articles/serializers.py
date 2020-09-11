from rest_framework import serializers
from .models import Artist, Music, Comment


# POST api/v1/musics/<music_pk>/comments/
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'music_id']


# List표현
class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content']


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'title', 'artist_id']


# music.comment_set.all()
class MusicDetailSerializer(MusicSerializer):
    comments = CommentListSerializer(source='comment_set', many=True)
	# 많은 수의 정보를 보여줘야 하는 부분은 many속성이 필요하다.
    class Meta(MusicSerializer.Meta):
        fields = MusicSerializer.Meta.fields + ['comments']


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']


# arrist.music_set.all()
class ArtistDetailSerializer(serializers.ModelSerializer):
    music_set = MusicSerializer(many=True)
    music_count = serializers.IntegerField(source='music_set.count')

    class Meta:
        model = Artist
        fields = ['id', 'name', 'music_set', 'music_count']