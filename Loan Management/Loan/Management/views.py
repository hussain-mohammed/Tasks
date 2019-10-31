from django.contrib import auth

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


from .serializer import UserSerializer, ProfileSerializer, DisplaySerializer, LoanDetailSerializer, StatusSerializer, \
    ForeclosureSerializer,LoanlistSerializer
from .models import Profile, LoanDetail


# Create your views here.
class register(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        if request.method == 'POST':
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class profile(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        data = Profile.objects.filter(user=self.request.user)
        try:
            status = LoanDetail.objects.filter(user=self.request.user).values('STATUS').order_by('-date')[0]
        except:
            status = LoanDetail.objects.filter(user=self.request.user).values('STATUS').order_by('-date')
        serializer = DisplaySerializer(data, many=True)
        status_serializer = StatusSerializer(status, many=True)
        response = serializer.data + status_serializer.data
        if len(response) >= 2:
            return Response(serializer.data + [status])
        else:
            return Response(serializer.data + ['LOAN IS AVAILABLE. YOU CAN AVAIL USING BELOW FORMS'])

    def post(self, request):
        try:
            statusinstance = LoanDetail.objects.filter(user=self.request.user).values('STATUS').order_by('-date')[0]
            loanstatuslist = ['Available','Rejected','Foreclosed','Disbursed','Defaulter']

            if statusinstance['STATUS'] in loanstatuslist:
                postCall = profile.loanapply(self,request)
            elif statusinstance['STATUS'] == 'Approved':
                postCall = profile.loanclosure(self,request)
            else:
                return Response('Please wait!!!! Your Documents are being validated...',status=status.HTTP_400_BAD_REQUEST)
        except IndexError as e:
            postCall = profile.loanapply(self,request)
        return postCall

    def loanapply(self, request):
        data = request.data
        serializer = LoanDetailSerializer(data=data)
        if serializer.is_valid():
            # serializer.save()
            LoanDetail.objects.create(user=self.request.user,
                                      amount=data['amount'],
                                      duration=data['duration'],
                                      STATUS='Pending'
                                      )
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def loanclosure(self,request):
        data = request.data
        loanduration = LoanDetail.objects.filter(user=self.request.user).values('duration').order_by('-date')[0]
        try:

            serializer = ForeclosureSerializer(data=data)
            if serializer.is_valid:
                # # for changing status from Approved to Closed
                loaninstance = LoanDetail.objects.filter(user=self.request.user).order_by('-date')[0]

                # calculating the amount that customer has to pay
                days = data.get('days', None)
                amount = LoanDetail.objects.filter(user=self.request.user).values('amount').order_by('-date')[0]
                one_day = ((0.06 / 100) * int(amount['amount']))
                pay = amount['amount'] + (one_day * int(days))

                if data.get('days') < loanduration['duration']:
                    loaninstance.STATUS = 'Foreclosed'
                elif data.get('days') == loanduration['duration']:
                    loaninstance.STATUS = 'Disbursed'
                else:
                    loaninstance.STATUS = 'Defaulter'
                
                loaninstance.returnedIN = days
                loaninstance.amountPaid = pay
                loaninstance.save()

                return Response("You Need To Pay " + str(pay) + "-----------------------Your Loan Is closed with the status of " +loaninstance.STATUS)
            return Response("ERROR ENTERING DATA")
        except TypeError as e:
            return Response("days field is required",status=status.HTTP_406_NOT_ACCEPTABLE)

class Detail(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        data = LoanDetail.objects.filter(user=self.request.user)
        serializer = LoanlistSerializer(data, many=True)
        return Response(serializer.data)
