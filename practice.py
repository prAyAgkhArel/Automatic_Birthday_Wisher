import smtplib

my_email = "your_gmail"
password = "your_pwd"

#establishing a connection with smtp i.e connection is SMTP object
connection = smtplib.SMTP("smtp.gmail.com")

#making connection secure
connection.starttls()

#logging in to the email
connection.login(user=my_email, password=password)

#sending_mail
connection.sendmail(from_addr=my_email, to_addrs="prayagkharel006@gmail.com", msg="Subject:Hello\n\nThis is body of my email")

#closing the connection you can also open connection as :with smptlib.SMTP("..") as connection:
# and need not to close just like opening file using with clause
connection.close()