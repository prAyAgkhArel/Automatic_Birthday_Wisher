
import datetime #to get hold of time
import os    # to access from system
import pandas  # to handle csv file
import smtplib # to connect with smtp
import random


#getting todays date
today = datetime.datetime.now()
month = today.month
day = today.day
today_date = (month, day)

data_frame = pandas.read_csv("birthdays.csv")

# creating a dictionary from dataframe such that its key is (month, day) and value is row of dataframe itself
dict = {(row.month,row.day):row for (index, row) in  data_frame.iterrows()}

# accessing the name of friend whose birthday is today
for (birthday_tuple, value) in dict.items():
    if birthday_tuple == today_date:
        name = dict[birthday_tuple]["name"]
        email = dict[birthday_tuple]["email"]

#getting letter ready by replacing [NAME] with the name of person whose birthday matches today
with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as letter:
    txt = ("").join(letter.readlines()).replace("[NAME]",name)

#logging in to the sender email
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=os.getenv("EMAIL"), password=os.getenv("EMAIL_PASSWORD"))

#sending letter to the email address of the friend whose birthday is today
connection.sendmail(from_addr= os.getenv("EMAIL"), to_addrs=email, msg=f"Subject:Birthday Wish\n\n{txt}")




