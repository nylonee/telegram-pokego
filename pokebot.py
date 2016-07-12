# image processing dependencies
from PIL import Image
import pytesseract
from processor import ImageProcessor
from pokemon_guesser import PokeGuesser

# telegram bot dependencies
import telepot, telepot.aio
try:
    from secrets import TOKEN
except ImportError:
    print("ERROR - Cannot find secrets.py.")
    print("Create a secrets.py that includes:")
    print("TOKEN = \"YOUR-TELEGRAM-BOT-TOKEN\"")
    exit(1)

# system dependencies
import ast, requests
import re, time, asyncio

class PokeBot(telepot.aio.Bot):
    def __init__(self, *args, **kwargs):
        super(PokeBot, self).__init__(*args, **kwargs)
        self._answerer = telepot.aio.helper.Answerer(self)
        self.im = ImageProcessor("pokemon.txt")
        self.pokedex = PokeGuesser()

    def regex_match(self, regex, text):
        match = re.search(regex, text)
        return match.group(1) if match else None

    async def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)

        if content_type == 'photo':
            await self.handle_evolve_or_powerup(msg, chat_id)

    async def handle_evolve_or_powerup(self, msg, chat_id):

        # download the photo for offline image processing
        file_id = str(msg['photo'][len(msg['photo'])-1]['file_id'])
        await bot.download_file(file_id, '{}.jpg'.format(file_id))

        # run photo through image processor and get data of last two images
        last = self.im.get_last_line()
        new = self.im.process_photo('{}.jpg'.format(file_id), {'user':msg['from']['id']})
        print(new)

        # upload pokemon line and HP to the public sheet
        # note: will fail if pokemon line or HP could not be pulled
        # view all responses here: https://goo.gl/XJZeof
        """try:
            pikaform = 'https://docs.google.com/forms/d/1J1WYkqPPu4z2grgy5MjPZ--qzHQZcJliOL1hqrR49K8/formResponse'
            requests.post(pikaform, {'entry.1962155915': str(new['pokemon']), 'entry.129956651': int(new['hp'])})
        except TypeError:
            pass"""

        try:
            if(int(last['hp']) < int(new['hp']) and
                    str(last['user']) == str(msg['from']['id']) and
                    str(last['pokemon']) == str(new['pokemon'])):

                before_pokemon = self.pokedex.guess_pokemon(last['pokemon'], last['evolve'], last['candy'])
                after_pokemon = self.pokedex.guess_pokemon(new['pokemon'], new['evolve'], new['candy'])

                if(before_pokemon == after_pokemon):
                    await self.sendMessage(chat_id, "{0} ({1}HP) -> {0} ({2}HP) powerup recorded".format(
                            before_pokemon, last['hp'], new['hp']))
                else:
                    await self.sendMessage(chat_id, "{0} ({1}HP) -> {2} ({3}HP) evolve recorded".format(
                            before_pokemon, last['hp'], after_pokemon, new['hp']))
        except TypeError:
            return

bot = PokeBot(TOKEN)
loop = asyncio.get_event_loop()
loop.create_task(bot.message_loop())
print("Bot started!")
loop.run_forever()
