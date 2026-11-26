"""
Main Telegram Bot Application: Worldwide Country Random Name Generator
Supports:
1. First page shows 5-6 popular countries + Search button + Pagination
2. Search worldwide countries by name, code, alias (e.g. BD, USA, Japan, Germany)
3. Country selection: generate random male, female, or mixed names unlimited times
4. Interactive inline keyboards with back navigation and clean UX
"""

import html
import math
import os
import sys
import time
from typing import Dict, List, Optional

from countries_data import COUNTRIES, Country, get_country_by_code, search_countries
from name_generator import generate_names
from telegram_client import TelegramBot

# Configuration Constants (Permanently Configured)
DEFAULT_BOT_TOKEN = "9197793802:AAE1YqPe3LuoSvRgqh9dIlq1EDG7oI8WZ-4"
ADMIN_TELEGRAM_ID = 7457103363

# Number of countries per page
PAGE_SIZE = 6

# Featured countries on first page
POPULAR_CODES = ["BD", "US", "GB", "IN", "JP", "DE"]

# User states: chat_id -> dict
USER_STATES: Dict[int, Dict[str, any]] = {}

# Bot Commands List for Telegram Menu Button
BOT_COMMANDS = [
    {"command": "start", "description": "🏠 মূল মেনু / কান্ট্রি লিস্ট ওপেন করুন"},
    {"command": "search", "description": "🔍 যেকোনো দেশের নাম সার্চ করুন"},
    {"command": "popular", "description": "⭐ টপ ও জনপ্রিয় দেশসমূহ দেখুন"},
    {"command": "recents", "description": "🕒 আপনার রিসেন্ট ব্যবহৃত দেশসমূহ"},
    {"command": "help", "description": "📖 ব্যবহারের নিয়ম ও সাহায্য"},
]



def build_country_list_keyboard(page: int = 1, query: Optional[str] = None) -> Dict[str, any]:
    """Build inline keyboard for country browsing or search results."""
    if query:
        countries = search_countries(query)
    else:
        # First page highlights popular countries first
        if page == 1:
            featured = [get_country_by_code(c) for c in POPULAR_CODES if get_country_by_code(c)]
            rest = [c for c in COUNTRIES if c["code"] not in POPULAR_CODES]
            all_list = featured + rest
        else:
            featured = [get_country_by_code(c) for c in POPULAR_CODES if get_country_by_code(c)]
            rest = [c for c in COUNTRIES if c["code"] not in POPULAR_CODES]
            all_list = featured + rest
        countries = all_list

    total = len(countries)
    total_pages = max(1, math.ceil(total / PAGE_SIZE))
    page = max(1, min(page, total_pages))

    start = (page - 1) * PAGE_SIZE
    page_items = countries[start : start + PAGE_SIZE]

    keyboard: List[List[Dict[str, str]]] = []

    # Country buttons (2 columns)
    row: List[Dict[str, str]] = []
    for c in page_items:
        btn_text = f"{c['flag']} {c['name']}"
        row.append({"text": btn_text, "callback_data": f"sel:{c['code']}"})
        if len(row) == 2:
            keyboard.append(row)
            row = []
    if row:
        keyboard.append(row)

    # Navigation buttons (Previous / Page / Next)
    nav_row: List[Dict[str, str]] = []
    prefix = f"sq:{query}" if query else "page"
    if page > 1:
        nav_row.append({"text": "⬅️ Prev", "callback_data": f"{prefix}:{page - 1}"})
    nav_row.append({"text": f"📄 {page}/{total_pages}", "callback_data": "noop"})
    if page < total_pages:
        nav_row.append({"text": "Next ➡️", "callback_data": f"{prefix}:{page + 1}"})
    keyboard.append(nav_row)

    # Search and Action buttons
    action_row: List[Dict[str, str]] = [
        {"text": "🔍 Search Country", "callback_data": "search_prompt"},
    ]
    if query:
        action_row.append({"text": "🏠 Home (All)", "callback_data": "home"})
    keyboard.append(action_row)

    return {"inline_keyboard": keyboard}


