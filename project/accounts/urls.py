from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home , name = 'Home'),
    path('login/' , views.login_form , name= 'Login'),
    path('profile/' , views.My_profile , name= 'Profile'),
    path('signup/' , views.Signup , name='SignUp'),
    path('updatprofile/' , views.Update_data , name = 'Update_Profile'),
    path('odrder/', views.Order_list , name='Order_list'),
    path('createpost/' , views.create_post , name = 'Create_Post'),
    path('bloglist/' , views.blog_list , name = 'Blog_list'),
    path('myposts/' , views.My_posts , name='My_posts'),
    path('myfvpost/', views.Fv_Post , name= 'My_Fv'),
    path('deletpost/<int:id>' , views.Post_Delete , name= 'detlepost'),
    path('updatepost/<int:id>' , views.Update_Post , name='UpdatePost'),
    path('mypostdtl/<int:id>' , views.My_post_detail , name='My_post_detail'),
    path('blogdtl/<int:id>' , views.Blog_Detail , name= 'Blog_Detail'),
    path('blogdtlan/<int:id>' , views.Blog_Detail_AN , name= 'Blog_Detail_AN'),
    path('book_doctor/<slug:slug>/' , views.Book_Doctor , name='Book_Doctor'),
    path('doctors_detail/<slug:slug>/' , views.Doctors_detail , name= 'Doctors_detail'),
]