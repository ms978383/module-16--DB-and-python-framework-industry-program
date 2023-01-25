from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def sign_up(request):
    if request.POST:
        user_data=User.objects.all()
        print("-----------------------------------------------------")
        role_name=request.POST['rolename']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        contact=request.POST['mobilenumber']
        email=request.POST['emailname']
        password=request.POST['passwordname']
        print("---------------jjadjaksak")
        user_data=User(role=role_name,first_name=firstname,last_name=lastname,contact=contact,email=email,password=password)
        user_data.save()
         
        
          
    
        re_msg="registerd"  
        context={
        're_msg':re_msg,
        } 
        print("  data registerd ")         
        return render(request,'My_shop/login.html',context)
    
    
    else:
       
        
        
        return render(request,'My_shop/register.html')


def login(request):
    if request.POST:
        print("qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq")
        user_data=User.objects.all()
        email=request.POST['emailname']
        
        password=request.POST['passwordname']
        user_data= User.objects.get(email=email)
        
        if user_data.password==password:
            print("1111111")
            if user_data.role=='Admin':
                user_data=User.objects.all()
                context={
                    'user_data':user_data
                }
                
                print("--------admin")
                return render(request,'My_shop/profile.html',context)
                
            elif user_data.role=='product manager':
                user_data= User.objects.all()
                product_details=productsubcategory.objects.all()
                context={
                    'user_data':user_data,
                    'product_details':product_details
                }
                print("------------pro")
                print('111223344')
                return render(request,'My_shop/all-productproduct.html',context)
                
    else:
        print("22222222")
        return render(request,'My_shop/login.html')
    
    

def add_products(request):
    
    
        
    print("--------------session")
    if request.POST:
        print("--------------POSt")
        product_details=productsubcategory.objects.create(
                    
        productid=request.POST['productid'],
        productname=request.POST['itemname'],
        productprice=request.POST['price'],
        productimage=request.FILES['productimage'],
        productmodel=request.POST['modelname'],
        productram=request.POST['ramsize']
        )
       
                
                
        print("------------save")
                
        if product_details:
            s_msg="Product add successfully! "
            print("---if part")
            context={
            's_msg':s_msg,
            'product':product_details
                        
            }
            return render(request,'My_shop/add-product.html',context) 
        else:
            print("---else part")
            context={
            
            'product':product_details
            }
            return render(request,'My_shop/add-product.html',context)
            print("----------last ")
    return render(request,'My_shop/add-product.html')

def all_products(request):
    if request.session:
        user_data= User.objects.all()
        product_details=productsubcategory.objects.all()
        
        
        
        context={
            'user_data':user_data,
            'product_details':product_details
        }
            
            
        return render(request,'My_shop/all-product.html',context)


def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return render(request,'My_shop/login.html')
    else:
        return render(request,'My_shop/login.html')

def edit_products(request,id):
    
    product_details=productsubcategory.objects.get(pk=id)
    context={
         'product_details':product_details
    }
    
    return render(request,'My_shop/update-product.html',context)
def update_products(request,id):
    
    if request.POST:
        productid=request.POST['productid']
        productname=request.POST['itemname']
        productprice=request.POST['price']
        
        productmodel=request.POST['modelname']
        productram=request.POST['ramsize']
        
        product_details=productsubcategory.objects.get(pk=id)
        product_details.productid=productid
        product_details.productname=productname
        product_details.productprice=productprice
   
        product_details.productmodel=productmodel
        product_details.productram=productram
        product_details.save()
        
        
    return render(request,'My_shop/all-product.html')

def delete_products(request,id):
    product_details=productsubcategory.objects.get(pk=id)
    product_details.delete()
    
    
    return render(request,'My_shop/all-product.html')