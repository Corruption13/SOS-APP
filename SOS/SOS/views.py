from django.shortcuts import render, redirect
from django.http import HttpResponse
from rescuemap.models import RescueTeam
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth

def user_view(request):
 
    if request.POST.get("rescue_me"):
        print("yes")
        return redirect("../map_me")
    elif request.POST.get("rescue_other"):  # You can use else in here too if there is only 2 submit types.
        print("no")
        return redirect("../map_other")

    return render(request, "user.html")



def submitted_view(request):
    return render(request, "staysafe.html")



def test(request):
    return render(request, "test.html")



def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            row = RescueTeam.objects.get(user=user)
            print("user found!", row)

            if(row.valid == True):
                auth.login(request, user)
                print("Heck yah!");
                return redirect("../map_me")
            else: return redirect('../done')
        else:
            return render(request, "login.html", {'flag': True})
    else:
        return render(request, "login.html")
    #return HttpResponse("<h1>Login First!<h1> <a href='..'> CLick here!</a>  ")



def register_view(request):
    print("register")
    if request.method == "POST":
        print("POSTYES")
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password1']
        email= "placeholder@gmail.com"
        phone = request.POST['phone']
        print("phone: " + phone)
        if(len(password) <= 6):

            print("pass too short")
            return render(request, 'register.html', {'pass_flag': True})
        
        try:
            user = User.objects.create_user(
                    username=username, 
                    password=password,
                    email=email,
                    first_name= first_name,
                    last_name=last_name,
                
                )
            rescue = RescueTeam.create(user, phone, False)

            rescue.save()
            user.save()
            print("user created\n")
            auth.login(request, user)
            return redirect("../reg_done")
        except:
            print("error")
            return render(request, 'register.html', {'alert_flag': True})
          
      


    else:
        print("else_out")
        return render(request, 'register.html')



def logout_view(request):
    auth.logout(request)
    return redirect("../")

def panel_view(request):
    if request.POST.get("register"):
        return redirect("../register")
    elif request.POST.get("login"):  
        return redirect("../login")

    elif request.POST.get("rescue"): 
        return redirect("../rescue")

    elif request.POST.get("extra1"):  
        return redirect(".")
 
    elif request.POST.get("extra2"):  
        return redirect(".")


    else:
        return render(request, "authpanel.html")

def reg_done(request):
    return render(request, "reg_done.html")