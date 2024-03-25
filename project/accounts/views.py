from django.shortcuts import render , redirect
from django.contrib.auth.models import User , AnonymousUser
from .models import Profile , patient , Create_Post , Comment , Favorite
from .forms import Login_Form , UserCreationForms , Update_User , Update_Profile, Update_Post_Form
from django.contrib.auth import authenticate , login
from django.contrib.auth.decorators import login_required
# Create your views here.


def Home(request):


    context = {
        'doctors' : User.objects.all(),
    }
    return render(request , 'pages/Home.html' , context) 



def Doctors_detail(request , slug):

    context = {
        'dtls' : Profile.objects.get(slug = slug),
    }

    return render(request , 'pages/Doctors_detail.html' , context)


def login_form(request):

    if request.method == 'POST':
        Login = Login_Form()
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        user = authenticate(request , username = Username , password = Password)
        if user is not None :
            login(request , user)
            return redirect ('Home')
    else:
        Login = Login_Form()

    context = {
        'login_form' : Login
    }

    return render(request , 'pages/Login.html' , context)

@login_required(login_url='Login')
def My_profile(request):

    return render(request, 'pages/Myprofile.html')

def Signup(request):

    Form = UserCreationForms()

    if request.method == 'POST':
       Form = UserCreationForms(request.POST)
       if Form.is_valid():
           Form.save()
           username = Form.cleaned_data.get('username')
           password = Form.cleaned_data.get('password')
           user = authenticate(username = username , password = password)
           login(request , user)
           return redirect('Home')

    context = {
        'sign_up_form': Form
    }

    return render(request , 'pages/Signup.html' , context)


@login_required(login_url='Login')
def Update_data(request):

    user_data = Update_User(instance=request.user)
    user_profile = Update_Profile(instance=request.user.profile)

    if request.method == 'POST':
        user_data = Update_User( request.POST , instance=request.user)
        user_profile = Update_Profile( request.POST , request.FILES , instance=request.user.profile)

        if user_data.is_valid and user_profile.is_valid :
            user_data.save()
            user_profile.save()
            return redirect ('Profile')

    context = {
        'user_data': user_data,
        'user_profile' : user_profile
    }

    return render(request , 'pages/Updat_Profile.html' , context)


def Book_Doctor(request , slug):
    user = Profile.objects.get(user = slug)
    context = {
        'user': user,
    }

    if request.method == 'POST':
        doctor = request.POST['doctor']
        name = request.POST['name']
        age = request.POST['age']
        phone1 = request.POST['phone1']
        phone2 = request.POST['phone2']
        description = request.POST['description']

        data = patient(doctor = user.user , name = name , age = age , phone1 = phone1 , phone2 = phone2 , description = description)

        if data != None:
            data.save()
            return redirect('Home')

    return render(request , 'pages/Book_Doctor.html' , context)

@login_required(login_url='Login')
def Order_list (request):

    context = {

        'Order': patient.objects.filter( doctor = request.user)
    }

    return render(request , 'pages/Order_list.html' , context)

@login_required(login_url='Login')
def create_post(request):

    user = request.user.profile.user

    if request.method == 'POST':
        crt_pst = Create_Post(user = user , title = request.POST.get('title') , subject = request.POST.get('subject') , image = request.FILES.get('image') , Introduction = request.POST.get('Introduction'))
        
        if crt_pst != None:
            crt_pst.save()
            return redirect('Home')

    return render(request , 'pages/Create_Post.html')


def blog_list(request):


    context = {
        'Blogs': Create_Post.objects.all().order_by('time'),
    }

    return render(request , 'pages/Blog_list.html' , context)

@login_required(login_url='Login')
def Blog_Detail(request , id):

    Post = Create_Post.objects.get(id = id)

    
    Fav = Favorite.objects.filter(user = request.user , Post = id)
    Fan = False

    if Fav:
        Fan = True


    if request.method == 'POST' and 'comments' in request.POST :
        data = Comment(post = Post , comment= request.POST.get('comments') , name= request.POST.get('name') , email = request.POST.get('email'))
        if data != None and len(request.POST.get('comments')) > 1:
            data.save()
    
    
    if 'FAV' in request.POST:
        Favorite( Post = Post , user = request.user).save()
    
    if 'DeleteFan' in request.POST:
        Favorite.objects.get(user = request.user , Post = id).delete()


    context = {
        'Blog_dtl': Create_Post.objects.get(id = id),
        'comments' : Comment.objects.filter(post = id),
        'Fan': Fan,
    }

    return render(request , 'pages/Blog_Detail.html' , context)

@login_required(login_url='Login')
def My_posts(request):

    context = {
        'Blogs': Create_Post.objects.filter(user = request.user),
    }

    return render(request , 'pages/My_posts.html' , context)

@login_required(login_url='Login')
def My_post_detail(request , id):


    context = {
        'Blog_dtl': Create_Post.objects.get(id = id),
        'comments': Comment.objects.filter(post = id),
    }

    return render(request , 'pages/My_post_detail.html' , context)

@login_required(login_url='Login')
def Update_Post(request ,  id):

    MyPost = Create_Post.objects.get(id = id)

    post_form = Update_Post_Form(instance = MyPost)

    if request.method == 'POST':
        post_form = Update_Post_Form(request.POST , request.FILES , instance = MyPost )
        if post_form.is_valid():
            post_form.save()
            return redirect('/')

    context = {
        'Post':post_form,
    }
    return render(request , 'pages/Update_Post.html' , context)

@login_required(login_url='Login')
def Post_Delete(request , id):

    mypost = Create_Post.objects.get(id = id)

    if request.method == 'POST':
        mypost.delete()
        return redirect('My_posts')

    context = {
        'Post': mypost,
    }

    return render(request , 'pages/My_Post_Confirm_delete.html' , context)

@login_required(login_url='Login')
def Fv_Post(request):

    context = {
        'Blogs': Favorite.objects.filter(user = request.user)
    }

    return render(request , 'pages/Favorite_Post.html' , context)


def Blog_Detail_AN(request , id):

    Post = Create_Post.objects.get(id = id)


    if request.method == 'POST' and 'comments' in request.POST :
        data = Comment(post = Post , comment= request.POST.get('comments') , name= request.POST.get('name') , email = request.POST.get('email'))
        if data != None and len(request.POST.get('comments')) > 1:
            data.save()
    


    context = {
        'Blog_dtl': Create_Post.objects.get(id = id),
        'comments' : Comment.objects.filter(post = id),
    }

    return render(request , 'pages/Blog_Detail_AN.html' , context)