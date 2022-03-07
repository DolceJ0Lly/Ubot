from telethon import TelegramClient, events, sync
from telethon import *
from datetime import datetime

import os
import asyncio
import telethon


API_ID = 1641545
API_HASH ="5e2f76a9ef8d04cb1386a9f9d246dd9f"
# prendete tutti i codici da my.telegram.org

userbot_personal = TelegramClient("userbot_personal", API_ID, API_HASH)




async def usbot():

  
  @userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.stato"))
  async def statususerbot(event):
    await event.edit("UserBot online✅")

  @userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.nome"))
  async def nameprofilyou(event):
    x = event.text.split(" ", maxsplit=1)[1]
    result = await userbot_personal(functions.account.UpdateProfileRequest(
          first_name=x,
      ))
    await event.edit(f"nome messo in **{x}**")

  @userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.ferma"))
  async def _stopuserbot(event):
    await event.edit("Fra 3 secondi andra offline l'userbot")
    await userbot_personal.disconnect()
    await asyncio.sleep(3)


  @userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.riavvia"))
  async def reboot(event):
    await event.delete()
    import os, sys, threading
    os.system("clear")
  
    os.execl(sys.executable, sys.executable, *sys.argv)
    thereading.Thread(target=_restart, args=(bot, msg)).start()


  @userbot_personal.on(events.NewMessage(outgoing=True, pattern=r".ping"))
  async def _ping(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("**Ping!**")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("**Ping!**\n`{}`".format(ms))

  @userbot_personal.on(events.NewMessage(outgoing=True))
  async def t_p(event):
    if event.text == ".lol":
      await event.edit("Non è divertente. Non ho riso. Il tuo tentativo di fare il comico è stato talmente pietoso da rendermi ancora più triste e frustrato di prima. La tua idea di scherzo è completamente fallata, le tue battute sono delle offese a livello intellettuale nei confronti di tutti i comici che a differenza tua sanno far ridere la gente. Io mi immagino te, dietro la tastiera, con un sorriso malizioso sulle labbra, pronto a scrivere questa battuta mediocre che non mi ha fatto nemmeno sorridere. Dovresti seriamente smettere di provare a far ridere la gente, perché non fa per te, non ne sei capace, non sei divertente, non sei simp, e le tue battute sono deprimenti e non fanno ridere")



  #@userbot_personal.on(events.Raw)
  #async def handler(update):
    # Print all incoming updates
    #await userbot_personal.send_message("me",update.stringify())

  @userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.delm"))
  async def _delm(event):
    await event.delete()
    d = await event.get_reply_message()
    await d.delete()
    await event.respond("Messaggio Cancellato")

  @userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.del"))
  async def _delm(event):
    await event.delete()
    d = await event.get_reply_message()
    await d.delete()

  @userbot_personal.on(events.NewMessage(outgoing=True, pattern=r"\.version_telethon"))
  async def versiontelethon(e):
    g = (telethon.__version__)
    await e.edit(f"versione di telethon -> {g}")


  
print("Userbot Personale Online!")


with userbot_personal:
  userbot_personal.loop.run_until_complete(usbot())
  userbot_personal.run_until_disconnected()

