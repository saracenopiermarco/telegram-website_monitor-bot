import time
import threading
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import telebot

# ============================================================
# Load Telegram API token from external file (not in GitHub)
# ============================================================
def load_token():
    with open("token.secret", "r") as f:
        return f.read().strip()

API_TOKEN = load_token()
bot = telebot.TeleBot(API_TOKEN)

# ============================================================
# Data structures for monitoring and user setup flow
# ============================================================
active_monitors = {}   # user_id → (url, keyword)
user_states = {}       # user_id → {"step": "...", "url": "..."}

# ============================================================
# Extract text from a webpage (generic scraper)
# ============================================================
def extract_text(url):
    """
    Downloads the webpage and returns a compact text-only version.
    Removes scripts, styles, and collapses whitespace.
    """
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = BeautifulSoup(html, features="html.parser")

    # Remove script and style tags
    for script in soup(["script", "style"]):
        script.extract()

    # Extract visible text and collapse whitespace
    text = soup.get_text(separator=" ")
    return " ".join(text.split())

# ============================================================
# Commands
# ============================================================
@bot.message_handler(commands=['start', 'help'])
def welcome(msg):
    bot.reply_to(msg,
        "Hi! I can monitor any webpage and notify you when a keyword appears.\n\n"
        "To begin, type:\n/monitor"
    )

@bot.message_handler(commands=['monitor'])
def ask_url(msg):
    """
    Step 1 of the interactive setup.
    Ask the user for the URL to monitor.
    """
    user_states[msg.chat.id] = {"step": "waiting_url"}
    bot.reply_to(msg, "Which URL do you want to monitor?")

@bot.message_handler(commands=['stop'])
def stop_monitor(msg):
    """
    Stops monitoring for the current user.
    """
    if msg.chat.id in active_monitors:
        del active_monitors[msg.chat.id]
        bot.reply_to(msg, "Monitoring stopped.")
    else:
        bot.reply_to(msg, "You have no active monitoring tasks.")

# ============================================================
# Handle user input during the interactive setup
# ============================================================
@bot.message_handler(func=lambda m: True)
def handle_user_input(msg):
    user_id = msg.chat.id

    # If the user is not in the setup flow, ignore
    if user_id not in user_states:
        return

    state = user_states[user_id]

    # Step 1: user must send the URL
    if state["step"] == "waiting_url":
        url = msg.text.strip()
        state["url"] = url
        state["step"] = "waiting_keyword"
        bot.reply_to(msg, "Got it. Which keyword should I look for?")
        return

    # Step 2: user must send the keyword
    if state["step"] == "waiting_keyword":
        keyword = msg.text.strip()
        url = state["url"]

        # Save the monitoring task
        active_monitors[user_id] = (url, keyword)

        # Clear the state
        del user_states[user_id]

        bot.reply_to(msg, f"Monitoring started.\nURL: {url}\nKeyword: '{keyword}'")
        return

# ============================================================
# Background monitoring loop
# ============================================================
def monitor_loop():
    """
    Periodically checks all active monitors every few seconds.
    When the keyword is found, the bot notifies the user.
    """
    while True:
        time.sleep(5)

        for user_id, (url, keyword) in list(active_monitors.items()):
            try:
                text = extract_text(url)

                if keyword in text:
                    bot.send_message(
                        user_id,
                        f"🔔 Keyword found!\n'{keyword}' appeared on the page:\n{url}"
                    )
                    del active_monitors[user_id]

            except Exception as e:
                bot.send_message(user_id, f"Error while checking the page:\n{e}")
                del active_monitors[user_id]

# ============================================================
# Start background thread + polling
# ============================================================
threading.Thread(target=monitor_loop, daemon=True).start()
bot.polling(none_stop=True)
