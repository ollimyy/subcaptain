from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import *

urlpatterns = [
    path('',HomeView.as_view()),

    path('accounts/register/', RegisterView.as_view()),
    path('accounts/login/', LoginView.as_view(next_page="/payments")),
    path('accounts/logout/', LogoutView.as_view(next_page="/payments")),

    path('payments', RecurringPaymentListView.as_view()),
    path('payments/new', RecurringPaymentCreateView.as_view()),
    path('payments/<int:pk>', RecurringPaymentUpdateView.as_view()),
    path('payments/<int:pk>/delete', RecurringPaymentDeleteView.as_view()),

    path('categories', PaymentCategoryListView.as_view()),
    path('categories/new', PaymentCategoryCreateView.as_view()),
    path('categories/<int:pk>', PaymentCategoryUpdateView.as_view()),
    path('categories/<int:pk>/delete', PaymentCategoryDeleteView.as_view())
]