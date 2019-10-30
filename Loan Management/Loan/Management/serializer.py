from rest_framework import serializers

from django.contrib.auth.models import User


from .models import Profile,LoanDetail


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['name','phone','dob','address']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    confirmpassword = serializers.CharField(max_length=32,write_only=True)

    class Meta:
        model = User
        fields = ['username','email','password','confirmpassword','profile']

    def create(self, validated_data):
        password = validated_data['password']
        confirmpassword = validated_data['confirmpassword']
        if password == confirmpassword:
            user = User.objects.create(username=validated_data['username'],
                                       email=validated_data['email'],
                                       )
            user.set_password(password)
            user.save()
            profile_data = validated_data.pop('profile')
            profile = Profile.objects.create(user=user,
                                             name=profile_data['name'],
                                             phone=profile_data['phone'],
                                             dob=profile_data['dob'],
                                             address=profile_data['address']
                                             )
            return user

        else:
            raise serializers.ValidationError({'Password': 'Password does not match'})



class DisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ['name','phone','dob','address']


class LoanDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanDetail
        fields = ['amount','duration']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanDetail
        fields = ['STATUS']


class ForeclosureSerializer(serializers.Serializer):
    days = serializers.IntegerField(required=True)


class LoanlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanDetail
        fields = ['amount','duration','STATUS','returnedIN','amountPaid']
