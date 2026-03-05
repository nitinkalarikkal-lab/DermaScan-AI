
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login_view/',views.login_view,name='login_view'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('admin_header/',views.admin_header,name='admin_header'),
    path('verify_doctor',views.verify_doctor,name='verify_doctor'),
    path('admin_index/',views.admin_index,name='admin_index'),
    path('approved_doctors/',views.approved_doctors,name='approved_doctors'),
    path('feedbacks/',views.feedbacks,name='feedbacks'),
    path('users/',views.users,name='users'),
    path('complaint/',views.complaint,name='complaint'),
    path('doctor_index/',views.doctor_index,name='doctor_index'),
    path('doctor_profile/',views.doctor_profile,name='doctor_profile'),
    path('doctor_profile_edit/',views.doctor_profile_edit,name='doctor_profile_edit'),
    path('manage_schedule/',views.manage_schedule,name='manage_schedule'),
    path('view_appoinment/',views.view_appoinment,name='view_appoinment'),
    path('chat/',views.chat,name='chat'),
    path('doctor_complaint/',views.doctor_complaint,name='doctor_complaint'),
    path('user_home/',views.user_home,name='user_home'),
    path('view_doctors/', views.view_doctors, name='view_doctors'),
    path('user_register/', views.user_register, name='user_register'),
    path('user_complaint/', views.user_complaint, name='user_complaint'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('user_profile_edit/', views.user_profile_edit, name='user_profile_edit'),
    path('view_bookings/',views.view_bookings,name='view_bookings'),
    path('admin_approve_doctor/<int:id>',views.admin_approve_doctor,name='admin_approve_doctor'),
    path('admin_reject_doctor/<int:id>', views.admin_reject_doctor, name='admin_reject_doctor'),
    path('doctor_feedback/',views.doctor_feedback,name='doctor_feedback'),
    path('user_feedback/',views.user_feedback,name='user_feedback'),
    path('admin_send_reply/<int:id>',views.admin_send_reply,name='admin_send_reply'),
    path('view_schedule/<int:id>',views.view_schedule,name='view_schedule'),
    path('user_chat/',views.user_chat,name='user_chat'),
    path('book_appointment/<int:id>/',views.book_appointment,name='book_appointment'),
    path('doctor_approved_booking/<int:id>', views.doctor_approved_booking, name='doctor_approved_booking'),
    path('doctor_rejected_booking/<int:id>', views.doctor_rejected_booking, name='doctor_rejected_booking'),
    path("pay/<int:booking_id>/", views.pay_now, name="pay_now"),
    path("payment/callback/", views.payment_callback, name="payment_callback"),
    path("chat/<int:id>/", views.chat_page, name="chat"),
    path("load_chat/", views.load_chat, name="load_chat"),
    path("send_chat/", views.send_chat, name="send_chat"),
    path('add_rating/<int:doctor_id>/', views.add_rating, name='add_rating'),
    path('view_rating/<int:doctor_id>/', views.view_rating, name='view_rating'),

    path("doctor_paid_patients/",views.doctor_paid_patients,name="doctor_paid_patients"),
    path('new_chat/<int:patient_user_id>/',views.new_doctor_chat,name='new_doctor_chat'),

    path('user_doctor_chat/', views.user_doctor_chat_list, name='user_doctor_chat_list'),
    path('user_doctor_chat/<int:doctor_user_id>/', views.user_doctor_chat, name='user_doctor_chat'),

    path("skin-predict/",views.skin_prediction, name="skin_prediction"),
    path("skin_chatbot/",views.skin_chatbot, name="skin_chatbot"),
    path("navigation_header/",views.navigation_header, name="navigation_header"),
    path('user_view_rating/<int:doctor_id>/',views.user_view_rating,name='user_view_rating'),

    path('forgot-password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('forgot-password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),


]
