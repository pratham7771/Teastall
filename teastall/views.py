from unicodedata import name
from django.forms import forms
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .models import contactuser,signupuser,usersuggestion,paymentuser
from .forms import signupForm,paymentForm,suggestionform,contactForm
import requests
import json
import random
from django.core.mail import send_mail
from teaproject import settings
from django.contrib import messages


# Create your views here.
def index(request):
    userh=request.session.get('userdetails')
    if request.method=='POST':
        if request.POST['password']==request.POST['cpassword']:
            if request.POST.get('signup')=='signup':
                unp=request.POST['username']

                myf=signupForm(request.POST,request.FILES)
                if myf.is_valid():
                    myf.save()
                    print("Signup successfully!")
                    request.session['userp']=unp
                    mo=request.POST['mo']
                    otp=random.randint(1111,9999)

                    #send SMS______________________
                    # mention url
                    url = "https://www.fast2sms.com/dev/bulk"


                    # create a dictionary
                    my_data = {
                        # Your default Sender ID
                        'sender_id': 'FSTSMS',
                        
                        # Put your message here!
                        'message': f'Hello User, \n Your account has been created!',
                        
                        'language': 'english',
                        'route': 'p',
                        
                        # You can send sms to multiple numbers
                        # separated by comma.
                        'numbers': mo	
                    }

                    # create a dictionary
                    headers = {
                        'authorization': '',
                        'Content-Type': "application/x-www-form-urlencoded",
                        'Cache-Control': "no-cache"
                    }
                    # make a post request
                    response = requests.request("POST",
                                                url,
                                                data = my_data,
                                                headers = headers)
                    
                    #load json data from source
                    returned_msg = json.loads(response.text)

                    # print the send message
                    print(returned_msg['message'])
                    # ____________________________
                    
                    return redirect('/')
                else:
                    print(myf.errors)

            elif request.POST.get('login')=='login':
                un=request.POST['username']
                
                ps=request.POST['password']
                cs=request.POST['cpassword']

                userid=signupuser.objects.get(username=un)

                userd=signupuser.objects.filter(username=un,password=ps,cpassword=cs)
                if userd:
                    print("Login successfully!")
                    request.session['userdetails']=un
                    
                    request.session['userid']=userid.id

                    # Send Email___________________
                    subject = 'Welcome to Tea Stall'    
                    message = f'Hello Costumer, \n {un}Your Account has been successfully login!'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = request.POST['username']
                    send_mail( subject,message,email_from,[recipient_list])

                    return redirect('home')
                else:
                    print("login failed!")
        else:
            return render(request,'index.html')
    else:
        pass
        # print("somthig went worng!!!!")
    return render(request,'index.html',{'userc':userh})

def home(request):
    userh=request.session.get('userdetails')
    if userh:
        userpay=paymentuser.objects.filter(cpay=userh)
        userinfo=contactuser.objects.filter(cuser=userh)
        usersug=usersuggestion.objects.filter(nameofuploader=userh)
        return render (request,'home.html',{'userc':userh,'userinfo':userinfo,'userpay':userpay,'usersug':usersug})
    else:
        return render(request,'home.html',{'userc':userh})

def about(request):
    usera=request.session.get('userdetails')
    return render(request,'about.html',{'userc1':usera})

def addtocart(request):
    useradd=request.session.get('userdetails')
    if useradd:
        userpay=paymentuser.objects.filter(cpay=useradd)
        userinfo=contactuser.objects.filter(cuser=useradd)
        usersug=usersuggestion.objects.filter(nameofuploader=useradd)
        return render (request,'addtocart.html',{'usercart':useradd,'userinfo':userinfo,'userpay':userpay,'usersug':usersug})
    else:
        return render(request,'addtocart.html',{'usercart':useradd})

def condelete(request,id):
    cid=contactuser.objects.get(id=id)
    cid.delete()
    return redirect('home')

def sugdelete(request,id):
    csug=usersuggestion.objects.get(id=id)
    csug.delete()
    return redirect('home')

def paydelete(request,id):
    cpa=paymentuser.objects.get(id=id)
    cpa.delete()
    return redirect('home')

def contact(request):
    usercon=request.session.get('userdetails')
    if request.method=='POST':
        cf=contactForm(request.POST)
        if cf.is_valid():
            cf.save()
            print("Contact Qurey Add successfully")
            return redirect('home')
        else:
            print(cf.errors())
    else:
        cf=contactForm()
    return render(request,'contact.html',{'userc2':usercon})

def menu(request):
    userm=request.session.get('userdetails')
    return render(request,'menu.html',{'userc3':userm})

