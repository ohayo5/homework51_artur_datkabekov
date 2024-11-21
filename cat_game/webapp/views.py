from django.shortcuts import render, redirect
from .models import Cat

cat_instance = None

def home(request):
    if request.method == "POST":
        global cat_instance
        name = request.POST.get("name")
        cat_instance = Cat(name=name)
        return redirect("cat_info")
    return render(request, "webapp/home.html")

def cat_info(request):
    global cat_instance
    if not cat_instance:
        return redirect("home")

    action = request.POST.get("action")
    if action == "feed":
        cat_instance.feed()
    elif action == "play":
        cat_instance.play()
    elif action == "sleep":
        cat_instance.sleep()

    return render(request, "webapp/cat_info.html", {
        "cat": cat_instance,
        "avatar": cat_instance.get_avatar(),
    })
