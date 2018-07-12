from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def careers_form_mail(s):
    subject = 'New Career Application'
    html_message = render_to_string('mail/career_details.html', {'career': s})
    plain_message = strip_tags(html_message)
    from_email = 'momsparadisevizag@gmail.com'
    to = 'momsparadisevizag@gmail.com'
    return send_mail(subject, plain_message, from_email, [to], html_message=html_message)


def moms_form_mail(mom):
    subject = 'New Admission - Mom'
    html_message = render_to_string('mail/mother_details.html', {'mom': mom})
    plain_message = strip_tags(html_message)
    from_email = 'momsparadisevizag@gmail.com'
    to = 'momsparadisevizag@gmail.com'
    send_mail(subject, plain_message, from_email, [to], html_message=html_message)