import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


logging.basicConfig(
    level=logging.INFO, format="%(name)s - [%(levelname)s] - %(message)s"
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID", ""))
api_hash = os.environ.get("API_HASH", "")
bot_token = os.environ.get("TOKEN", "")
client = TelegramClient("client", api_id, api_hash).start(bot_token=bot_token)
spam_chats = []


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ɪ ᴀᴍ ᴀʟɪᴠᴇ ⚡")
    await event.reply(
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n𝐇𝐄𝐋𝐋𝐎 𝐓𝐇𝐈𝐒 𝐈𝐒 𝐆𝐑𝐎𝐔𝐏 𝐅𝐀𝐒𝐓 𝐌𝐄𝐍𝐓𝐈𝐎𝐍𝐁𝐎𝐓.\n✪ ɪ ᴀᴍ ᴛɢᴍ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴛʜᴇ ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ.\n✪ᴛʜɪꜱ ʙᴏᴛ ᴡᴏʀᴋꜱ 10ᴋ+ ᴍᴇᴍʙᴇʀꜱ ɢʀᴏᴜᴘ.\n✪ ᴜᴘᴛᴏ 20 ᴍᴇᴍʙᴇʀꜱ ᴛᴀɢ ᴀᴛ ꜱᴀᴍᴇ ᴛɪᴍᴇ.\n✪ ᴛʜᴀɴᴋs ғᴏʀ ᴜsɪɴɢ ʀᴜɴ /help..\n\n━━━━━━━━━━━━━━━━━━━━━━━━",
        link_preview=False,
        buttons=(
            [
                Button.url(
                    "➕ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ➕",
                    "https://t.me/BlooDy_sweeT_of_PrincE_boT?startgroup=true",
                ),
            ],
            [
                Button.url("ɢʀᴏᴜᴘ", "https://t.me/Alinallmovies"),
                Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/Alinallmovies"),
            ],
            [
                Button.url("⚡ ᴏᴡɴᴇʀ ⚡", "https://t.me/thavarajtj"),
            ],
        ),
    )

