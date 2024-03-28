from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Shop, Warehouse, Product, Student
from .forms import ShopForm, WarehouseForm, ProductForm, StudentForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                print(form.errors)
                form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'base/samples/login.html', {'form': form})


def logout_view(request):
    print('sssss')
    auth_logout(request)

    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:

        form = UserRegisterForm()
    return render(request, 'base/samples/register.html', {'form': form})


@login_required(login_url='login')
def create_shop(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.user = request.user
            shop.save()
            return redirect('home')
    else:
        form = ShopForm()
    return render(request, 'base/create_shop.html', {'form': form})


@login_required(login_url='login')
def create_warehouse(request):
    if request.method == 'POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            warehouse = form.save()
            warehouse.user = request.user
            warehouse.save()
            return redirect('home')
        else:
            print(form.errors)
    form = WarehouseForm()
    shops = Shop.objects.all()
    context = {'form': form, 'shops': shops}
    return render(request, 'base/create_warehouse.html', context)


@login_required(login_url='login')
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            product.user = request.user
            product.save()
            return redirect('home')
    form = ProductForm()
    warehouses = Warehouse.objects.all()
    context = {'form': form, 'warehouses': warehouses}
    return render(request, 'base/create_product.html', context)


def home(request):
    if request.user.is_authenticated:
        shops = Shop.objects.filter(user=request.user)
        warehouses = Warehouse.objects.filter(user=request.user)
        products = Product.objects.filter(user=request.user)
        shop_count = Shop.objects.filter(user=request.user).count()
        warehouse_count = Warehouse.objects.filter(user=request.user).count()
        product_count = Product.objects.filter(user=request.user).count()

    else:
        shops = Shop.objects.all()
        warehouses = Warehouse.objects.all()
        products = Product.objects.all()
        shop_count = Shop.objects.all().count()
        warehouse_count = Warehouse.objects.all().count()
        product_count = Product.objects.all().count()

    total = shop_count + warehouse_count + product_count
    context = {'shops': shops, 'warehouses': warehouses, 'products': products,
               'shop_count': shop_count, 'warehouse_count': warehouse_count, 'product_count': product_count,
               'total': total}
    return render(request, 'base/index.html', context)


@login_required(login_url='login')
def delete_warehouse(request, warehouse_id):
    warehouse = get_object_or_404(Warehouse, pk=warehouse_id)
    warehouse.delete()
    return redirect('home')


@login_required(login_url='login')
def delete_shop(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    shop.delete()
    return redirect('home')


@login_required(login_url='login')
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return redirect('home')


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = StudentForm()
    context = {'form': form,}
    return render(request, 'base/add_student.html', context)


def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('add_student')
    else:
        form = StudentForm(instance=student)
    return render(request, 'base/update_student.html', {'form': form})


def delete_student(request):
    student_id = request.POST.get("id")
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return redirect('add_student')


def icons(request):
    return render(request, 'base/icons.html', {})


def buttons(request):
    return render(request, 'base/button.html', {})


def typography(request):
    return render(request, 'base/typography.html', {})


def form_element(request):
    return render(request, 'base/form_element.html', {})


def tables(request):
    return render(request, 'base/tables.html', {})


def charts(request):
    return render(request, 'base/charts.html', {})


def apex_charts(request):
    return render(request, 'base/apex_charts.html', {})


def error404(request):
    return render(request, 'base/samples/error-404.html', {})


def error500(request):
    return render(request, 'base/samples/error-500.html', {})
