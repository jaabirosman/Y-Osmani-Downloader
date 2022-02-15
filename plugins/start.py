from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel🔔", url="https://t.me/osmanibots")],
        [InlineKeyboardButton(
            "Support🇸🇴 ", url="https://t.me/osmanigroupbot")]
    ])
    welcomed = f"👋 Salama <b>{message.from_user.first_name} Sida Muuqaal Loola Dago Botkaan Gudihiisa Adigoo Adeegsanaya Tusalayasha aan bixinay Y-Osmani Downloader Caawinaad By @ReallyRibaj , Linkiga Muqaalka Copy Sodheh Sidaan oo kale ☞︎︎︎.</b>\n/help Eeg Tusalan"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
