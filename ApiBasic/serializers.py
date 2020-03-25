from rest_framework import serializers
from .models import Article



# class ArticleSerializer(serializers.Serializer):
# 	title   = serializers.CharField(max_length=100)
# 	author  = serializers.CharField(max_length=100)
# 	email   = serializers.EmailField(max_length=100)
	
	

# 	def create(self, validated_data):
# 		return Article.object.create(validated_data)

# 	def update(self, instance, validated_data):
# 		instance.title   = validated_data.get('title', instance.title)
# 		instance.author  = validated_data.get('author', instance.title)
# 		instance.email   = validated_data.get('email', instance.title)
# 		instance.save()
# 		return instance

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'