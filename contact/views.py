from django.shortcuts import render

# Create your views here.



@require_http_methods(['POST'])
def contact(request):
    response_message = None
    error = None

    try:
        data = json.loads(request.body.decode('utf-8'))
        name = data["name"]
        email = data["email"]
        reason = data["reason"]
        phone = data["phone"]
        message = data["message"]
        if not (name):
            raise ValidationError("Missing 'name'")
        elif not (message):
            raise ValidationError("Missing'message'")
        validate_email(email)
    except (ValidationError, KeyError, ValueError) as e:
        # logger.warning(e)
        error = "Bad input"
        print(str(e))
        return JsonResponse({
            "message" : None,
            "error" : LANDING_PAGE_ERROR["bad_input"]
        })


    email_body = """
    New Message from The school Website
    From: %s
    E-mail: %s
    Reason For Contacting: %s
    Phone Number: %s
    Message: %s


    """ % ( name,
            email,
            reason,
            phone,
            message,
            )


    subject = "Website Inquiry Contact us Page"

    try:
        send_mail(
            subject,
            email_body,
            settings.LANDING_PAGE_INQUIRY_SENDER,
            [settings.RECEPIENTS["sendInquiryForm"]],
            fail_silently=False
        )
        response_message = "Sent successfully"
        error = "None"
    except SMTPException as e:
        logger.error("Failed to send email inquiry")
        logger.error(e)
        error = LANDING_PAGE_ERROR["contact_form_email_send_failure"]
        print(response_message)

    return JsonResponse({
        "message": response_message,
        "error": error
    })