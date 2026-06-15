#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
====================================================================
  بوت الاختبار الشامل — أساسيات الحاسوب
  Computer Fundamentals — Comprehensive Quiz Bot
  إعداد الطالب: باسم عصيد كمر / Prepared by: Basim Aseed Kamar
====================================================================

المميزات / Features:
  • عربي وإنجليزي بنفس التقسيم  /  Arabic & English, identical structure
  • تعاريف + اختيارات + صح وخطأ  /  Definitions + MCQ + True/False
  • عداد زمني 30 ثانية لكل سؤال (استبيان تيليجرام الأصلي)  /  30s timer per question
  • لوحة صدارة محفوظة  /  Persistent leaderboard
  • أيقونات شفافة (إيموجي)  /  Transparent emoji icons

التشغيل / Run:
  ضع رمز البوت في متغيّر البيئة BOT_TOKEN ثم:  python bot.py
  Set BOT_TOKEN env variable then:           python bot.py
"""

import os
import json
import random
import logging

from telegram import (
    Update,
    Poll,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    PollAnswerHandler,
    ContextTypes,
)

from questions import (
    get_questions,
    get_full_test,
    get_mid_exam,
    CATEGORY_LABELS,
    CATEGORY_ORDER,
    MIDEXAM_LABEL,
)

# --------------------------------------------------------------------
# الإعدادات / Configuration
# --------------------------------------------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "").strip()
ADMIN_CHAT_ID = os.environ.get("ADMIN_CHAT_ID", "").strip()  # اختياري / optional
QUESTION_TIME = 30           # عداد كل سؤال بالثواني / seconds per question
GAP_AFTER_ANSWER = 2         # مهلة قصيرة قبل السؤال التالي / short pause before next
LEADERBOARD_FILE = os.environ.get("LEADERBOARD_FILE", "leaderboard.json")

CREDIT = "إعداد الطالب باسم عصيد كمر · Prepared by Basim Aseed Kamar"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# --------------------------------------------------------------------
# نصوص الواجهة الثنائية / Bilingual UI strings
# --------------------------------------------------------------------
TEXT = {
    "ar": {
        "welcome": (
            "📘 *أساسيات الحاسوب — الاختبار الشامل*\n"
            "أهلاً بك 👋\n\n"
            "اختر القسم الذي تريد اختبار نفسك فيه. لكل سؤال عدّاد *30 ثانية* ⏱️\n\n"
            f"_{CREDIT}_"
        ),
        "choose_lang": "🌐 اختر اللغة / Choose language:",
        "menu": "📋 *القائمة الرئيسية*\nاختر نوع الاختبار:",
        "full": "🚀 الاختبار الشامل",
        "leaderboard_btn": "🏆 لوحة الصدارة",
        "changelang": "🌐 تغيير اللغة",
        "starting": "🚀 يبدأ الاختبار الآن! استعدّ... عندك *30 ثانية* لكل سؤال ⏱️",
        "q_counter": "السؤال {i} من {n}",
        "finish": (
            "🎯 *انتهى الاختبار!*\n\n"
            "👤 {name}\n"
            "✅ نتيجتك: *{score}* من *{total}*  ({pct}%)\n"
            "{grade}\n\n"
            "🏆 ترتيبك في لوحة الصدارة: *#{rank}*"
        ),
        "grade_excellent": "🌟 ممتاز! أداء رائع.",
        "grade_good": "👏 جيد جداً، استمر.",
        "grade_ok": "🙂 جيد، راجع الملزمة وكرّر.",
        "grade_low": "📖 راجع الملزمة وحاول مرّة ثانية، تقدر!",
        "lb_title": "🏆 *لوحة الصدارة — أفضل النتائج*\n",
        "lb_empty": "🏆 لوحة الصدارة فارغة حالياً. كن أول المتصدّرين! 🚀",
        "lb_row": "{medal} *{name}* — {pct}%  ({score}/{total})",
        "again": "🔁 إعادة الاختبار",
        "menu_btn": "📋 القائمة",
        "cancelled": "⏹️ تم إيقاف الاختبار. اكتب /start للبدء من جديد.",
        "no_active": "لا يوجد اختبار جارٍ. اكتب /start للبدء.",
        "mid_intro": (
            "📝 *امتحان الميد — أسئلة مقالية*\n"
            "اقرأ السؤال وفكّر بإجابتك، ثم اضغط *«إظهار الإجابة»* لمقارنتها بالإجابة النموذجية.\n"
            "عدد الأسئلة: {n}"
        ),
        "mid_q": "📝 *سؤال {i} من {n}*\n\n{q}",
        "mid_show": "💡 إظهار الإجابة",
        "mid_answer": "✅ *الإجابة النموذجية:*\n\n{a}",
        "mid_next": "➡️ السؤال التالي",
        "mid_done": "🎓 *انتهى امتحان الميد!*\nراجعت {n} أسئلة. بالتوفيق في امتحانك! 💪",
        "help": (
            "ℹ️ *المساعدة*\n\n"
            "/start — بدء الاختبار واختيار القسم\n"
            "/leaderboard — عرض لوحة الصدارة\n"
            "/cancel — إيقاف الاختبار الحالي\n\n"
            "لكل سؤال عدّاد 30 ثانية، والجواب الصحيح يظهر تلقائياً بعد إجابتك ✅\n\n"
            f"_{CREDIT}_"
        ),
    },
    "en": {
        "welcome": (
            "📘 *Computer Fundamentals — Comprehensive Quiz*\n"
            "Welcome 👋\n\n"
            "Pick a section to test yourself. Each question has a *30-second* timer ⏱️\n\n"
            f"_{CREDIT}_"
        ),
        "choose_lang": "🌐 Choose language / اختر اللغة:",
        "menu": "📋 *Main Menu*\nChoose a quiz type:",
        "full": "🚀 Comprehensive Test",
        "leaderboard_btn": "🏆 Leaderboard",
        "changelang": "🌐 Change language",
        "starting": "🚀 Starting now! Get ready... you have *30 seconds* per question ⏱️",
        "q_counter": "Question {i} of {n}",
        "finish": (
            "🎯 *Quiz finished!*\n\n"
            "👤 {name}\n"
            "✅ Your score: *{score}* of *{total}*  ({pct}%)\n"
            "{grade}\n\n"
            "🏆 Your leaderboard rank: *#{rank}*"
        ),
        "grade_excellent": "🌟 Excellent! Great work.",
        "grade_good": "👏 Very good, keep going.",
        "grade_ok": "🙂 Good, review the booklet and retry.",
        "grade_low": "📖 Review the booklet and try again — you can do it!",
        "lb_title": "🏆 *Leaderboard — Top Scores*\n",
        "lb_empty": "🏆 The leaderboard is empty. Be the first champion! 🚀",
        "lb_row": "{medal} *{name}* — {pct}%  ({score}/{total})",
        "again": "🔁 Play again",
        "menu_btn": "📋 Menu",
        "cancelled": "⏹️ Quiz stopped. Type /start to begin again.",
        "no_active": "No quiz in progress. Type /start to begin.",
        "mid_intro": (
            "📝 *Mid Exam — open-ended questions*\n"
            "Read the question and think about your answer, then tap *“Show answer”* "
            "to compare it with the model answer.\n"
            "Number of questions: {n}"
        ),
        "mid_q": "📝 *Question {i} of {n}*\n\n{q}",
        "mid_show": "💡 Show answer",
        "mid_answer": "✅ *Model answer:*\n\n{a}",
        "mid_next": "➡️ Next question",
        "mid_done": "🎓 *Mid exam finished!*\nYou reviewed {n} questions. Good luck on your exam! 💪",
        "help": (
            "ℹ️ *Help*\n\n"
            "/start — start the quiz and choose a section\n"
            "/leaderboard — show the leaderboard\n"
            "/cancel — stop the current quiz\n\n"
            "Each question has a 30s timer; the correct answer is revealed after you answer ✅\n\n"
            f"_{CREDIT}_"
        ),
    },
}


def t(lang, key, **kw):
    """جلب نص واجهة مع تنسيق / Fetch a UI string with formatting."""
    s = TEXT.get(lang, TEXT["en"]).get(key, "")
    return s.format(**kw) if kw else s


# --------------------------------------------------------------------
# لوحة الصدارة — تحميل وحفظ / Leaderboard — load & save
# --------------------------------------------------------------------
def load_leaderboard():
    try:
        with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_leaderboard(data):
    try:
        with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except OSError as e:
        logger.warning("Could not save leaderboard: %s", e)


def update_leaderboard(board, user_id, name, score, total):
    """يحفظ أفضل نسبة لكل مستخدم / Keep each user's best percentage."""
    pct = round(score / total * 100) if total else 0
    uid = str(user_id)
    cur = board.get(uid)
    if cur is None or pct > cur.get("pct", -1):
        board[uid] = {"name": name, "pct": pct, "score": score, "total": total}
    board[uid]["attempts"] = (cur.get("attempts", 0) + 1) if cur else 1
    save_leaderboard(board)
    return rank_of(board, uid)


