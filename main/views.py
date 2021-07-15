from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.db.models import Q
from django.http import JsonResponse

from datetime import datetime
from .models import *


# Create your views here.

def home(request):
    return render(request,'main/index.html')

def policy(request):
    return render(request,'main/policy.html')

def about(request):
    return render(request,'main/about.html')

def contact(request):
    return render(request,'main/contact.html')


def shop_details(request,pk):
    
    category1 = Category.objects.get(pk=pk)
    products=Product1.objects.filter(cat_id=category1)
    sub_cat1= [we.subcat_id.id for we in products]
    temp=[]
    sub_cat1=list(set(sub_cat1))
    for i in sub_cat1:
        temp.append(SubCategory.objects.get(pk=i))

    sub_cat={pk:temp}

    print(sub_cat1)
    
    context={'products':products,'category1':category1,'sub_cat':sub_cat,'urlkey':pk}

    return render(request,'main/shop-details.html',context)

def sub_category(request,cpk,pk):
    category1 = Category.objects.get(pk=cpk) 
    subcategory1=SubCategory.objects.get(pk=pk)
    products=Product1.objects.filter(cat_id=category1,subcat_id=subcategory1)
    product1=Product1.objects.filter(cat_id=category1)
    sub_cat1= [we.subcat_id.id for we in product1]
    
    
    
    
    temp=[]
    sub_cat1=list(set(sub_cat1))
    for i in sub_cat1:
        temp.append(SubCategory.objects.get(pk=i))

    
    sub_cat={cpk:temp}
    
    
    print(products)
    
    context={'products':products,'subcategory1':subcategory1,'sub_cat':sub_cat}

    return render(request,'main/shop-details.html',context)



    



def shop(request):

    Cat=Category.objects.all()
    context = {'Cat':Cat}
    return render(request,'main/shop.html',context)

def cart1(request):
    user = request.user
    if user.is_authenticated:
        try:
            c = Cart.objects.filter(cus_id = request.user)
        except:
            print("cart query not matched")
            c = None
        
        
        print(c)
        amount = 0.0
        
        cart_product = [p for p in Cart.objects.all() if p.cus_id == request.user]

        for p in cart_product:
            tempamount = (p.quantity*p.product_id.price)
            amount+=tempamount
            
        if amount<=1000:
            discount=((amount)*5)/100
        elif amount>1000 and amount<=2000:
            discount=((amount)*10)/100
        elif amount>2000 and amount<=3000:
            discount=((amount)*20)/100
        elif amount>3000 and amount<=4000:
            discount=((amount)*30)/100
        elif amount>4000 and amount<=5000:
            discount=((amount)*40)/100
        elif amount>5000 and amount<=6000:
            discount=((amount)*50)/100
        else:
            discount=((amount)*50)/100


        totalpurchased = len(cart_product)
        if totalpurchased == 0:
            return render(request,'main/empty.html')
        data = {
            'totalpurchased':totalpurchased,
            'amount':amount,
            'discount':discount,
            'total':amount-discount,
            
        }
        data['cart'] = c
        print(data['cart'])
        return render(request,'main/cart.html',data)
    else:
        return redirect('login')

def plus_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        c=Cart.objects.get(Q(product_id=prod_id) & Q(cus_id=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        discount=0.0
        totalamount=0.0
        cart_product = [p for p in Cart.objects.all() if p.cus_id == request.user]

        for p in cart_product:
            tempamount = (p.quantity*p.product_id.price)
            amount+=tempamount
            
        if amount<=1000:
            discount=((amount)*5)/100
        elif amount>1000 and amount<=2000:
            discount=((amount)*10)/100
        elif amount>2000 and amount<=3000:
            discount=((amount)*20)/100
        elif amount>3000 and amount<=4000:
            discount=((amount)*30)/100
        elif amount>4000 and amount<=5000:
            discount=((amount)*40)/100
        elif amount>5000 and amount<=6000:
            discount=((amount)*50)/100
        else:
            discount=((amount)*50)/100  
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount-discount,
            'discount':discount
        }
        print(data)
        return JsonResponse(data)

def minus_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        try:
            c=Cart.objects.get(Q(product_id=prod_id) & Q(cus_id=request.user))
        except:
            print("empty cart!")
        if(c):
        
            c.quantity-=1
            c.save()
        try:
            test = Cart.objects.filter(cus_id = request.user)
            print("this is also working",test)
            for i in test:
                print(i,i.quantity)
                if i.quantity == 0:
                    print("deleting:-",i.product_id.name)
                    i.delete()
        except:
            print("hehehehe")
        amount = 0.0
       
        totalamount=0.0
        discount=0.0
        cart_product = [p for p in Cart.objects.all() if p.cus_id == request.user]

        for p in cart_product:
            tempamount = (p.quantity*p.product_id.price)
            amount+=tempamount
        if amount<=1000:
            discount=((amount)*5)/100
        elif amount>1000 and amount<=2000:
            discount=((amount)*10)/100
        elif amount>2000 and amount<=3000:
            discount=((amount)*20)/100
        elif amount>3000 and amount<=4000:
            discount=((amount)*30)/100
        elif amount>4000 and amount<=5000:
            discount=((amount)*40)/100
        elif amount>5000 and amount<=6000:
            discount=((amount)*50)/100
        else:
            discount=((amount)*50)/100     
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount-discount,
            'discount':discount
        }
        print(data)
        return JsonResponse(data)

