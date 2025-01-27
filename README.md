# Lichess discord bot

[![Bot status widget](https://top.gg/api/widget/status/707287095911120968.svg)](https://top.gg/bot/707287095911120968)
[![Discord Bots](https://top.gg/api/widget/servers/707287095911120968.svg)](https://top.gg/bot/707287095911120968)

[Click here to invite the bot to your server!](https://discord.com/api/oauth2/authorize?client_id=707287095911120968&permissions=116800&scope=bot)

## Description
This bot integrates with the lichess.org chess website. The bot can show chess puzzles which can be solved right there in the channel! It can also retrieve ELO rankings for users, show user profiles, and connect your discord account to your lichess account for enhanced functionality!

## Default prefix
`-` (customizable)

## COMMANDS 
* `-help` or `-commands` → show list of commands
* `-lichessprefix [new prefix]` → Set a custom command prefix for your server
* `-about` → show information about the bot
* `-connect [lichess username]` → connect your Discord profile with your Lichess account.
* `-disconnect` → disconnect your Discord profile from a connected Lichess account
* `-rating [username | user url]` → show all chess ratings. When connected with `-connect` you can use this command without giving a username.
* `-rating [username | user url] [gamemode]` → retrieve the ratings for a user for a specific gamemode
* `-puzzle` → show a random lichess puzzle, or one near your puzzle rating if your Lichess account is connected using `-connect`
* `-puzzle [id]` → show a specific chess puzzle
* `-puzzle [rating1]-[rating2]` → show a random chess puzzle with a difficulty rating in a range
* `-answer [move]` → give an answer to the most recent puzzle shown in the channel
* `-bestmove` → ask for the answer for the most recent puzzle shown in the channel. If there are more steps to the puzzle, the user can continue from the next step
* `-profile [username]` → show a lichess user profile. When connected with `-connect` you can use this command without giving a username.

## Help / Contact / Issues / Requests / Collaboration
Questions, issues and requests can be posted as an issue in this repository, or posted in the [discord support server](https://discord.gg/KdpvMD72CV)

## Screenshots
![Puzzle command screenshot](/media/puzzle-example.png)

![Answer command screenshot](/media/answer-example.gif)

![Bestmove command screenshot](/media/bestmove-example.png)

![Rating command screenshot](/media/rating-example.png)

![Connect command screenshot](/media/connect-example.png)

![Profile command screenshot](/media/profile-example.png)
