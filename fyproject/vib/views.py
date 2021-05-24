from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from vib.models import Extend
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'vib/home.html')

def features(request):
    return render(request, 'vib/features.html')

def about(request):
    return render(request, 'vib/about.html')

def contact(request):
    return render(request, 'vib/contact.html')

def ulogin(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        print(user)
        #extendobject = Extend.objects.all()
        accounttype = Extend.objects.get(user=user)
        #print(accounttype.user_type)
        type = accounttype.user_type
        
       
        if user is not None:
            login(request  , user)
            if(type=="Candidate"):
                request.session['Utype']=type
                #return redirect('/dashboard/')
                return render(request, 'vib/home.html')
            if(type=="Company"):
                request.session['Utype']=type
                return redirect('/dashboard/')
                #return render(request, 'company/dashboard.html')

        else:
            messages.error(request, "Invalid credentials! Please try again")
            return render(request, "vib/login.html")
    return render(request, 'vib/login.html')

def signup(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        checkemail = User.objects.filter(email=email)
        checkuser = User.objects.filter(username=username)
        
        if len(checkemail)>0:
            messages.error(request, "Email is already exits.")
            return render(request, 'vib/signup.html')
        if len(checkuser)>0:
            messages.error(request, "User Name is already exits.")
            return render(request, 'vib/signup.html')
        
        # muser = User.objects.all()
        # for itme in muser:
        #     if(itme.email==email):
        #         messages.error(request, "Email is already exits.")
        #         return render(request, 'vib/signup.html')
        #         break

        # try:
        #     uemail = User.objects.get(email=request.POST['email'])

        # except User.DoesNotExist as e:
        #     messages.error(request, "Email is already exits.")
            

        if len(username) > 10:
            messages.error(request, " Your user name must be under 10 characters")
            return render(request, 'vib/signup.html')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return render(request, 'vib/signup.html')
        if password != cpassword:
            messages.error(request, " Passwords do not match")
            return render(request, 'vib/signup.html')

        # Create the user
        user = User.objects.create_user(username, email, password)
        print(user)
        user_type = request.POST['user_type']
        if user_type == "Company":
            company_name =request.POST['companyName']
            userType = Extend(user_type = user_type , user=user, company_name=company_name)
        else:
            userType = Extend(user_type = user_type , user=user)
        userType.save()
        user.save()
        
        messages.success(request, "You have succesfully Registerd.")
        return render(request, 'vib/signup.html')
    return render(request, 'vib/signup.html')




def schedule(request):
    return render(request, 'vib/schedule.html')

def ulogout(request):
    logout(request)
    try:
        del request.session['Utype']
    except KeyError:
        pass
    return redirect('/')
    #return render(request, 'vib/home.html')