def remove_cart(request):
    if request.method=='GET':
        prod_id=request.GET['prod_id']
        try:
            c=Cart.objects.get(Q(product_id=prod_id) & Q(cus_id=request.user))
        except:
            print("cart is empty!")
        if(c):
            c.delete()
        amount = 0.0
        
        totalamount=0.0
        cart_product = [p for p in Cart.objects.all() if p.cus_id == request.user]

        for p in cart_product:
            tempamount = (p.quantity*p.product_id.price)
            amount+=tempamount
        if amount<=1000:
            discount=((amount)*5)/100
        elif amount>1000 and amount<=2000:
            discount=((amount)*10)/100
        elif amount>2000 and amount<=3000:
            discount=((amount)*20)/100
        elif amount>3000 and amount<=4000:
            discount=((amount)*30)/100
        elif amount>4000 and amount<=5000:
            discount=((amount)*40)/100
        elif amount>5000 and amount<=6000:
            discount=((amount)*50)/100
        else:
            discount=((amount)*50)/100     
        data={
            
            'amount':amount,
            'totalamount':amount-discount,
            'discount':discount
        }
        print(data)
        return JsonResponse(data)



def checkout(request):
    user = request.user
    if user.is_authenticated:
        try:
            c = Cart.objects.filter(cus_id = request.user)
        except:
            return render(request,'main/empty.html')
            
        
        
        print(c)
        amount = 0.0
       
        discount=0.0
        cart_product = [p for p in Cart.objects.all() if p.cus_id == request.user]

        for p in cart_product:
            tempamount = (p.quantity*p.product_id.price)
            amount+=tempamount
            
        if amount<=1000:
            discount=((amount)*5)/100
        elif amount>1000 and amount<=2000:
            discount=((amount)*10)/100
        elif amount>2000 and amount<=3000:
            discount=((amount)*20)/100
        elif amount>3000 and amount<=4000:
            discount=((amount)*30)/100
        elif amount>4000 and amount<=5000:
            discount=((amount)*40)/100
        elif amount>5000 and amount<=6000:
            discount=((amount)*50)/100
        else:
            discount=((amount)*50)/100     
        
        
        
        totalpurchased = len(cart_product)
        try:
            shipping_details=Customer.objects.filter(user=user)
            print(shipping_details)
            shipping_details=shipping_details[len(shipping_details)-1]
            print(shipping_details)
        except:
            shipping_details=None
        print(shipping_details)
        flag="0"
        if shipping_details==None:
            flag="1"
        print(flag)
        data = {
            'totalpurchased':totalpurchased,
            'amount':amount,
            'totalamount':amount-discount,
            'cart':cart_product,
            'flag':flag,
            'shipping_details':shipping_details,
            'discount':discount
            
        }
        data['cart'] = c
        print(data['cart'])
        return render(request,'main/checkout.html',data)
    else:
        return redirect('login')

    return render(request,'main/checkout.html')

def login(request):
    return render(request,'account/login.html')

def signup(request):
    return render(request,'account/signup.html')

def search(request):
    if request.is_ajax():
        res=None
        pro=request.POST.get('pro')
        
        qs=Product1.objects.filter(name__icontains=pro)
        if len(qs)>0 and len(pro)>0:
            data=[]
            for pos in qs:
                item={
                    'pk':pos.pk,
                    'name':pos.name,
                    
                    
                }
                data.append(item)
            res=data[:3]
            print(res)
        else:
            res='No item found..'

        return JsonResponse({'data':res})
    return JsonResponse({})



def add_to_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        print(prod_id)
        product_information = Product1.objects.get(pk = prod_id)
        print(product_information)
        user = request.user
        try:
            c = Cart.objects.get(cus_id = request.user,product_id=product_information)
        except:
            print("cart query not matched")
            c = None
        
        print(c)
        if c:
            c.quantity+=1
            c.save()
        else:
            cont_obj = Cart(cus_id = user,product_id=product_information, quantity=1)
            cont_obj.save()
            c = Cart.objects.get(cus_id = user,product_id=product_information)
        amount = 0
        cart_product = [p for p in Cart.objects.all() if p.cus_id == request.user]

        sumofitem = c.get_total_cart
        for p in cart_product:
            tempamount = (p.quantity*p.product_id.price)
            amount+=tempamount

        totalpurchased = len(cart_product)
        data = {
            'sumofitem': sumofitem,
            'quantity':c.quantity,
            'totalpurchased':totalpurchased,
            'amount':amount
        }
    # print("\U0001f600")
    return JsonResponse(data)

def update_address(request):
    if request.method=='POST':
        user=request.user
        if user.is_authenticated:
            address=request.POST['address']
            city=request.POST['city']
            state=request.POST['state']
            zipcode=request.POST['zipcode']
            print(address,city,state,zipcode)
            try:
                temp=Customer.objects.get(user=user)
                temp.delete()
            except:
                temp=None
            
            shipping_address_obj=Customer(user=user,address=address,city=city,zipcode=zipcode,state=state)
            
            shipping_address_obj.save()
            print(shipping_address_obj)
            return redirect("checkout")
        else:
            return redirect("login")
    else:
        return redirect("checkout")

def orderplaced(request):
    if request.method=='POST':
        user=request.user
        if user.is_authenticated:
            c = Cart.objects.filter(cus_id = user)
            d=datetime.now()
            customer=Customer.objects.get(user=user)
            for we in c:
               order = OrderPlaced(user=user,customer=customer, product=we.product_id,quantity=we.quantity,date_ordered=d)
               order.save()
               we.delete()
               
            
            print(order,"hello")
            order = OrderPlaced.objects.filter(user=user)
            return render(request,'main/success.html',{'order':order})
        return redirect("login")
    else:
        user=request.user
        if user.is_authenticated:
            try:
                order=OrderPlaced.objects.filter(user=user)
            except:
                order=None
            
            return render(request,'main/orderplaced.html',{'order':order})
        else:
            return redirect("login")
        
    
    
        

        
