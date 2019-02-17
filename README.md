# best-memes-bot

Source code of the Telegram bot [@best_memes_bot](https://t.me/best_memes_bot)

## Table of contents

* [**The idea**](#idea)
* [**Development stage**](#stage)
* [**TODO**](#todo)
* [**Lategame**](#lategame)
* [**Changelog**](#changelog)
  * [**15-02-2019**](#15-02-19)
  * [**16-02-2019**](#16-02-19)
  * [**17-02-2019**](#17-02-19)

## The idea <a name="idea"></a>

The main idea of the bot is to have somewhere to get random and good memes. The bot started with some memes I already had (~700), and keeps track of which memes have been seen by the user so you never get a meme repeated.

It has a system that allows everybody to send their memes, and then it get aproved or rejected by me (Some mods in the future).

Since I love memes, I will post new memes kinda daily.

I would also like to implement a recommeder system so when a user requests a new meme, it will try to find a meme that the user will enjoy.

## Development stage <a name="stage"></a>

Currently the bot is in an optimal stage. There is the ability to see memes, save them, see the saved one, report memes and upload new memes.

## TODO <a name="todo"></a>

* [x] Add basic admin tools

Add the ability of ban users, send broadcast messages, restart the bot, execute python code, send messages, check for github updates.

* [x] Add basic tools

Let users contact me.

* [x] Add `/memes` command

This command will show a random meme, and an inline keyboard with three buttons: one to go to the previous seen meme, one to go to a new meme (next meme if the user used before the one to navigate to a previous meme), one to save the meme.

* [x] Add `/saved` command

This command will work as `/memes` but just navigating through the saved memes (So the user can see easily the memes he likes).

* [x] Add the 'upload meme' infrastructure

Gotta make something to let the users upload new memes.

* [x] Add creator to the memes and list of created memes to the users

As said before, I would like to let users upload memes, and if in the future I reward any of them, I will probably take that in count.

* [x] Add the reviewer to the memes

Would be nice to know who reviewed what.

* [x] Button to report a meme

A button in the memes navigation inline keyboard to allow users to report memes. When reported, the user has to explain why he reports the meme and I think the best idea is that I personally review it. This way I think I could identify if a mod isn't reviewing memes correctly.

* [x] Upload the bot strings to Transifex

Since the bot will be an open source, I would like to have the strings uploaded to Transifex, just in case someone wants to use the bot in their own language and want to help to translate it.

* [ ] Add `like` and `dislike` buttons

Would be cool to let users vote the memes and add a command to see the most voted memes.

* [ ] Add extra functionalities for admins and users

Let admins set mods and let users get their stats / info.

* [ ] Add `/fresh` command

Add a command that will only show memes uploaded in the last 48 hours.

* [ ] Let the users decide their language

Right now the bot automatically gets the user language from Telegram, but in the future would be nice to let users decide their language.

* [ ] Add categories to the memes I already have

There are a lot of memes already but none of them has a category yet.

## Lategame <a name="lategame"></a>

In the late future, and only if the bot grows enough, I would really like to implement a recommender system.

## Changelog <a name="changelog"></a>

### 15-02-2019 <a name="15-02-19"></a>

###### [1] <a name="15-02-19-1"></a>

First commit :)

###### [2] <a name="15-02-19-2"></a>

Now, when I send a meme to the bot, it is added to the database. I have also updated the memes structure to save the uploader, the reviewer and how many saves it has (despite only I can send memes yet and nobody can save 'em xD)

I have also changed the message I get with new users but I don't really like it, I have to update it yet.

The last change was in the template, changing the word of the command to make it easier the change of it while developing a new plugin based on the template.

### 16-02-2019 <a name="16-02-19"></a>

###### [1] <a name="16-02-19-1"></a>

Added admin tools for:

* Ban and unban users.
* Broadcast messages.
* Reload the bot.
* Execute code.
* Check for github updates and reload the bot if there is any.
* Send messages to certain IDs.
* Reply to users contact messages.
* Command to check admin commands.

Added user tools for:

* Contact the admins.

### 17-02-2019 <a name="17-02-19"></a>

###### [1] <a name="17-02-19-1"></a>

Tonight I have actually done a lot of work. I think the bot is actually prepared for a release. I have done:

* Now the bot no longer has the command `/meme` but `/memes`, which lets you navigate through all the memes stored in the bot, save the memes you like and report the memes you find wrong.
* Improved the `/start` message, adding an inline button that works as typing `/memes`, making it easier the first use.
* Added a `/help` command where the user can see commands he can use.
* Added a `/info` command to display a bit of info about the bot.
* Added a good report system, making it easy how to report memes, and also making it easy how to answer to the reports.
* Now users can send memes to the bot and I will be able to easily accept or decline the meme.
* Added a `/saved` command where the user can navigate through his saved memes.

The only remaining things to do are not actually that important for the early stages of the bot, so tomorrow I will start spreading the word.

###### [2] <a name="17-02-19-2"></a>

* Fixed a small typo in the bot strings + added a bit more info in the `/start` command
* Changed TODO's order to leave the undone work in the botton

###### [3] <a name="17-02-19-3"></a>

* Updated the callback_data for those that used the memes' file_id to shorter ones to prevent long file_ids creating invalid inline buttons.
* Restricted memes with file_ids longer than 62. (I haven't seen one in more than 2k file_ids but better control the posibility)

###### [4] <a name="17-02-19-4"></a>

* Updated the `/memes` command to handle correctly the use of users that have already seen all the bot memes.

###### [5] <a name="17-02-19-5"></a>

* Updated the arrows of the inline keyboard to make them easier to see
* Removed the meme file_id caption
* Updated the structure of the README