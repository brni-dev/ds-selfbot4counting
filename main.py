import discord, time

channels4counting = () # A whitelist for all the counting channel ID's
TOKEN = "YourTokenHere"
def sleep(t): time.sleep(t)

class Client(discord.Client):
    async def on_ready(self):
        print(f'Selfbot {self.user} started!')
    async def on_message(self, message):
        if message.author.id != self.user.id and message.channel.id in channel4counting:
            if len(message.content) > 1999 or message.content.startswith('-'): return
            else:
                try:
                    sleep(0.3) 
                    cnvrt = int(message.content.split()[0]) + 1
                    await message.channel.send(str(cnvrt))
                    sleep(0.2)
                except: pass

try:
    Client().run(TOKEN, bot=False)
except Exception as e:
    exit(f"Error! {e}")
