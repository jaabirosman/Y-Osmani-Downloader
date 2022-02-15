from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"☞︎︎︎ 𝗧𝘂𝘀𝗮𝗮𝗹𝗼:- Waxaa Marka Hore Copy soo dhahdaa Linkiga Muuqaalka Kadibna Past Dheh, 𝗖𝗮𝗮𝘄𝗶𝗻𝗮𝗮𝗱. @ReallyRibaj : https://youtu.be/PAspv-3wBlk"
    await message.reply_text(helptxt)
