# 🔍 Telegram Website Monitor Bot

A lightweight Telegram bot that monitors any webpage and notifies you when a chosen keyword appears.  
Built with **Python**, **BeautifulSoup**, and **pyTelegramBotAPI**, it runs locally using polling and includes an interactive setup flow.

---

## 📖 Anecdote: How This Bot Was Born

This bot has a very specific origin story.  
The idea came during the COVID pandemic in 2020, when all gyms were closed and everyone was training at home. Sports equipment on websites like Decathlon would sell out instantly — the moment new stock appeared online, it disappeared again within minutes.

With all the extra time I had at home because of the lockdown, and out of pure necessity, I created the first version of this bot. At the beginning, there was no “monitor active” message or any kind of rate‑limiting: the bot simply spammed notifications nonstop.

My house sounded like a call center, with Telegram ringing at full volume every time the keyword appeared. But it worked.

After a couple of attempts — and a lot of noise — I finally managed to buy the equipment I had been trying to get for so long.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/saracenopiermarco/telegram-website_monitor-bot.git
cd telegram-website_monitor-bot
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## 🔐 Setup
Create a file named `token.secret` in the project root:
```123456789:ABCDEF_your_telegram_bot_token_here```

## 🔐 Getting Your Telegram Bot Token

To use this project, you need a Telegram bot token.  
You can create your own bot in less than a minute using **BotFather**, the official Telegram bot for managing bots.

Follow these steps:

1. Open Telegram and search for **@BotFather**
2. Start a chat and send the command: ```/start```
3. Choose a username for your bot, create the bot and copy the token
4. Insert the bot usernam in the Telegram Search Bar, and start the bot using ```/start```.


Paste the token into a file named `token.secret`, placed in the root of the project.
⚠️ **Important:**  
> - Do NOT share your token  
> - Do NOT commit it to GitHub  
> - The file `token.secret` is already included in `.gitignore`

## 🤝 Contributing

Contributions are welcome!  
If you’d like to improve the bot, fix a bug, or propose a new feature, feel free to:

- open an issue  
- submit a pull request  
- suggest enhancements or improvements to the monitoring logic  

Please keep the code clean, documented, and consistent with the existing structure.

---

## ⭐ Support

If you find this project useful, consider giving it a ⭐ on GitHub.  
It helps visibility and encourages further development.

You can also share ideas, report issues, or suggest new features through the repository’s issue tracker.