def rank_of(board, uid):
    ordered = sorted(
        board.items(),
        key=lambda kv: (kv[1].get("pct", 0), kv[1].get("score", 0)),
        reverse=True,
    )
    for i, (k, _) in enumerate(ordered, start=1):
        if k == uid:
            return i
    return len(ordered)


# --------------------------------------------------------------------
# لوحات الأزرار / Keyboards
# --------------------------------------------------------------------
def lang_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📗 العربية", callback_data="lang:ar"),
         InlineKeyboardButton("📘 English", callback_data="lang:en")],
    ])


def menu_keyboard(lang):
    labels = CATEGORY_LABELS[lang]
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(t(lang, "full"), callback_data="menu:full")],
        [InlineKeyboardButton(labels["definitions"], callback_data="menu:definitions")],
        [InlineKeyboardButton(labels["mcq"], callback_data="menu:mcq")],
        [InlineKeyboardButton(labels["true_false"], callback_data="menu:true_false")],
        [InlineKeyboardButton(MIDEXAM_LABEL[lang], callback_data="menu:midexam")],
        [InlineKeyboardButton(t(lang, "leaderboard_btn"), callback_data="menu:leaderboard")],
        [InlineKeyboardButton(t(lang, "changelang"), callback_data="menu:changelang")],
    ])


