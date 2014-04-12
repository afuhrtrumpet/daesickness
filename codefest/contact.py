from django.core.mail import send_mail

def contact_sponsor(term, sponsor_email, desparate_email, desparate_name):
    message = "{0} has some questions about {1}".format(desparate_name, term)
    message += ".  You signed up as a sponsor for this condition.\n"
    message += "It would be wonderful if you got back to {0} via email:\n\n\t".format(desparate_name)
    message += desparate_email
    send_mail('DAE Sickness',
              message,
              'from@example.com',
              [sponsor_email],
              fail_silently=False
              )
