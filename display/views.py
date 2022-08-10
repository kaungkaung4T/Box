from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from display.models import profile
from display.form import ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from display.models import speak
from display.models import SMS
from django.http import HttpResponse, JsonResponse
from display.models import Blog
from display.form import BlogForm, FileForm
from display.form import FileForm, UserUpadteForm
from display.models import File, Like
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from display.serializer import BlogSerilizer
from rest_framework.decorators import api_view
from display.serializer import FileSerilizer
import json
import urllib.request
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
def api(request):
    context = [
        "api/token/",
        "api/token/refresh/"
    ]
    return Response(context)


# building api and all tests are tested with post man and all success
#test blog use with rest framwork and post man everything that tested are works
class resting(APIView):
    def get(self, request, *args, **kwargs):
        b = Blog.objects.all()
        bs = BlogSerilizer(b, many=True)
        return Response(bs.data)

    def post(self, request, *args, **kwargs):
        bs = BlogSerilizer(data=request.data)
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        return Response(bs.errors)

    def put(self, request, pk, *args, **kwargs):
        b = Blog.objects.get(id=pk)
        bs = BlogSerilizer(b, data=request.data)
        if bs.is_valid():
            bs.save()
            return Response(bs.data)
        return Response(bs.errors)

    def delete(self, request, pk, *args, **kwargs):
        b = Blog.objects.get(id=pk)
        b.delete()
        data = {}
        data["success"] = "success"
        return Response(data=data)

# test with rest_api in browser before this was tested with post_man
# tests are all success
from rest_framework.decorators import api_view

@api_view(["PUT"])
def update_rest(request, pk):
    b = Blog.objects.get(id=pk)
    bs = BlogSerilizer(b, data=request.data)
    if bs.is_valid():
        bs.save()
        return Response(bs.data)
    return Response(bs.errors)

@api_view(["DELETE"])
def delete_rest(request, pk):
    b = Blog.objects.get(id=pk)
    b.delete()
    data = {}
    data["success"] = "success"
    return Response(data=data)



#test file with rest and post man
# didnt add update for file in user interface but everything test with POST MAN is success for more complete
# and also all test datas with rest api in browser are all success.
from display.serializer import FileSerilizer
class file_test(APIView):
    serializer_class = FileSerilizer
    def get(self, request, *args, **kwargs):
        f = File.objects.all()
        fs = FileSerilizer(f, many=True)
        return Response(fs.data)

    def post(self, request, *args, **kwargs):
        serilizer_class = FileSerilizer
        fs = FileSerilizer(data=request.data)
        if fs.is_valid():
            fs.save()
            return Response(fs.data)
        return Response(fs.errors)

    def put(self, request, pk, *args, **kwargs):
        f = File.objects.get(id=pk)
        fs = FileSerilizer(f, data=request.data)
        if fs.is_valid():
            fs.save()
            return Response(fs.data)
        return Response(fs.errors)

    def delete(self, request, pk, *args, **kwargs):
        f = File.objects.get(id=pk)
        f.delete()
        data = {}
        data["success"] = "success"
        return Response(data=data)

#test url for update with filefied from fileserilizer
class file_test2(APIView):
    serializer_class = FileSerilizer

    def put(self, request, pk, *args, **kwargs):
        f = File.objects.get(id=pk)
        fs = FileSerilizer(f, data=request.data)
        if fs.is_valid():
            fs.save()
            return Response(fs.data)
        return Response(fs.errors)


#here is rest_framework test in browser before that is test with post man
# it is another way to test in browser and it also work but better test in class file_test
# in class file_test, everything tested are all success
@api_view(["PUT"])
def update_rest2(request, pk):
    f = File.objects.get(id=pk)
    fs = FileSerilizer(f, data=request.data)
    if fs.is_valid():
        fs.save()
        return Response(fs.data)
    return Response(fs.errors)

@api_view(["DELETE"])
def delete_rest2(request, pk):
    f = File.objects.get(id=pk)
    f.delete()
    data = {}
    data["success"] = "success"
    return Response(data=data)

