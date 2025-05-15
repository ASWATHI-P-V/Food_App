from django.shortcuts import render
from comida.models import*
# Create your views here.
def index(request):
	return render(request,'index.html')

def register(request):
	if request.method=='POST':
		name=request.POST['First Name']
		address=request.POST['Address']
		place=request.POST['Place']
		email=request.POST['Email']
		contact=request.POST['Contact']
		password=request.POST['Password']
		query=user_tb(name=name,address=address,place=place,email=email,contact=contact,password=password)
		query.save()
		return render(request,'index.html')
	else:
		return render(request,'index.html')	

def login(request):
	if request.method=='POST':		
		email=request.POST['Email']
		password=request.POST['Password']
		query=user_tb.objects.all().filter(email=email,password=password)
		if query:
			for x in query:
				request.session['id']=x.id
				return render(request,'index.html',{'succes':'succesfuly login'})
		else:
			return render(request,'index.html',{'error':'invailed password'})
	else:
		return render(request,'index.html')

def logout(request):
	if request.session.has_key('id'):
		del request.session['id']
	return render(request,'index.html')

def adminlogin(request):
	if request.method=='POST':		
		email=request.POST['email']
		password=request.POST['password']
		check=adminlogin_tb.objects.all().filter(email=email,password=password)
		if check:
			for x in check:
				request.session['id']=x.id
				return render(request,'adminindex.html',{'succes':'succesfuly login'})
		else:
			return render(request,'adminlogin.html',{'error':'invailed password'})
	else:
		return render(request,'adminlogin.html')

def addproduct(request):
	if request.method=='POST':
		Name=request.POST['Name']
		Category=request.POST['Category']
		Description=request.POST['Description']
		Price=request.POST['Price']
		Image=request.FILES['Image']
		Availableqty=request.POST['Availableqty']
		query=add_products_tb(Name=Name,Category=Category,Description=Description,Price=Price,Image=Image,Availableqty=Availableqty)
		query.save()
		return render(request,'forms.html')
	else:
		return render(request,'forms.html')
		
def userlist(request):
	query=user_tb.objects.all()
	return render(request,'tables.html',{'query':query})

def adminindex(request):
	return render(request,'adminindex.html')