# best-memes-bot
Source code of the Telegram bot [@best_memes_bot](https://t.me/best_memes_bot)

# The idea
The main idea of the bot is to have somewhere to get random memes. The bot starts with some memes I already had (~700), and keep track of which memes have been seen by the user so you never get a meme repeated. The idea is to have a system that allows everybody to send their memes, and then it get aproved or rejected by some mod. I would also like to implement a recommeder system so when a user request a new meme, it will try to a meme that the user will enjoy.

The new memes flow would go as:

- A user sends a new meme to the bot
- A mod accepts or declines it
- If it is accepted, the mod should provide some tags, which will be the categories
- If it is declined, the mod will provide a reason why
- The user that sends the meme gets notified wether the bot was aproved or declined (and why)

I would actually like to store the reviewer of every meme, and also link the meme to the user that uploaded it so in the future I can get some stats and maybe reward the users that upload the most memes.

# Development stage

The bot is currently in an early stage of the development, I actually just started the bot yesterday (13-02-2019) and there is a lot of work to do. It just let users register with `/start` and `/stop` and send a random meme with `/meme` (This already stores the meme as seen by the user and also increases the views count on the meme).

# TODO

- [ ] Add basic admin tools

Add the ability of ban users, send broadcast messages, restart the bot, execute python code, send messages, check for github updates, mod people etc.

- [ ] Add basic tools

Let users contact me, get bot stats and their own info.

- [ ] Add `/memes` command

This command will show a random meme, and an inline keyboard with three buttons: one to go to the previous seen meme, one to go to a new meme (next meme if the user used before the one to navigate to a previous meme), one to save the meme.

- [ ] Add `/saved` command

This command will work as `/memes` but just navigating through the saved memes (So the user can see easily the memes he likes).

- [ ] Upload the bot strings to Transifex

Since the bot will be an open source, I would like to have the strings uploaded to Transifex, just in case someone wants to use the bot in their own language and want to help to translate it.

- [ ] Let the users decide their language

Right now the bot automatically gets the user language from Telegram, but in the future would be nice to let users decide their language.

- [ ] Add categories to the memes I already have

I just added ~700 memes but none of them have any category yet.

- [ ] Add the 'upload meme' infrastructure

Gotta make something to let the users upload new memes.

- [ ] Add creator to the memes and list of created memes to the users

As said before, I would like to let users upload memes, and if in the future I reward any of them, I will probably take that in count.

- [ ] Add the reviewer to the memes

Would be nice to know who reviewed what.

- [ ] Button to report a meme

A button in the memes navigation inline keyboard to allow users to report memes. When reported, the user has to explain why he reports the meme and I think the best idea is that I personally review it. This way I think I could identify if a mod isn't reviewing memes correctly.

# Lategame

In the late future, and only if the bot grows enough, I would really like to create a recommender system.

# Changelog

## 15-02-2019
First commit :)