def end_keyboard(lang):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(t(lang, "again"), callback_data="menu:full")],
        [InlineKeyboardButton(t(lang, "leaderboard_btn"), callback_data="menu:leaderboard"),
         InlineKeyboardButton(t(lang, "menu_btn"), callback_data="menu:open")],
    ])


# --------------------------------------------------------------------
# الأوامر / Commands
# --------------------------------------------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.pop("session", None)
    await update.message.reply_text(t("ar", "choose_lang"), reply_markup=lang_keyboard())


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ar")
    await update.message.reply_text(t(lang, "help"), parse_mode="Markdown")


async def cancel_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ar")
    session = context.user_data.get("session")
    if session and session.get("active"):
        session["active"] = False
        await update.message.reply_text(t(lang, "cancelled"))
    else:
        await update.message.reply_text(t(lang, "no_active"))


async def leaderboard_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "ar")
    await update.message.reply_text(
        render_leaderboard(context, lang), parse_mode="Markdown")


# --------------------------------------------------------------------
# معالجة الأزرار / Callback handling
# --------------------------------------------------------------------
async def on_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data.startswith("lang:"):
        lang = data.split(":", 1)[1]
        context.user_data["lang"] = lang
        await query.message.reply_text(t(lang, "welcome"), parse_mode="Markdown")
        await query.message.reply_text(t(lang, "menu"), parse_mode="Markdown",
                                       reply_markup=menu_keyboard(lang))
        return

    lang = context.user_data.get("lang", "ar")

    if data.startswith("mid:"):
        await handle_mid(update, context, lang, data.split(":", 1)[1])
        return

    action = data.split(":", 1)[1]

    if action == "changelang":
        await query.message.reply_text(t(lang, "choose_lang"), reply_markup=lang_keyboard())
        return
    if action == "open":
        await query.message.reply_text(t(lang, "menu"), parse_mode="Markdown",
                                       reply_markup=menu_keyboard(lang))
        return
    if action == "leaderboard":
        await query.message.reply_text(render_leaderboard(context, lang), parse_mode="Markdown",
                                       reply_markup=menu_keyboard(lang))
        return

    if action == "midexam":
        await start_mid_exam(update, context, lang)
        return

    # غير ذلك: بدء اختبار / otherwise: start a quiz
    if action == "full":
        items = get_full_test(lang)
    elif action in CATEGORY_ORDER:
        items = get_questions(lang, action)
    else:
        return

    await start_quiz(update, context, lang, items)


def render_leaderboard(context, lang):
    board = context.application.bot_data.setdefault("leaderboard", load_leaderboard())
    if not board:
        return t(lang, "lb_empty")
    ordered = sorted(board.values(),
                     key=lambda v: (v.get("pct", 0), v.get("score", 0)),
                     reverse=True)[:10]
    medals = ["🥇", "🥈", "🥉"] + ["▫️"] * 7
    lines = [t(lang, "lb_title")]
    for i, v in enumerate(ordered):
        lines.append(t(lang, "lb_row", medal=medals[i], name=v["name"],
                       pct=v.get("pct", 0), score=v.get("score", 0), total=v.get("total", 0)))
    return "\n".join(lines)


