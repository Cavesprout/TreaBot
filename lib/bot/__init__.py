from discord import Intents
from discord import Embed
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import CommandNotFound

from asyncio import sleep
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from glob import glob

PREFIX = "$"
OWNER_IDS = [482592062546378753]
COGS = [path.split("\\")[-1][:-3] for path in glob("./lib/cogs/*.py")]

class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)

    def ready_up(self, cog):
        setattr(self, cog, True)
        print(f" {cog} cog root ready")

    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.cogs_ready = Ready()
        self.scheduler = AsyncIOScheduler

        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

    def setup(self):
        for cog in COGS:
            self.load_extension(f"lib.cogs.{cog}")
            print(f" {cog} cog root deployed")

        print("all cog roots deployed")

    def run(self, version, version_message):
        self.VERSION = version
        self.VERSION_MESSAGE = version_message

        print("running setup...")
        self.setup()
        
        with open("lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("running bot...")
        super().run(self.TOKEN)

    async def on_connect(self):
        print("bot connected")

    async def on_disconnect(self):
        print("bot disconnected")

    async def on_ready(self):
        if not self.ready:
            self.stdout = self.get_channel(825038173981376513)

            self.ready = True
            print("bot ready")

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)

bot = Bot()