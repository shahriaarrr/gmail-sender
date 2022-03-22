import yagmail

user = input('your email: ')
'''
If you don't know how to enable app code in Gmail, refer to the link below

https://support.google.com/accounts/answer/185833?hl=en
'''
app_password =  input('your app password: ')
to = input('Destination email: ')

subject = input('give me your email\'s subject: ')
message = input('write your message: ')
content = [message,]

print('\nplease wait...\n')

with yagmail.SMTP(user, app_password) as yag:
    yag.send(to, subject, content)
    print('Sent email successfully:)')