# tests data are all success
# start from here is backend

def profile_home(request):
    new = Blog.objects.filter(user__username=request.user)
    image = profile.objects.filter(user__username=request.user)
    if request.method == "POST":
        new = Blog.objects.filter(user__username=request.user)
        image = profile.objects.filter(user__username=request.user)
        p = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if p.is_valid():
            p.save()
            messages.success(request, "your photo has been updated!")
            return redirect("profile")
    else:

        p = ProfileUpdateForm()

    return render(request, "profile.html",
                  {"p":p,"new":new, "image":image})

def profile2(request, p):
    new = Blog.objects.filter(user__username=p)
    image = profile.objects.filter(user__username=p)
    return render(request, "profile2.html",
                  {"new":new, "image":image})

def home(request):
    b = Blog.objects.all()
    if request.method == "POST":
        b = Blog.objects.all()
        return render(request, "index.html",
                      {"b":b})

    return render(request, "index.html",
                  {"b":b})

def search(request):
    if request.method == "POST":
        s = request.POST["search"]
        search = profile.objects.filter(user__username__icontains=s)
        return render(request, "search.html",
                      {"search": search, "s":s})

    return render(request, "search.html")


def registration(request):
    if request.method == "POST":
        name = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if name == "" or email == "" or password == "":
            messages.info(request, "You need to fill out those fields!")
            return redirect("registration")

        if password == password2:
            if User.objects.filter(username=name).exists():
                messages.info(request, "username already exist!")
                return redirect("registration")

            elif User.objects.filter(email=email).exists():
                messages.info(request, "email already exist!")
                return redirect("registration")

            else:
                user = User.objects.create_user(username=name, email=email, password=password)
                user.save()
                return redirect("login")
        else:
            messages.info(request, "passwords are not same!")
            return redirect("registration")

    else:
        return render(request, "registration.html")


def login(request):
    if request.method == "POST":
        name = request.POST["username"]
        password = request.POST["password"]

        u = auth.authenticate(username=name, password=password)
        if u is not None:
            auth.login(request, u)
            return redirect("/")
        else:
            messages.info(request, "login Fail!")
            return redirect("login")
    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect("/")


def chat(request):
    return render(request, "chat.html")

def chat2(request, chatid):
    cid = speak.objects.get(name=chatid)
    username = request.GET.get("user")
    return render(request, "chat2.html",
                  {"cid":cid, "username":username})

def save(request):
    s = request.POST["speak"]
    username = request.POST["username"]
    if speak.objects.filter(name=s).exists():
        return redirect("chat/"+ s + "/?user=" + username)
    else:
        new = speak.objects.create(name=s)
        new.save()
        return redirect("chat/"+ s + "/?user=" + username)

def store(request):
    username = request.POST["username"]
    speak = request.POST["speak"]
    chatting = request.POST["chatting"]
    image = request.POST["image"]
    new = SMS.objects.create(name=speak, username=username, data=chatting, image=image)
    new.save()
    return HttpResponse("message sent")

def sms(request, chatid):
    s = speak.objects.get(name=chatid)
    new = SMS.objects.filter(name=s.id)
    return JsonResponse({"new":list(new.values())})


def blog(request):
    if request.method == "POST":
        b = BlogForm(request.POST, request.FILES)
        if b.is_valid():
            instance = b.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, "Uploaded")
            return redirect("profile")
    else:
        b = BlogForm()

    return render(request, "blog.html",
                  {"blog":b})

def update_blog(request, pk):
    b_all = Blog.objects.get(id=pk)
    form = BlogForm(instance=b_all)
    if request.method == "POST":
        new_b = BlogForm(request.POST, request.FILES, instance=b_all)
        if new_b.is_valid():
            new_b.save()
            messages.success(request, "Updated")
            return redirect("profile")
    return render(request, "updateblog.html",
                  {"form":form})

