from django.urls import path
from .views import LoanList,LoanDetail

urlpatterns = [
    path('loan/',LoanList.as_view(),name='loan'),
    path('loan/<int:pk>',LoanDetail.as_view(),name='loanview'),
]