def build_generator_keyboard(country_code: str, gender: str = "all") -> Dict[str, any]:
    """Keyboard for generating random names for a selected country."""
    keyboard = [
        [
            {"text": "🔄 Generate Again (5 Names)", "callback_data": f"gen:{country_code}:{gender}:5"},
            {"text": "⚡ Generate 10", "callback_data": f"gen:{country_code}:{gender}:10"},
        ],
        [
            {"text": ("✅ Both" if gender == "all" else "👥 Both"), "callback_data": f"gen:{country_code}:all:5"},
            {"text": ("✅ Male (👨)" if gender == "male" else "👨 Male"), "callback_data": f"gen:{country_code}:male:5"},
            {"text": ("✅ Female (👩)" if gender == "female" else "👩 Female"), "callback_data": f"gen:{country_code}:female:5"},
        ],
        [
            {"text": "🌍 Choose Another Country", "callback_data": "home"},
            {"text": "🔍 Search", "callback_data": "search_prompt"},
        ],
    ]
    return {"inline_keyboard": keyboard}


def render_country_screen(country_code: str, gender: str = "all", count: int = 5) -> (str, Dict[str, any]):
    country = get_country_by_code(country_code)
    if not country:
        return "❌ দেশ খুঁজে পাওয়া যায়নি!", build_country_list_keyboard()

    names = generate_names(country["pool"], count=count, gender=gender)
    names_text = "\n".join([f"• <b>{html.escape(n)}</b>" for n in names])

    gender_label = "সব (উভয়)" if gender == "all" else ("পুরুষ (Male)" if gender == "male" else "মহিলা (Female)")

    msg = (
        f"{country['flag']} <b>{html.escape(country['name'])} — নাম জেনারেটর</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🎯 <b>ফিল্টার:</b> {gender_label} | সংখ্যা: {count} টি\n\n"
        f"{names_text}\n\n"
        f"<i>💡 নিচের 'Generate Again' বাটনে ক্লিক করে আনলিমিটেড নতুন নতুন নাম পান!</i>"
    )
    return msg, build_generator_keyboard(country_code, gender)


def handle_start(bot: TelegramBot, chat_id: int):
    USER_STATES[chat_id] = {"awaiting_search": False}
    text = (
        "👋 <b>ওয়ার্ল্ডওয়াইড কান্ট্রি র্যান্ডম নেম জেনারেটর বটে স্বাগতম!</b>\n\n"
        "বিশ্বের যেকোনো দেশের মানুষের কালচারাল নাম জেনারেট করুন আনলিমিটেড।\n\n"
        "👇 নিচে পছন্দের দেশ সিলেক্ট করুন অথবা <b>🔍 Search Country</b> বাটনে সার্চ দিন:"
    )
    kb = build_country_list_keyboard(page=1)
    bot.send_message(chat_id, text, reply_markup=kb)


def handle_search_prompt(bot: TelegramBot, chat_id: int, message_id: Optional[int] = None):
    USER_STATES[chat_id] = {"awaiting_search": True}
    text = (
        "🔍 <b>দেশ সার্চ করুন:</b>\n\n"
        "আপনি যে দেশের নাম জেনারেট করতে চান তার নাম বা কোড লিখে মেসেজ পাঠান।\n"
        "যেমন: <code>Bangladesh</code>, <code>bd</code>, <code>USA</code>, <code>Japan</code>, <code>Germany</code> ইত্যাদি।"
    )
    kb = {"inline_keyboard": [[{"text": "🔙 Back to List", "callback_data": "home"}]]}
    if message_id:
        bot.edit_message_text(chat_id, message_id, text, reply_markup=kb)
    else:
        bot.send_message(chat_id, text, reply_markup=kb)


