from rest_framework import serializers
from .models import Author, AuthorProfile, Post

# AuthorProfile Serializer (OneToOne with Author)
class AuthorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorProfile
        fields = ['website', 'phone']

# Author Serializer (include nested AuthorProfile)
class AuthorSerializer(serializers.ModelSerializer):
    profile = AuthorProfileSerializer(source='authorprofile', read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'email', 'bio', 'profile']

# Post Serializer (include nested Author)
class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)  # nested author data দেখাবে

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'author']
