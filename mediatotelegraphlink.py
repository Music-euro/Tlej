#Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [MediaToTelegraphLink bot by TeLe TiPs] (https://github.com/teletips/MediaToTelegraphLink-TeLeTiPs)

from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import upload_file
import os

teletips=Client(
    "MediaToTelegraphLink",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

@teletips.on_message(filters.command('start') & filters.private)
async def start(client, message):
    text = f"""
هاي {message.from_user.mention},
أنا هنا لإنشاء روابط Telegraph لملفات الوسائط الخاصة بك.

ما عليك سوى إرسال ملف وسائط صالح مباشرة إلى هذه الدردشة.
أنواع الملفات الصالحة هي "jpeg" و "jpg" و "png" و "mp4" و "gif".

لإنشاء روابط في الدردشات الجماعية ، أضفني إلى مجموعتك الفائقة وأرسل الأمر / tl كرد على ملف وسائط صالح.
🏠 | [CH](https://t.me/TELEMEX)

❤ | [DEV](https://t.me/Y_408)

🔥 | [DEV²](https://t.me/M_408)
            """
    await teletips.send_message(message.chat.id, text, disable_web_page_preview=True)
    

@teletips.on_message(filters.media & filters.private)
async def get_link_private(client, message):
    try:
        text = await message.reply("يعالج... ")
        async def progress(current, total):
            await text.edit_text(f"📥 تحميل الوسائط... {current * 100 / total:.1f}%")
        try:
            location = f"./media/private/"
            local_path = await message.download(location, progress=progress)
            await text.edit_text("📤 تحميل علي تيليجرام...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🌐 | تيليجرام لينك**:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ | فشل تحميل الملف**\n\n<i>**Reason**: {e}</i>")
            os.remove(local_path) 
            return                 
    except Exception:
        pass        

@teletips.on_message(filters.command('tl'))
async def get_link_group(client, message):
    try:
        text = await message.reply("يعالج...")
        async def progress(current, total):
            await text.edit_text(f"📥 تحميل الوسائط... {current * 100 / total:.1f}%")
        try:
            location = f"./media/group/"
            local_path = await message.reply_to_message.download(location, progress=progress)
            await text.edit_text("📤 تحميل علي تيليجرام...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🌐 | تيليجرام لينك**:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ | فشل تحميل الملف**\n\n<i>**Reason**: {e}</i>")
            os.remove(local_path) 
            return         
    except Exception:
        pass                                           

print("Bot is alive!")
teletips.run()

#Copyright ©️ 2022 TeLe TiPs. All Rights Reserved
