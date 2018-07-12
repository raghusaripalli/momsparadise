from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from shop.models import Product, Category
from shop.tasks import careers_form_mail, moms_form_mail


def home(request):
    return render(request, 'shop/home.html')


def product_list(request, category_slug=None):
    category = None
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/shop.html', {'category': category, 'categories': categories, 'products': products
                                              , 'cart_product_form': cart_product_form})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product_detail.html', {'product': product, 'cart_product_form': cart_product_form})


def thank_you(request):
    if request.POST.get("careers", "") != "":
        s = dict()
        s['name'] = request.POST.get("name", "")
        s['phone'] = request.POST.get("phone", "")
        s['email'] = request.POST.get("email", "")
        s['edu'] = request.POST.get("edu", "")
        s['current'] = request.POST.get("current", "")
        s['pref'] = request.POST.get("pref", "")

        careers_form_mail(s)
    else:
        mom = dict()
        mom['name'] = request.POST.get("name", "")
        mom['phone'] = request.POST.get("phone", "")
        mom['address'] = request.POST.get("address", "")
        mom['items'] = request.POST.get("items", "")
        mom['timing'] = request.POST.get("timing", "")
        mom['mailid'] = request.POST.get("mailid", "")

        moms_form_mail(mom)

    return render(request, 'shop/thankyou.html')
