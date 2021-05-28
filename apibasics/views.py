from .serializers import loanSerializers
from rest_framework import generics,permissions
#generics handles almost all of the views
from .models import Loan
class LoanList(generics.ListCreateAPIView):
    queryset= Loan.objects.all()
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    # queryset is all objects from Loan model
    serializer_class= loanSerializers

class LoanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Loan.objects.all()
    serializer_class= loanSerializers


