from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField, SerializerMethodField
from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    url= HyperlinkedIdentityField(
        view_name = 'articles-api:detail',
        lookup_field = 'slug'
    )
    image =SerializerMethodField()
    class Meta:
        model = Article
        fields = [
            'id',
            'url',
            'title',
            'slug',
            'date',
            'image',
        ]

    def get_image(self, obj):
        try:
            image=obj.thumb.url
        except:
            image=None
        return image
