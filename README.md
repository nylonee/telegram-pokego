# Introduction

A Telegram bot that detects Pokemon Go screenshots in a chat, and uses OCR to
pull useful information from the screenshot.


# Running The Bot

```
pip install -r requirements.txt --upgrade
python3 pokebot.py
```

# Features
 * Pulls Pokemon, candy required to evolve, HP from screenshots
 * Saves screenshots and data to file
 * Able to detect two consecutive screenshots and determine whether they
 depict an evolve or a powerup
