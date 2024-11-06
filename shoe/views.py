from django.shortcuts import render, redirect
import requests
from .models import Customer, Order, Cart
from shoeApi.models import MenModel, WomenModel, KidsModel, NewArrivalModel

def get_current_user(request):
    return request.session.get('user', None)

def fetch_api_data(url):
    try:
        response = requests.get(url, timeout=10)  # Set timeout to 10 seconds
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None  # Return None if there's an error

def render_with_user(request, template_name, context):
    current_user = get_current_user(request)
    context['current_user'] = current_user
    return render(request, template_name, context)

def handle_user_login(request, email, password):
    check_user = Customer.objects.filter(email=email, password=password).first()
    if check_user:
        request.session['user'] = check_user.first_name
        request.session['email'] = check_user.email
        return True
    return False

# Views
def index(request):
    return render_with_user(request, 'index.html', {})

def login(request):
    if get_current_user(request):
        return redirect('index')
    
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if handle_user_login(request, email, password):
            return redirect('index')
        else:
            error = 'Invalid email or password'
            return render(request, 'login.html', {'error': error})

    return render(request, 'login.html')

def signUp(request):
    if get_current_user(request):
        return redirect('index')

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pwd = request.POST.get('password')

        if Customer.objects.filter(email=email).exists():
            error = 'This email is already used'
            return render(request, 'signup.html', {'error': error})
        
        Customer.objects.create(first_name=fname, last_name=lname, email=email, password=pwd)
        return redirect('login')

    return render(request, 'signup.html')

def logout(request):
    request.session.flush()
    return redirect('index')

def men(request):
    url = 'http://127.0.0.1:8000/api/men/'
    data = fetch_api_data(url)
    if data is None:
        # Handle the case where data is None (e.g., show an error message)
        return render_with_user(request, 'men.html', {'data': [], 'error': 'Failed to fetch data from API'})
    return render_with_user(request, 'men.html', {'data': data})


def women(request):
    url = 'http://127.0.0.1:8000/api/women/'
    data = fetch_api_data(url)
    return render_with_user(request, 'women.html', {'data': data})

def kids(request):
    url = 'http://127.0.0.1:8000/api/kids/'
    data = fetch_api_data(url)
    return render_with_user(request, 'kids.html', {'data': data})

def newArrivals(request):
    url = 'http://127.0.0.1:8000/api/newArrivals/'
    data = fetch_api_data(url)
    return render_with_user(request, 'new-arrivals.html', {'data': data})

def orderSummary(request, id, url):
    if not get_current_user(request):
        return redirect('index')

    email = request.session['email']
    ForeignKey = Customer.objects.get(email=email)

    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        qty = int(request.POST.get('quantity'))
        amount = int(request.POST.get('amount'))
        imageUrl = request.POST.get('imageUrl')

        Order.objects.create(
            productId=id,
            productName=name,
            productQty=qty,
            totalAmount=(amount * qty),
            imageUrl=imageUrl,
            foreignKey=ForeignKey
        )
        return redirect('index')

    url = f'http://127.0.0.1:8000/api/{url}/{id}'
    product = fetch_api_data(url)
    return render_with_user(request, 'orderSummary.html', {'product': product})

def search(request):
    if request.method == 'POST':
        current_user = get_current_user(request)
        s = request.POST.get('search-bar').title()

        kids = KidsModel.objects.filter(name=s)
        women = WomenModel.objects.filter(name=s)
        men = MenModel.objects.filter(name=s)

        if kids.exists():
            return render(request, 'search.html', {'shoeinfo': kids, 'url': 'kids', 'current_user': current_user})
        if women.exists():
            return render(request, 'search.html', {'shoeinfo': women, 'url': 'women', 'current_user': current_user})
        if men.exists():
            return render(request, 'search.html', {'shoeinfo': men, 'url': 'men', 'current_user': current_user})
        
        return render(request, 'search.html', {'NoData': s, 'current_user': current_user})

    return redirect('index')

def importOrders(request):
    if not get_current_user(request):
        return redirect('index')

    email = request.session['email']
    ForeignKey = Customer.objects.get(email=email)
    data = Order.objects.filter(foreignKey=ForeignKey)

    return render_with_user(request, 'confirmOrder.html', {'data': data})

def cancelOrder(request, id):
    Order.objects.get(orderId=id).delete()
    return redirect('orders')

def addToCart(request, id):
    if 'user' in request.session:
        email = request.session['email']
        ForeignKey = Customer.objects.get(email=email)

        models = [KidsModel, WomenModel, MenModel, NewArrivalModel]
        for model in models:
            item = model.objects.filter(id=id).first()
            if item:
                Cart.objects.create(
                    productId=item.id,
                    productName=item.name,
                    Amount=item.price,
                    description=item.description,
                    imageUrl=item.imageUrl,
                    foreignKey=ForeignKey
                )
                return redirect(model.__name__.lower())  # Redirect to the appropriate category page

    return redirect('index')

def cart(request):
    current_user = get_current_user(request)
    return render(request, 'cart.html', {'current_user': current_user})

def importCart(request):
    if 'user' in request.session:
        current_user=request.session['user']
        email=request.session['email']
    
        ForeignKey=Customer.objects.get(email=email)
        data=Cart.objects.filter(foreignKey=ForeignKey)
        return render(request,'cart.html',{'current_user':current_user,'data':data})
    
    return render(request,'cart.html')

def removeCart(request, id):
    Cart.objects.get(CartId=id).delete()
    return redirect('cart')
