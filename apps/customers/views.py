from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from apps.customers.models import Customer
from apps.customers.serializer import CustomerSerializer


class CustomerRetrieveUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerListCreateAPIView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

