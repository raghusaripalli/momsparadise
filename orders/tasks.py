from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Order, OrderItem


def order_notify(order_id):
    """
    Task to send an e-mail to admins when order is created successfully
    """
    order = Order.objects.get(id=order_id)
    order_item = OrderItem.objects.filter(order=order)
    total_price = float(0.0)
    for i in order_item:
        total_price += float(i.quantity) * float(i.product.price)
    subject = 'Order {} - New'.format(order.id)
    html_message = render_to_string('mail/order.html', {'order': order,
                                                        'orderItem': order_item,
                                                        'total_price': total_price})
    plain_message = strip_tags(html_message)
    from_email = 'momsparadisevizag@gmail.com'
    to = 'momsparadisevizag@gmail.com,'+order.email

    mail_sent = send_mail(subject, plain_message, from_email, [to], html_message=html_message)
    return mail_sent