def delete_blog(request, pk):
    if request.method == "POST":
        b = Blog.objects.get(id=pk)
        b.delete()
        messages.success(request, "Deleted")
    return redirect("profile")

def like(request):
    if request.method == "POST":
        pk = request.POST.get("like")
        b = Blog.objects.get(id=pk)
        if request.user in b.liked.all():
            b.liked.remove(request.user)
        else:
            b.liked.add(request.user)
        like, created = Like.objects.get_or_create(user=request.user, post_id=b.id)

        if not created:
            if like.value == "Like":
                like.value = "unlike"
            else:
                like.value = "Like"
        like.save()
    return redirect("/")

def file(request):
    fall = File.objects.filter(user__username=request.user)
    if request.method == "POST":
        fall = File.objects.filter(user__username=request.user)
        f = FileForm(request.POST, request.FILES)
        if f.is_valid():
            instance = f.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, "Uploaded")
            return redirect("file")
    else:
        f = FileForm()

    return render(request, "file.html",
                  {"f":f, "fall":fall})

def update_file(request, pk):
    f = File.objects.get(id=pk)
    ff = FileForm(instance=f)
    if request.method == "POST":
        ff = FileForm(request.POST, request.FILES, instance=f)
        if ff.is_valid():
            ff.save()
            messages.success(request, "Updated")
            return redirect("file")
    return render(request, "file2.html",
                  {"ff":ff, "f":f})

def delete_file(request, pk):
    if request.method == "POST":
        f = File.objects.get(id=pk)
        f.delete()
        messages.success(request, "Deleted")
    return redirect("file")

def setting(request):
    if request.method == "POST":
        user = UserUpadteForm(request.POST, request.FILES, instance=request.user)
        profile = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user.is_valid() and profile.is_valid():
            user.save()
            profile.save()
            messages.success(request, "Updated")
            return redirect("setting")
    else:
        user = UserUpadteForm()
        profile = ProfileUpdateForm()

    return render(request, "setting.html",
                  {"user2":user, "profile":profile})

def users(request):
    p = profile.objects.all()
    return render(request, "users.html",
                  {"p":p})

def image(request):
    num = 1
    try:
        if request.method == "POST":

            if "hello" in request.POST:
                s = request.POST["save"]

                s2 = request.POST.get("save2")
                s2 = int(s2)
                num += s2

                num = str(num)
                out = urllib.request.urlopen(
                    "https://api.unsplash.com/search/collections/?page=" + num + "&query=" + s + "&per_page=10&client_id=PQWPBeazRPcL-LNVkq6gdG0Shw3MNqPTAnqD50jJ71Y").read()
                new = json.loads(out)
                create = {
                    # "name": new["results"][0]["cover_photo"]["urls"]["small"]
                    "name": new["results"]
                }
                return render(request, "image.html",
                              {"create": create, "num":num, "s":s})

            if "search" in request.POST:
                s = request.POST["search"]

                if s == " ":
                    return render(request, "image.html",
                                  {"s": s})
                if " " in s:
                    news = ""
                    for ss in s:
                        if ss == " ":
                            ss = "-"
                        news += ss
                    s = news
                num = 1
                num = str(num)

                out = urllib.request.urlopen("https://api.unsplash.com/search/collections/?page="+ num +"&query="+ s +"&per_page=10&client_id=PQWPBeazRPcL-LNVkq6gdG0Shw3MNqPTAnqD50jJ71Y").read()

                new = json.loads(out)
                create = {
                    # "name": new["results"][0]["cover_photo"]["urls"]["small"]
                    "name": new["results"]
                }
                return render(request, "image.html",
                              {"create": create, "s":s, "num":num})


        else:
            create = []

        return render(request, "image.html")

    except Exception as e:
        return HttpResponse("<center><h2 style='display:inline;'>Network connection error.</h2>"
                            "<label> Please check your network, is off or not. </label><center>")

def read_more(request, pk):
    b = Blog.objects.get(id=pk)
    return render(request, "readmore.html",
                  {"b":b})








