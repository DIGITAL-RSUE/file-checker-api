from dj_rest_auth.serializers import UserDetailsSerializer


class UserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = (
            "username",
            "first_name",
            "last_name",
        )