# --------------------------------------------------------------------
# تدفّق الاختبار / Quiz flow
# --------------------------------------------------------------------
async def start_quiz(update, context, lang, items):
    user = update.effective_user
    chat_id = update.effective_chat.id
    items = list(items)
    random.shuffle(items)

    context.user_data["session"] = {
        "lang": lang,
        "mode": "quiz",
        "items": items,
        "idx": 0,
        "score": 0,
        "answered": 0,
        "active": True,
        "awaiting_poll_id": None,
        "chat_id": chat_id,
        "user_id": user.id,
        "name": user.full_name or (user.username or "Player"),
    }
    await context.bot.send_message(chat_id, t(lang, "starting"), parse_mode="Markdown")
    await send_question(context, user.id)


async def send_question(context, user_id):
    session = get_session(context, user_id)
    if not session or not session.get("active") or session.get("mode") == "mid":
        return
    idx = session["idx"]
    items = session["items"]

    if idx >= len(items):
        await finish_quiz(context, user_id)
        return

    q = items[idx]
    lang = session["lang"]
    chat_id = session["chat_id"]
    counter = t(lang, "q_counter", i=idx + 1, n=len(items))
    question_text = f"({idx + 1}/{len(items)}) {q['q']}"

    msg = await context.bot.send_poll(
        chat_id=chat_id,
        question=question_text[:300],
        options=q["options"],
        type=Poll.QUIZ,
        correct_option_id=q["correct"],
        is_anonymous=False,
        open_period=QUESTION_TIME,
        explanation=q.get("exp", "")[:200],
        explanation_parse_mode=None,
    )
    poll_id = msg.poll.id
    session["awaiting_poll_id"] = poll_id

    polls = context.application.bot_data.setdefault("polls", {})
    polls[poll_id] = {"user_id": user_id, "correct": q["correct"], "chat_id": chat_id}

    # وظيفة احتياطية: التقدّم إذا لم يُجب خلال الوقت / fallback: advance if unanswered
    context.job_queue.run_once(
        timeout_job, QUESTION_TIME + 1,
        data={"user_id": user_id, "poll_id": poll_id},
        name=f"to_{poll_id}",
    )


async def handle_poll_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pa = update.poll_answer
    poll_id = pa.poll_id
    user_id = pa.user.id

    polls = context.application.bot_data.setdefault("polls", {})
    meta = polls.get(poll_id)
    if not meta:
        return

    session = get_session(context, user_id)
    if not session or not session.get("active"):
        return
    if session.get("awaiting_poll_id") != poll_id:
        return

    selected = pa.option_ids[0] if pa.option_ids else None
    session["answered"] += 1
    if selected == meta["correct"]:
        session["score"] += 1

    await proceed(context, user_id, poll_id)


async def timeout_job(context: ContextTypes.DEFAULT_TYPE):
    data = context.job.data
    await proceed(context, data["user_id"], data["poll_id"])


async def proceed(context, user_id, poll_id):
    """تقدّم محمي من التكرار / Guarded advance (answer OR timeout)."""
    session = get_session(context, user_id)
    if not session or not session.get("active"):
        return
    if session.get("awaiting_poll_id") != poll_id:
        return  # سبق التقدّم / already advanced

    session["awaiting_poll_id"] = None
    # إلغاء الوظيفة الاحتياطية إن وُجدت / cancel pending fallback job
    for job in context.job_queue.get_jobs_by_name(f"to_{poll_id}"):
        job.schedule_removal()

    session["idx"] += 1
    context.job_queue.run_once(
        next_job, GAP_AFTER_ANSWER,
        data={"user_id": user_id},
        name=f"next_{user_id}_{session['idx']}",
    )


async def next_job(context: ContextTypes.DEFAULT_TYPE):
    await send_question(context, context.job.data["user_id"])


