#keto
from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import authorized_users_only


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👮← مرحبآ عزيزي : 「{message.from_user.first_name} 」
🤖← اسم البوت :「 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) 」
ـــــــــــــــــــــــــــــــــــــــــــــــ
📜← مميزات البوت : يقوم بالبحث عن اي اغنيه وتشغيلها بالمكالمات لاتحتاج الئ بوت اخر لتحميل الاغاني هذا البوت فيه جميع المميزات بحث وتشغيل
لمعرفة اوامر البوت ارسل /help
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ اضفني الئ مجموعتك ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                         "", url="https://t.me/ZEPD8 
                    ),
                    InlineKeyboardButton(
                        "", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "👥 قروب السورس", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 قناة السورس", url=f"https://t.me/{UPDATES_CHANNEL}")               
                 ],[
                    InlineKeyboardButton(
                        "المـطـور 👮 ", url="t.me/iOm3y"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✔ **البوت قيد التشغيل**\n<b>☣ **مدة التشغيل:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "☢ قروب السورس", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 قناة السورس", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>مرحبآ ← {message.from_user.mention()}, يرجى النقر فوق الزر أدناه لرؤية اوامر  المساعدة التي يمكنك قراءتها لاستخدام هذا البوت ادخل خاص البوت ثم ارسل /help</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="✔ طريقة الاستخدام", url=f"https://t.me/{BOT_USERNAME}?start=help"
                    )
                ]
            ]
        )
    )

@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>مرحبآ ← {message.from_user.mention()}, أهلا بكم في قائمة الاوامر ✨
\n📙 كيف تستعملني؟
\n1. أضفني أولاً إلى مجموعتك
2. قم برفعي ادمن وأعطني كل الصلاحيات
3. ثم أضف @{ASSISTANT_NAME} إلى مجموعتك أو ارسل /userbotjoin
 4. تأكد من تشغيل الدردشة الصوتية أولاً قبل بدء تشغيل الموسيقى
\n💁🏻‍♀️ ** أوامر لجميع المستخدمين:**
\n /play (اسم الأغنية) - تشغيل الأغنية من youtube
/stream (الرد على الصوت) - تشغيل الأغنية باستخدام ملف صوتي
/playlist - إظهار أغنية القائمة في قائمة الانتظار
/song (اسم الأغنية) - تنزيل أغنية من youtube
/search (اسم الفيديو) - ابحث عن مقطع فيديو من youtube بالتفصيل
/vsong  (اسم الفيديو) - تنزيل الفيديو من youtube مفصل
/lyric - (اسم الأغنية) تنزيل الاغنية مع الكلمات
/vk (اسم الأغنية) - تنزيل الأغنية من الوضع المضمَّن
\n👷🏻‍♂️ **أوامر للادمنية:**
\n/player - افتح لوحة إعدادات مشغل الموسيقى
/pause - إيقاف تشغيل الموسيقى مؤقتًا
/resume - استئناف تم إيقاف الموسيقى مؤقتًا
/skip - انتقل إلى الأغنية التالية
/end - إيقاف تشغيل الموسيقئ
/userbotjoin - دعوة المساعد للانضمام إلى مجموعتك
/reload - لتحديث قائمة الإدارة
/cache - لمسح ذاكرة التخزين المؤقت للمشرف
/auth - المستخدم المصرح له باستخدام برنامج Music bot
/deauth - غير مصرح به لاستخدام برنامج تتبع الموسيقى
/musicplayer (on / off) - تعطيل / تمكين مشغل الموسيقى في مجموعتك
\n🎧  أوامر التشغيل بالقناة:
\n/cplay - تشغيل الموسيقى على قناة الدردشة الصوتية
/cplayer - إظهار الأغنية أثناء البث
/cpause - إيقاف الموسيقى المشغله مؤقتًا
/cresume - استئناف توقف البث مؤقتًا
/cskip - تخطي التشغيل الى الأغنية التالية
/cend - قم بإنهاء تشغيل الموسيقى
/admincache - قم بتحديث ذاكرة التخزين المؤقت للادمنية
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "☣ قروب السورس", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 قناة السورس", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "♞🏻‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/iOm3y"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("ᴘɪɴɢɪɴɢ...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "✈ `ᴘᴏɴɢ!!`\n"
        f"☣ `{delta_ping * 1000:.3f} ᴍs`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@authorized_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 حالة الـبـوت:\n"
        f"➤ **مدة التشغيل:** `{uptime}`\n"
        f"➤ **وقت التشغيل:** `{START_TIME_ISO}`"
    )
