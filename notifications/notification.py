import smtplib

gmail_password = 'tmdacqwxqkldqgzl'
gmail_user = 'rasoolasik1@gmail.com'

def send(invalid):

    sent_from = gmail_user
    to = ['rasoolasik@gmail.com', 'rasoolasik1@gmail.com']
    subject = 'Notification for Access Denied'
    body = "There has been " + str(invalid) + " attempts with wrong credentials"

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        print(sent_from, to, email_text)
        server.sendmail(sent_from, to, email_text)
        server.close()
        print ('Email sent!')
    except Exception as e:
        print ('Something went wrong...')
        raise e


