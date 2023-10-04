# MY ARTICLES APP
#### Video Demo:  https://youtu.be/wZnUGXAsPE0
#### Description:
My application is intended to find, read and save articles.

My application is all about articles. The idea came from my real life situation where I read some interesting articles and
later when I think about sharing them, I can't find them anymore.

Every user can register in the app, login and logout. It allows user to save his articles, search history and more.
During user registration he must choose his username and password. Password must have at least 8 characters and consists
from lower and uppercase words, numbers and some symbols (the allowed symbols is described during registration). Also
user must type password conformation. After registration finishes the app will add the new user to the sqlite3 database
named articles.db of users consists of: user id, username and hash password of the user.

After user registered or logged into the app he can see greeting in the right upper corner. To do this, I get the username
from the database by user id.

The app has 3 main features which can be represented by options in the nav bar: Search history, Saved Articles, My tags.

# 1.

In this app I can search articles by keyword or phrase, save them to my local account and get back to them whenever i want.
You also have history of your searches that you can clean and rerun again.