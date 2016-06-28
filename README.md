# Introduction

A Telegram bot that detects Pokemon Go screenshots in a chat, and uses OCR to
pull useful information from the screenshot.


# Running The Bot

```
cd telegram-pokego
pip install -r requirements.txt --upgrade
echo "TOKEN = 'TELEGRAM_BOT_TOKEN'" > secrets.py
python3 pokebot.py
```
Don't forget to generate a [telegram bot](https://core.telegram.org/bots) token, and disable the privacy.

# Features
 * Pulls Pokemon, candy required to evolve, HP from screenshots
 * Saves screenshots and data to file
 * Able to detect two consecutive screenshots and determine whether they
 depict an evolve or a powerup
