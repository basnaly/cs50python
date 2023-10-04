# MY ARTICLES APP
#### Video Demo:  https://youtu.be/wZnUGXAsPE0
Description

My application is intended to find, read and save articles.

Introduction

My application is all about articles. The idea came from my real life situation where I read some interesting articles and

later when I think about sharing them, I can't find them anymore.

Authentication

Every user can register in the app, login and logout. It allows user to save his articles, search history and more.

During user registration he must choose his username and password. Password must have at least 8 characters and consists

from lower and uppercase words, numbers and some symbols (the allowed symbols is described during registration). Also

user must type password conformation. After registration finishes the app will add the new user to the sqlite3 database

named articles.db of users consists of: user id, username and hash password of the user.

After user registered or logged into the app he can see greeting in the right upper corner. To do this, I get the username

from the database by user id.

News API

For this app I am using news api: https://newsapi.org/docs/

If you wish to run my app in your environment you should run:

export API_KEY = <your API key for news api>

And after that run:

flask run

You can see my query to news api in project/helpers.py function lookup

Application Features

The app has 3 main features which can be represented by options in the nav bar: Search history, Saved Articles, My tags.

1. Search history

All user requests to articles API are saved here. User can run the search again to see the newer articles for the same parameters: type

of articles, keyword and language. Also user can delete searches that are not relevant for him anymore.

2. Saved Articles

When user gets cards of articles, he can save it by clicking on the "Save to my articles" button of selected article's card. After that

user will get the message: "This article was successfully saved!". This article will be shown in the table on the saved article page. In each row

of this table there 3 buttons: Add, Delete and Filter.

"Add" button

This button add tag to the article. But to use it user must create his own tags (I'll descrabe this in the "My tags" section).  After user

creats his own tags and asign the tag to the article, the tag's name appears instead of "Add" button. Also near the tag appears "x" button

that allows user to delete the tag from this article.

"Delete" button

User can delete the article by clicking on the "delete" button.

"Filter" button

When user have tags he can filter the articles by tag. So user can see all articles of tag "AI" or "Cloud", for example or

all articles that he has.

3. My tags