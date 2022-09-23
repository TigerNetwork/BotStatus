from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    name = "RichStatus",
    api_id = "11469239",
    api_hash = "a7a24e71e12f5540d66c7f27ee0b992d",
    session_string = "BQDGUQEy208KujNyBexfvsy-FDEUyJDWQiagZlRnvh6MhFmrR1B_FuYVR1wCLie4-Njith3bswgEner2aqPuihV1u6523bdzjSeWkBC30XRQKnk4aC49h32cZYsEiMMC7a2Dz7mE8aQyyOXunmQdm7SrIj-jTqWsyyL1nwjkGS4NLgO14O3W69RfqpvukiAXf_VRDoBT4wGN-ImWRhaHL30nNcjplAnJmY8vJHmbGN9XDJ-c_gZ7xs0r1dkvg6B9simjMDUIfp_ODKDZc8xXu-aTvK4St6gUG68p66437qnfeFyZTsuGgDVI6kScrzyPuXD_F0OHyfYY3jSYvt10x-7uAAAAAUrLlYkA"
)
TIME_ZONE = "Asia/Kolkata"
BOT_LIST = [i.strip() for i in "MissRichBot".split(' ')]
CHANNEL_OR_GROUP_ID = "-1001512351197"
MESSAGE_ID = "20"
BOT_ADMIN_IDS = [int(i.strip()) for i in "5215836363 5549823369".split(' ')]

async def main_teletips():
    async with app:
            while True:
                print("Checking...")
                xxx_teletips = f"📈 | **Rᴇᴀʟ-Tɪᴍᴇ Bᴏᴛ Sᴛᴀᴛᴜs**"
                for bot in BOT_LIST:
                    try:
                        yyy_teletips = await app.send_message(bot, "/start")
                        aaa = yyy_teletips.id
                        await asyncio.sleep(10)
                        zzz_teletips = app.get_chat_history(bot, limit = 1)
                        async for ccc in zzz_teletips:
                            bbb = ccc.id
                        if aaa == bbb:
                            xxx_teletips += f"\n\n🤖  @{bot}\n        └ **Down** ❌"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"🚨 **Beep! Beep!! @{bot} is down** ❌")
                                except Exception:
                                    pass
                            await app.read_chat_history(bot)
                        else:
                            xxx_teletips += f"\n\n🤖  @{bot}\n        └ **Aʟɪᴠᴇ** ✅"
                            await app.read_chat_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                xxx_teletips += f"\n\n✔️ Lᴀsᴛ ᴄʜᴇᴄᴋᴇᴅ ᴏɴ: {last_update} ({TIME_ZONE})\n\n<i>♻️ Rᴇғʀᴇsʜᴇs ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ</i>"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_teletips)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(1800)
                        
app.run(main_teletips())

#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
