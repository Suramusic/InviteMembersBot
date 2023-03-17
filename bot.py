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


    @client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ᴅᴇᴀʀ sᴛᴀʀᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴғ ⚡")
    helptext = "✪ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ TGM ᴍᴇɴᴛɪᴏɴ\n\nᴄᴏᴍᴍᴀɴᴅ⚡\n✪ /tgm  /mentionall /tagall  \n✪ /cancel\n✪ /admin\n\nᴄᴏᴍᴍᴀɴᴅ ᴜꜱᴇ⚡\n✪ ᴄᴏᴍᴍᴀɴᴅ: /tgm\n✪ ᴄᴏᴍᴍᴀɴᴅ: /cancel ᴛᴏ ᴄᴀɴᴄᴇʟ ɢᴏɪɴɢ ᴏɴ ᴘʀᴏᴄᴇss.\n✪ ᴄᴏᴍᴍᴀɴᴅ /admin ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴀʟʟ ᴀᴅᴍɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ\n✪ Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜ ᴛᴇxᴛ ᴡʜᴀᴛ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴏᴛʜᴇʀs.\n\n✪Example⚡\n✪ /tgm Good Morning⚡\n✪ Yᴏᴜ ᴄᴀɴ ʏᴏᴜ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴀs ᴀ ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴍᴇssᴀɢᴇ. Bᴏᴛ ᴡɪʟʟ ᴛᴀɢ ᴜsᴇʀs ᴛᴏ ᴛʜᴀᴛ ʀᴇᴘʟɪᴇᴅ ᴍᴇsssᴀɢᴇ."
    await event.reply(
        helptext,
        link_preview=False,
        buttons=(
            [
                Button.url("ɢʀᴏᴜᴘ", "https://t.me/Alinallmovies"),
                Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/Alinallmovies"),
            ]
        ),
    )


@client.on(events.NewMessage(pattern="^/owner$"))
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ᴅᴇᴀʀ sᴛᴀʀᴛ ᴍᴇ ɪɴ ᴘᴍ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴғ 🥺")
    helptext = "✪ ᴏᴡɴᴇʀ ᴍᴇɴᴜ ᴏғ 𝐏𝐑𝐈𝐍𝐂𝐄 ᴍᴇɴᴛɪᴏɴ\n\n✪ ᴍʏ ᴏᴡɴᴇʀ ɪs [ꜰᴀᴛʜᴇʀ](https://t.me/thavarajtj)\n✪ ᴍᴏᴠɪᴇ [ᴄʜᴀɴɴᴇʟ](https://t.me/Alinallmovies)."
    await event.reply(
        helptext,
        link_preview=False,
        buttons=(
            [
                Button.url("ɢʀᴏᴜᴘ", "https://t.me/Alinallmovies"),
                Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/Alinallmovies"),
            ]
        ),
    )
    
    
    @bot.on(admin_cmd(pattern="inviteall ?(.*)"))
@bot.on(sudo_cmd(pattern="inviteall ?(.*)", allow_sudo=True))
async def get_users(event):   
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        hell = await event.reply("`processing...`")
    else:
    	hell = await event.edit("`processing...`")
    legendx22 = await get_chatinfo(event) ; chat = await event.get_chat()
    if event.is_private:
              return await hell.edit("`Sorry, Can add users here`")    
    s = 0 ; f = 0 ; error = 'None'   
  
    await hell.edit("**TerminalStatus**\n\n`Collecting Users.......`")
    async for user in event.client.iter_participants(legendx22.full_chat.id):
                try:
                    if error.startswith("Too"):
                        return await hell.edit(f"**Terminal Finished With Error**\n(`May Got Limit Error from telethon Please try agin Later`)\n**Error** : \n`{error}`\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people")
                    await event.client(functions.channels.InviteToChannelRequest(channel=chat,users=[user.id]))
                    s = s + 1                                                    
                    await hell.edit(f"**Terminal Running...**\n\n• Invited `{s}` people \n• Failed to Invite `{f}` people\n\n**× LastError:** `{error}`")                
                except Exception as e:
                    error = str(e) ; f = f + 1             
    return await hell.edit(f"**Terminal Finished** \n\n• Successfully Invited `{s}` people \n• failed to invite `{f}` people")


@bot.on(admin_cmd(pattern="edd ?(.*)"))
@bot.on(sudo_cmd(pattern="edd ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await edit_or_reply(event, "`.add` users to a chat, not to a Private Message")
    else:
        logger.info(to_add_users)
        if not event.is_channel and event.is_group:
            # https://lonamiwebs.github.io/Telethon/methods/messages/add_chat_user.html
            for user_id in to_add_users.split(" "):
                try:
                    await borg(
                        functions.messages.AddChatUserRequest(
                            chat_id=event.chat_id, user_id=user_id, fwd_limit=1000000
                        )
                    )
                except Exception as e:
                    await event.reply(str(e))
            await edit_or_reply(event, "Invited Successfully")
        else:
            # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
            for user_id in to_add_users.split(" "):
                try:
                    await borg(
                        functions.channels.InviteToChannelRequest(
                            channel=event.chat_id, users=[user_id]
                        )
                    )
                except Exception as e:
                    await event.reply(str(e))
            await edit_or_reply(event, "Added user to the chat....")

   

print(">> PRINCE WORKING <<")
client.run_until_disconnected()
