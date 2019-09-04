from django.utils.crypto import get_random_string
from .dao import sql_templates
from django.shortcuts import render
from celery import shared_task
from theangrydev.models import dbconn
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


@shared_task
def send_email(email):
    message = Mail(
        from_email='prithaj@theangrydev.io',
        to_emails=email,
        subject='New content from theangrydev!!!',
        html_content=render('subs_email.html', {})
    )

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))


@shared_task
def notify_subscribers(post_id):
    '''
    This message will be pushed to the queue when I make a new post.
    This will generate a list of people who have subscribed to the tags attached to this post
    '''
    sql = sql_templates["subs_list.sql"].render({
        'POST_ID': post_id
    })

    dbconn.execute(sql)
    emails = [email[0] for email in dbconn.fetchall()]

    for email in emails:
        send_email.delay(email)