async def finish_quiz(context, user_id):
    session = get_session(context, user_id)
    if not session:
        return
    session["active"] = False
    lang = session["lang"]
    chat_id = session["chat_id"]
    score = session["score"]
    total = len(session["items"])
    pct = round(score / total * 100) if total else 0

    if pct >= 90:
        grade = t(lang, "grade_excellent")
    elif pct >= 70:
        grade = t(lang, "grade_good")
    elif pct >= 50:
        grade = t(lang, "grade_ok")
    else:
        grade = t(lang, "grade_low")

    board = context.application.bot_data.setdefault("leaderboard", load_leaderboard())
    rank = update_leaderboard(board, user_id, session["name"], score, total)

    await context.bot.send_message(
        chat_id,
        t(lang, "finish", name=session["name"], score=score, total=total,
          pct=pct, grade=grade, rank=rank),
        parse_mode="Markdown",
        reply_markup=end_keyboard(lang),
    )

    # إشعار المشرف (اختياري) / optional admin notification
    if ADMIN_CHAT_ID:
        try:
            await context.bot.send_message(
                int(ADMIN_CHAT_ID),
                f"📊 {session['name']} — {score}/{total} ({pct}%) · rank #{rank}",
            )
        except Exception as e:  # noqa: BLE001
            logger.warning("Admin notify failed: %s", e)


# --------------------------------------------------------------------
# امتحان الميد (أسئلة مقالية) / Mid exam (open-ended flow)
# --------------------------------------------------------------------
async def start_mid_exam(update, context, lang):
    user = update.effective_user
    chat_id = update.effective_chat.id
    items = get_mid_exam(lang)
    context.user_data["session"] = {
        "mode": "mid",
        "lang": lang,
        "items": items,
        "idx": 0,
        "active": True,
        "chat_id": chat_id,
        "user_id": user.id,
    }
    await context.bot.send_message(chat_id, t(lang, "mid_intro", n=len(items)),
                                   parse_mode="Markdown")
    await send_mid_question(context, user.id)


async def send_mid_question(context, user_id):
    session = get_session(context, user_id)
    if not session or not session.get("active") or session.get("mode") != "mid":
        return
    idx, items, lang, chat_id = (session["idx"], session["items"],
                                 session["lang"], session["chat_id"])
    if idx >= len(items):
        session["active"] = False
        await context.bot.send_message(chat_id, t(lang, "mid_done", n=len(items)),
                                       parse_mode="Markdown", reply_markup=menu_keyboard(lang))
        return
    q = items[idx]
    kb = InlineKeyboardMarkup([[InlineKeyboardButton(
        t(lang, "mid_show"), callback_data="mid:show")]])
    await context.bot.send_message(
        chat_id, t(lang, "mid_q", i=idx + 1, n=len(items), q=q["q"]),
        parse_mode="Markdown", reply_markup=kb)


async def handle_mid(update, context, lang, sub):
    query = update.callback_query
    user_id = update.effective_user.id
    session = get_session(context, user_id)
    if not session or not session.get("active") or session.get("mode") != "mid":
        return

    if sub == "show":
        idx, items = session["idx"], session["items"]
        if idx >= len(items):
            return
        q = items[idx]
        try:
            await query.edit_message_reply_markup(reply_markup=None)
        except Exception:  # noqa: BLE001
            pass
        kb = InlineKeyboardMarkup([[InlineKeyboardButton(
            t(lang, "mid_next"), callback_data="mid:next")]])
        await query.message.reply_text(
            t(lang, "mid_answer", a=q["a"]), parse_mode="Markdown", reply_markup=kb)

    elif sub == "next":
        try:
            await query.edit_message_reply_markup(reply_markup=None)
        except Exception:  # noqa: BLE001
            pass
        session["idx"] += 1
        await send_mid_question(context, user_id)


def get_session(context, user_id):
    ud = context.application.user_data.get(user_id)
    return ud.get("session") if ud else None


# --------------------------------------------------------------------
# نقطة التشغيل / Entry point
# --------------------------------------------------------------------
def main():
    if not BOT_TOKEN:
        raise SystemExit(
            "❌ BOT_TOKEN غير مضبوط. ضع رمز البوت في متغيّر البيئة BOT_TOKEN.\n"
            "❌ BOT_TOKEN is not set. Put your bot token in the BOT_TOKEN env variable."
        )

    app = Application.builder().token(BOT_TOKEN).build()
    app.bot_data["leaderboard"] = load_leaderboard()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("cancel", cancel_cmd))
    app.add_handler(CommandHandler("leaderboard", leaderboard_cmd))
    app.add_handler(CallbackQueryHandler(on_callback))
    app.add_handler(PollAnswerHandler(handle_poll_answer))

    logger.info("Bot is running (long polling)...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
