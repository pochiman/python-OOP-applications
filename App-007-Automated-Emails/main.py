import yagmail
import pandas 
from news import NewsFeed
import datetime
import time

while True:
    if datetime.datetime.now().hour == 22 and datetime.datetime.now().minute == 18:
        df = pandas.read_excel('people.xlsx')

        for index, row in df.iterrows():
            today = datetime.datetime.now().strftime('%Y-%m-%d') 
            yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
            news_feed = NewsFeed(interest=row['interest'],
                                 from_date=yesterday,
                                 to_date=today)

            email = yagmail.SMTP(user='YOUREMAIL@gmail.com', password='YOURPASSWORD')
            email.send(to=row['email'],
                       subject=f"Your {row['interest']} news for today!",
                       contents=f"Hi {row['name']}\n See what's on about {row['interest']} today. \n{news_feed.get()}\nPönch")

    time.sleep(60)
