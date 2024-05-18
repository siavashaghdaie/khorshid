from django.shortcuts import render, redirect
from django.template import context
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from .models import Customer, Product, User, Buy, MenuCat, MenuItem, Order,OrderItem
from .forms import UserForm, BuyForm, ProductForm, ArtworkForm, ArtistForm, OrderItemForm
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
import requests, convert_numbers, random
from kavenegar import *
from datetime import datetime



def index(request):
    shop = []
    gallery = []
    product = Product.objects.all()
    shop_counter = 0
    gallery_counter = 0
    for product in product:
        if product.product_type == 'two':
            shop_counter +=1
            if shop_counter < 4:
                shop.append(product)
      
        if product.product_type == 'one':
            gallery_counter += 1
            if gallery_counter < 5:
                gallery.append(product)
    context = {'shop':shop, 'gallery': gallery}
    return render (request, 'cafe/index.html', context)

    

#decorator is preventing a logged in user from re-loggin in. to see the details open decorator.py
@unauthenticated_user
def loginPage(request):
    #send a parameter to the template to tell which for we need
    page = 'login'
    #getting information from front end
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        #check to see if user exists:
        #this is only to check user existance by username.
        #password is not checked yet
        try:
            user = User.objects.get(username=username)
        except:
            #raise an error "user does not exist"
            pass

        #authenticate user and check password
        user = authenticate(request, username=username, password=password)
        print(user)
        #if user exists then go on and login 
        if user is not None:
            print('user is not None')
            login(request, user)
            return redirect('index')
        else:
            #raise an error "password is incorrect"
            pass

    context = {'page' : page}
    return render (request, 'cafe/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect ('index')

@unauthenticated_user
def registerUser(request):
    page = 'register'
    form = UserForm() 
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            #we add commit=False to be able to freeze the user form and still get it's objects
            #because we may need to clean the form data.
            #for example change all uppercases to lower case in username
            user = form.save(commit=False)
            #its better to use .lower() also in login form to make sure
            #if user enters username with upper case by mistake
            #login procedure is not interupted
            user.username = user.username.lower()
            user.password = make_password(user.password)
            user.save()
            #we need to save the for first to be able to change the group
            # for user which does not exist, group can not be changed
             
            group = Group.objects.get(name='customer')
            user.groups.add(group)

            # group = Group.objects.get(name='customer')
            # user.groups.add(group)

            #now registeration is done and we want to log user in
            login(request, user)
            return redirect('index')
        else:
            #raise an error "form validation failed"
            pass
             
    context = {'page' : page, 'form':form}
    return render(request, 'cafe/login.html', context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    context = {'user':user}
    return render (request, 'cafe/profile.html', context)

def userProfileUpdate(request,pk):
    page = 'profileupdate'
    user = User.objects.get(id=pk)
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            user = form.save()
            user.username = user.username.lower()
            user.password = make_password(user.password)
            user.save()

            return redirect ('index')

    context={'form':form, 'page':page }
    return render(request, 'cafe/login.html', context)

def profileDelete(request,pk):
    user = User.objects.get(id=pk)
    #if request.method == 'POST':
    if request.user.is_authenticated:
        if request.user.id == user.id:
            user.delete()
            return redirect('login')
        else:
            return redirect('index')
    #return render(request, 'cafe/login.html')


def menu(request):
    cats = MenuCat.objects.all()
    items = MenuItem.objects.all()
    order_items = OrderItem.objects.all()
    orders = []
    try:
        device = request.COOKIES['device']
        username = request.user
        user = User.objects.get(username = username)
        customer, created = Customer.objects.get_or_create(user=user, name=user.username, device=device) 
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(name=device, device=device) 

    order, created = Order.objects.get_or_create(customer=customer, complete = False)


    if request.method == 'POST':
        item = request.POST['item']
        menu_item = MenuItem.objects.get(name=item)
        qty= request.POST['qty']
        

        if int(qty) > 0:
            total_price = int(qty) * int(menu_item.price)
            orderItem, created = OrderItem.objects.get_or_create(menu_item = menu_item, order = order)
            orderItem.quantity = qty
            orderItem.total_price = total_price
            orderItem.save()
        else:
            try:
                orderItem = OrderItem.objects.get(menu_item = menu_item, order = order)
                orderItem.delete()
            except:
                pass


    for ord in order_items:
        orders.append(ord.menu_item.name)

    print(orders)                
    context = {'cats' : cats, 'items' : items, 'order_items':order_items, 'order':order,'orders':orders, 'customer':customer}
    return render (request, 'cafe/menu.html', context)

    

# @allowed_users(allowed_roles=['customer'])
def shop(request):
    shop = Product.objects.all()
    context = {'shop': shop}
    return render (request, 'cafe/shop.html', context)

def product_delete(request,pk):
    product = Product.objects.get(id=pk)
    product_type = product.product_type 
    product.delete()
    if product_type == 'two':
        return redirect ('shop')
    else:
        return redirect ('gallery')


def product(request,pk):
    product = Product.objects.get(id=pk)
    form = BuyForm() 
    if request.method == "POST":
        form = BuyForm(request.POST)
        if form.is_valid():
            buy = form.save(commit=False)
            product = Product.objects.get(id=pk)
            buy.product = product
            buy.ver = '0000'
            buy.save()
            return redirect('factor',buy.id)
        else:
            #raise an error "form validation failed"
            pass
             
    context = {'form':form, 'product':product}
    return render (request, 'cafe/product.html',context)

def product_modify(request,pk):
    page = 'product_update'
    product = Product.objects.get(id=pk)
    if product.product_type == 'two':
        form = ProductForm(instance=product)
        if request.method == 'POST':
            form = ProductForm(request.POST,request.FILES, instance=product)
            if form.is_valid():
                form.save()
                return redirect ('shop')
    
    if product.product_type == 'one':
        form = ArtworkForm(instance=product)
        if request.method == 'POST':
            form = ArtworkForm(request.POST,request.FILES, instance=product)
            if form.is_valid():
                form.save()
                return redirect ('gallery')


    context={'form':form, 'page':page }
    return render(request, 'cafe/add_modify.html', context)

def product_add(request):
    page = 'product_add'
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            product = form.save()
            product.product_type = 'two'
            product.save()
            return redirect ('shop')
    context={'form':form, 'page':page }
    return render(request, 'cafe/add_modify.html', context)

def artwork_add(request):
    page = 'product_add'
    form = ArtworkForm()
    if request.method == 'POST':
        form = ArtworkForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            product = form.save()
            product.product_type = 'one'
            product.save()
            return redirect ('gallery')

    context={'form':form, 'page':page }
    return render(request, 'cafe/add_modify.html', context)

def artist_add(request):
    form = ArtistForm()
    if request.method == 'POST':
        form = ArtistForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('gallery')

    context={'form':form }
    return render(request, 'cafe/add_artist.html', context)

def factor(request,pk):
    fault = 0
    buy = Buy.objects.get(id=pk)
    
    if request.method == 'POST':
        ver = request.POST.get('ver')
        ver = convert_numbers.persian_to_english(ver) #512396044
        if ver == buy.ver:
                return redirect ('payment', buy.id)
        else:
            if fault < 3:
                fault += 1
            else:
                buy.ver = '0000'
                buy.save()
                fault = 0
                return redirect ('factor',buy.id)

    context={'buy': buy, 'fault': fault}
    return render (request, 'cafe/factor.html', context)

def mafia(request):
    return render (request, 'cafe/mafia.html')

def gallery(request):
    shop = Product.objects.all()

    painting = False
    writing = False
    sculpture = False
    photography = False
    mosaic = False
    fasion = False
    other = False

    for product in shop:
        if product.section == 'painting':
            painting = True
        if product.section == 'writing':
            writing = True
        if product.section == 'sculpture':
            sculpture = True
        if product.section == 'photography':
            photography = True
        if product.section == 'mosaic':
            mosaic = True
        if product.section == 'fasion':
            fasion = True
        if product.section == 'other':
            other = True
        
    context = {'shop': shop, 'painting': painting, 'writing': writing,
    'sculpture':sculpture, 'photography':photography, 'mosain': mosaic,
    'fasion':fasion, 'other':other}
    return render (request, 'cafe/gallery.html', context)

def artist(request):
    return render (request, 'cafe/artist.html')

def artwork(request):
    return render (request, 'cafe/artwork.html')

def contact(request):
    return render (request, 'cafe/contact.html')

def social(request):
    return render (request, 'cafe/social.html')

def events(request):
    return render (request, 'cafe/events.html')

def modify(request, pk):
    buy = Buy.objects.get(id=pk)
    product = buy.product.id
    buy.delete()
    return redirect('product',product)

def sms(request,pk):
    
    buy = Buy.objects.get(id = pk)
    token = random.randint(1000, 9999)
    buy.ver = token
    buy.save()
    mobile = buy.ord_mobile[1:]
    mobile = convert_numbers.persian_to_english(mobile) #512396044

    sms='https://sms.magfa.com/magfaHttpService?service=Enqueue&domain=sinet&username=irib_67&password=VLAJXUiMkECWYRxX&from=3000067&to=98'+mobile+'&message='+'کدتأیید شما:'+str(token)
    r = requests.get(sms)
    if r.status_code == 200:
        print ('SMS Successfully Sent!')
        
    else:
        print('SMS Server Error')

    # API_KEY = '5937424C356D384743795863555654446178546761474A3336664C77612F7176454F72704B4547763569453D'
    # try:
    #     api = KavenegarAPI(API_KEY)
    #     params = {
    #         'receptor': '09124630590',
    #         'template': 'teste-vahede-fani-cafe-ketab-khorshid',
    #         'token': token
    #     }
    #     response = api.verify_lookup(params)
    # except APIException as e:
    #     print(e)
    # except HTTPException as e:
    #     print(e)

    return redirect ('factor', buy.id)

def payment(request, pk):
    buy = Buy.objects.get(id=pk)
    buy.satteled = True
    buy.save()
    context = {'buy':buy}
    return render (request, 'cafe/thanks.html' , context)

    