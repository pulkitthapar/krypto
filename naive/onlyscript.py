import requests
import json
import smtplib

token = input("Name of token: ").strip().lower()


def fetch(token):
    url = (
        f"https://api.coingecko.com/api/v3/simple/price?ids={token}&vs_currencies=usd")
    response = json.loads(requests.get(url).text)
    value = int(response[token]['usd'])
    #print(f"Current price: {str(value)} USD")
    return value


def send_mail(val,token):
    email = '#your_email'
    password = '#your_email_password'
    send_to_email = '#recipient_email'
    message =f"Value of {token} dropped to {val} USD!"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    print('Sending email...')
    server.sendmail(email, send_to_email, message)
    server.quit()
    print('Email Sent!')

target = int(input("Target price: "))
while(True):
    curr = fetch(token)
    if(curr==target):
        send_mail(curr,token)
        break