def payment(request):
    userm=request.session.get('userdetails')
    #usrobj=paymentuser.objects.get(name="gopal sorathiya")
    #cvv=usrobj.expyear
    #print(cvv)
    if request.method=='POST':
        paf=paymentForm(request.POST)
        p=request.POST['state']
        if paf.is_valid():
            paf.save()
            print("payment compaleted!")
            #request.session['paydetails']=p
            return redirect('home')
        else:
            print(paf.errors)
    else:
        paf=paymentForm()
    return render(request,'payment.html',{'userc1':userm})

def suggestion(request):
    usersu=request.session.get('userdetails')

    if request.method=='POST':
        usersf=suggestionform(request.POST)
        if usersf.is_valid():
            usersf.save()
            print("Your Suggestion Uploaded!")
            return redirect('home')
        else:
            print(usersf.errors)
    else:
        usersf=suggestionform()
    return render(request,'suggestion.html',{'usersugg':usersu})

def updateprofile(request):
    userup=request.session.get('userdetails')
    userid=request.session.get('userid')
    id=signupuser.objects.get(id=userid)

    if request.method=='POST':
        signupf=signupForm(request.POST)
        if signupf.is_valid():
            signupf=signupForm(request.POST,instance=id)
            signupf.save()
            print("Your Profile updated!")
            msg="Your Profile updated!"
            return render(request,'updateprofile.html',{'userupdate':userup,'userid':signupuser.objects.get(id=userid),'msg':msg})
            # return redirect('home')
        else:
            print(signupf.errors)
    else:
        print("Error....")
    return render(request,'updateprofile.html',{'userupdate':userup,'userid':signupuser.objects.get(id=userid)})

def viewscart(request):
    return render(request,'viewscart.html')

def signup(request):
    user=request.session.get('userdetails')
    if request.method=='POST':
        if request.POST['password']==request.POST['cpassword']:
            #if request.POST.get('signup')=='signup':
                unp=request.POST['username']

                myf=signupForm(request.POST,request.FILES)
                if myf.is_valid():
                    myf.save()
                    print("Signup successfully!")
                    request.session['userp']=unp
                    mo=request.POST['mo']
                    name=request.POST['stfirstname']
                    surname=request.POST['stlastname']
                    #print(surname)
                    otp=random.randint(1111,9999)

                    #send SMS______________________
                    # mention url
                    url = "https://www.fast2sms.com/dev/bulk"


                    # create a dictionary
                    my_data = {
                        # Your default Sender ID
                        'sender_id': 'FSTSMS',
                        
                        # Put your message here!
                        'message': f'Hello {name} {surname}, \n Your account has been created!',
                        
                        'language': 'english',
                        'route': 'p',
                        
                        # You can send sms to multiple numbers
                        # separated by comma.
                        'numbers': mo	
                    }

                    # create a dictionary
                    headers = {
                        'authorization': '',
                        'Content-Type': "application/x-www-form-urlencoded",
                        'Cache-Control': "no-cache"
                    }
                    # make a post request
                    response = requests.request("POST",
                                                url,
                                                data = my_data,
                                                headers = headers)
                    
                    #load json data from source
                    returned_msg = json.loads(response.text)

                    # print the send message
                    print(returned_msg['message'])
                    # ____________________________
                    
                    messages.success(request,"Your Signup successfully!")
                    return redirect('/')
                else:
                    print(myf.errors)
        else:
            pass
    return render(request,'signup.html',{'usersignup':user})

def userlogin(request):
    userl=request.session.get('userdetails')
    if request.method=='POST':
                un=request.POST['username']
                ps=request.POST['password']
                
                # cs=request.POST['cpassword']

                userid=signupuser.objects.get(username=un)
                
                userd=signupuser.objects.filter(username=un,password=ps)
                if userd:
                    print("Login successfully!")
                    # request.session['userdetails']=un.stfirstname
                    request.session['userdetails']=userid.username
                    request.session['userfn']=userid.stfirstname
                    request.session['userid']=userid.id

                    # Send Email___________________
                    subject = 'Welcome to Tea Stall'    
                    message = f'Hello {userid.stfirstname} \nYour Account has been successfully login!'
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = request.POST['username']
                    #send_mail( subject,message,email_from,[recipient_list])

                    messages.success(request,"Your Login successfully!")
                    return redirect('home')
                else:
                    print("login failed!")
    return render(request,'login.html',{'userlogin':userl})

def userlogout(request):
    logout(request)
    return redirect('/')
    
    #return HttpResponse()
# def userlogout1(request):
#     logout(request)
#     return redirect('about')

def details(request):
    userm=request.session.get('userdetails')
    return render(request,'details.html',{'userm':userm})