def run_bot(token: str):
    bot = TelegramBot(token)
    me = bot.get_me()
    if not me or not me.get("ok"):
        print("❌ Invalid Bot Token or network error! Please verify your token.")
        sys.exit(1)

    bot_info = me.get("result", {})
    username = bot_info.get("username", "UnknownBot")
    print(f"✅ Bot connected successfully: @{username}")

    # Register Bot Command Menu
    cmd_resp = bot.set_my_commands(BOT_COMMANDS)
    if cmd_resp and cmd_resp.get("ok"):
        print("📋 Menu commands registered successfully with Telegram!")
    else:
        print("⚠️ Could not register commands menu.")

    print("🚀 Listening for updates... Press Ctrl+C to stop.")

    offset = None
    while True:
        try:
            updates = bot.get_updates(offset=offset, timeout=25)
            for u in updates:
                offset = u["update_id"] + 1

                # Handle normal text messages
                if "message" in u:
                    msg = u["message"]
                    chat_id = msg["chat"]["id"]
                    text = msg.get("text", "").strip()

                    state = USER_STATES.get(chat_id, {})

                    if text.startswith("/start") or text.startswith("/help"):
                        handle_start(bot, chat_id)
                    elif state.get("awaiting_search") or text.startswith("/search"):
                        q = text.replace("/search", "").strip()
                        USER_STATES[chat_id]["awaiting_search"] = False
                        if not q:
                            handle_search_prompt(bot, chat_id)
                        else:
                            results = search_countries(q)
                            if not results:
                                res_text = (
                                    f"🔍 '<b>{html.escape(q)}</b>' নামে কোনো দেশ পাওয়া যায়নি!\n\n"
                                    "সঠিক ইংরেজি নাম বা কোড দিয়ে আবার চেষ্টা করুন।"
                                )
                                kb = {
                                    "inline_keyboard": [
                                        [{"text": "🔍 Try Again", "callback_data": "search_prompt"}],
                                        [{"text": "🏠 View All Countries", "callback_data": "home"}],
                                    ]
                                }
                                bot.send_message(chat_id, res_text, reply_markup=kb)
                            else:
                                res_text = f"🔍 '<b>{html.escape(q)}</b>' এর জন্য পাওয়া ফলাফল ({len(results)} টি দেশ):"
                                kb = build_country_list_keyboard(page=1, query=q)
                                bot.send_message(chat_id, res_text, reply_markup=kb)
                    else:
                        # Default fallback: treat text as a country search!
                        results = search_countries(text)
                        if results:
                            res_text = f"🔍 '<b>{html.escape(text)}</b>' এর জন্য ফলাফল ({len(results)} টি দেশ):"
                            kb = build_country_list_keyboard(page=1, query=text)
                            bot.send_message(chat_id, res_text, reply_markup=kb)
                        else:
                            handle_start(bot, chat_id)

                # Handle inline keyboard callback queries
                elif "callback_query" in u:
                    cq = u["callback_query"]
                    cq_id = cq["id"]
                    chat_id = cq["message"]["chat"]["id"]
                    message_id = cq["message"]["message_id"]
                    data = cq.get("data", "")

                    bot.answer_callback_query(cq_id)

                    if data == "noop":
                        continue
                    elif data == "home":
                        USER_STATES[chat_id] = {"awaiting_search": False}
                        text = (
                            "🌍 <b>ওয়ার্ল্ডওয়াইড কান্ট্রি র্যান্ডম নেম জেনারেটর</b>\n\n"
                            "যে দেশের নাম জেনারেট করতে চান সিলেক্ট করুন:"
                        )
                        kb = build_country_list_keyboard(page=1)
                        bot.edit_message_text(chat_id, message_id, text, reply_markup=kb)

                    elif data == "search_prompt":
                        handle_search_prompt(bot, chat_id, message_id)

                    elif data.startswith("page:"):
                        page = int(data.split(":")[1])
                        text = "🌍 <b>সব দেশের তালিকা (পৃষ্ঠা পরিবর্তন):</b>"
                        kb = build_country_list_keyboard(page=page)
                        bot.edit_message_text(chat_id, message_id, text, reply_markup=kb)

                    elif data.startswith("sq:"):
                        # Search query pagination: sq:<query>:<page>
                        parts = data.split(":")
                        query = parts[1]
                        page = int(parts[2])
                        text = f"🔍 '<b>{html.escape(query)}</b>' এর ফলাফল:"
                        kb = build_country_list_keyboard(page=page, query=query)
                        bot.edit_message_text(chat_id, message_id, text, reply_markup=kb)

                    elif data.startswith("sel:"):
                        code = data.split(":")[1]
                        text, kb = render_country_screen(code, gender="all", count=5)
                        bot.edit_message_text(chat_id, message_id, text, reply_markup=kb)

                    elif data.startswith("gen:"):
                        # gen:code:gender:count
                        parts = data.split(":")
                        code = parts[1]
                        gender = parts[2]
                        count = int(parts[3])
                        text, kb = render_country_screen(code, gender=gender, count=count)
                        bot.edit_message_text(chat_id, message_id, text, reply_markup=kb)

        except KeyboardInterrupt:
            print("\n🛑 Bot stopped by user.")
            break
        except Exception as e:
            print(f"⚠️ Polling loop error: {e}")
            time.sleep(2)


if __name__ == "__main__":
    token = os.environ.get("TELEGRAM_BOT_TOKEN") or DEFAULT_BOT_TOKEN
    if len(sys.argv) > 1:
        token = sys.argv[1]

    if token:
        run_bot(token)
    else:
        print("❌ টোকেন ছাড়া বট চালানো সম্ভব নয়!")
