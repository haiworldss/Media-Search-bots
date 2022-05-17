#Kanged From @TroJanZheX
from info import AUTH_CHANNEL, AUTH_USERS, CUSTOM_FILE_CAPTION, API_KEY, AUTH_GROUPS
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, filters
import re
import random
from pyrogram.errors import UserNotParticipant
from utils import get_filter_results, get_file_details, is_subscribed, get_poster
BUTTONS = {}
BOT = {}


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    clicked = query.from_user.id
    try:
        typed = query.message.reply_to_message.from_user.id
    except:
        typed = query.from_user.id
        pass
    if (clicked == typed):

        if query.data == "about":
            buttons = [
                [
                     InlineKeyboardButton('📝 Lapor Bug / Req Anime', url='https://t.me/Assistant_09474783bot'),
                     InlineKeyboardButton("❓ Tutorial", callback_data="back")
                ]
                ]
            await query.message.edit(text="<b><b>Cara Pencarian:</b>\n\n➤Pencarian bisa dilakukan dengan dua cara, yaitu dengan cara ketik langsung atau dengan mode inline. Untuk mengunakan mode inline bisa tag nama botnya lalu ketik judul anime yang ingin dicari.\n\n➤ Gunakan kata kunci untuk mempermudah pencarian: kata kunci [search query]. Contoh: Nekopoi boku.\n\n➤ kata kunci: Nekopoi, HH, Sakuracircle, sangen rips.\n\n➤ Jika pas mencari pakai kata kunci tidak ditemukan, maka tulis judulnya saja langsung di pencariannya.\n\n<b>Catatan:</b> Kalian bisa menekan tombol di bawah jika kalian menemukan bug atau mau request anime.", reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)

         
                if query.data == "back":
            buttons =                 [            [
            InlineKeyboardButton('🔎 Cari Anime', switch_inline_query_current_chat=''),
            InlineKeyboardButton('🔗 Bagikan Bot', switch_inline_query=''),
            ],
            [
            InlineKeyboardButton("❓ Tutorial", callback_data="about"),
            InlineKeyboardButton("🗣 Channel", url='https://t.me/gawrproject'),
            ]
                ]
            await query.message.edit(START_MSG, reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)
