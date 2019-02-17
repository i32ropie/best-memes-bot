# best-memes-bot

Source code of the Telegram bot [@best_memes_bot](https://t.me/best_memes_bot)

## The idea

The main idea of the bot is to have somewhere to get random memes. The bot starts with some memes I already had (~700), and keep track of which memes have been seen by the user so you never get a meme repeated. The idea is to have a system that allows everybody to send their memes, and then it get aproved or rejected by some mod. I would also like to implement a recommeder system so when a user request a new meme, it will try to a meme that the user will enjoy.

The new memes flow would go as:

- A user sends a new meme to the bot
- A mod accepts or declines it
- If it is accepted, the mod should provide some tags, which will be the categories
- If it is declined, the mod will provide a reason why
- The user that sends the meme gets notified wether the bot was aproved or declined (and why)

I would actually like to store the reviewer of every meme, and also link the meme to the user that uploaded it so in the future I can get some stats and maybe reward the users that upload the most memes.

## Development stage

The bot is currently in an early stage of the development, I actually just started the bot yesterday (13-02-2019) and there is a lot of work to do. It just let users register with `/start` and `/stop` and send a random meme with `/meme` (This already stores the meme as seen by the user and also increases the views count on the meme).

## TODO

- [x] Add basic admin tools

Add the ability of ban users, send broadcast messages, restart the bot, execute python code, send messages, check for github updates.

- [x] Add basic tools

Let users contact me.

- [x] Add `/memes` command

This command will show a random meme, and an inline keyboard with three buttons: one to go to the previous seen meme, one to go to a new meme (next meme if the user used before the one to navigate to a previous meme), one to save the meme.

- [x] Add `/saved` command

This command will work as `/memes` but just navigating through the saved memes (So the user can see easily the memes he likes).

- [x] Add the 'upload meme' infrastructure

Gotta make something to let the users upload new memes.

- [x] Add creator to the memes and list of created memes to the users

As said before, I would like to let users upload memes, and if in the future I reward any of them, I will probably take that in count.

- [x] Add the reviewer to the memes

Would be nice to know who reviewed what.

- [x] Button to report a meme

A button in the memes navigation inline keyboard to allow users to report memes. When reported, the user has to explain why he reports the meme and I think the best idea is that I personally review it. This way I think I could identify if a mod isn't reviewing memes correctly.

- [ ] Add extra functionalities for admins and users

Let admins set mods and let users get their stats / info.

- [ ] Upload the bot strings to Transifex

Since the bot will be an open source, I would like to have the strings uploaded to Transifex, just in case someone wants to use the bot in their own language and want to help to translate it.

- [ ] Let the users decide their language

Right now the bot automatically gets the user language from Telegram, but in the future would be nice to let users decide their language.

- [ ] Add categories to the memes I already have

I just added ~700 memes but none of them have any category yet.

## Lategame

In the late future, and only if the bot grows enough, I would really like to create a recommender system.

## Changelog

### 17-02-2019 | 3

- Updated the callback_data for those that used the memes' file_id to shorter ones to prevent long file_ids creating invalid inline buttons.
- Restricted memes with file_ids longer than 62. (I haven't seen one in more than 2k file_ids but better control the posibility)

### 17-02-2019 | 2

- Fixed a small typo in the bot strings + added a bit more info in the `/start` command
- Changed TODO's order to leave the undone work in the botton

### 17-02-2019

Tonight I have actually done a lot of work. I think the bot is actually prepared for a release. I have done:

- Now the bot no longer has the command `/meme` but `/memes`, which lets you navigate through all the memes stored in the bot, save the memes you like and report the memes you find wrong.
- Improved the `/start` message, adding an inline button that works as typing `/memes`, making it easier the first use.
- Added a `/help` command where the user can see commands he can use.
- Added a `/info` command to display a bit of info about the bot.
- Added a good report system, making it easy how to report memes, and also making it easy how to answer to the reports.
- Now users can send memes to the bot and I will be able to easily accept or decline the meme.
- Added a `/saved` command where the user can navigate through his saved memes.

The only remaining things to do are not actually that important for the early stages of the bot, so tomorrow I will start spreading the word.

### 16-02-2019

Added admin tools for:

- Ban and unban users.
- Broadcast messages.
- Reload the bot.
- Execute code.
- Check for github updates and reload the bot if there is any.
- Send messages to certain IDs.
- Reply to users contact messages.
- Command to check admin commands.

Added user tools for:

- Contact the admins.

### 15-02-2019 | 2

Now, when I send a meme to the bot, it is added to the database. I have also updated the memes structure to save the uploader, the reviewer and how many saves it has (despite only I can send memes yet and nobody can save 'em xD)

I have also changed the message I get with new users but I don't really like it, I have to update it yet.

The last change was in the template, changing the word of the command to make it easier the change of it while developing a new plugin based on the template.

### 15-02-2019

First commit :)