import telebot
from telebot import types
import time

def token_keep():
    token = '1208007811:AAG9HB_UhErwoOUPezJW2do_l3OdnCSX-KA'
    return token
bot = telebot.TeleBot(token_keep())
bot.get_me()

Mutaxasis_dict = {}

class Mutaxasis():
    def __init__(self, fullname):
        self.fullname = fullname
        self.age = None
        self.state = None
        self.city = None
        self.contact = None
        self.email = None
        self.price = None
        self.profession = None
        self.profession_type = None
        self.time_support = None
        self.goal = None
        self.img = None


current_date = time.strftime('%d-%m-%Y')  # format: 21-04-2020


@bot.message_handler(func=lambda message: True, commands=['start'])
def welcome(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    username = message.chat.username
    bot.send_message(chat_id, 'Assalomu aleykum bu yerdan siz O`zbekistonlik mutaxasislarni ochiq ma`lumotlarini '
                              'topasiz. E\'lon qoldirish uchun /register burug\'ini bosing. MutaxasislarUZ '
                              'loyihasi  <a href="http://t.me/Dasturchilar_comunity">Dasturchilar Comunity</a> '
                              'faollari tomonidan tashkillashtirildi.',
                     parse_mode='html')

    bot.send_message('-1001453835973', f'#{user_id} {message.chat.first_name}')


@bot.message_handler(commands=['register'])
def register(message):
    chat_id = message.chat.id
    m = message.text

    msg = bot.send_message(chat_id, '👤 *Mutaxasis*\n\n'
                                    'ism\, familiyani yozing\.\n'
                                    'Masalan: Davlatov Jasur',
                           parse_mode='MarkdownV2')
    bot.register_next_step_handler(msg, register_fullname)


def register_fullname(message):
    chat_id = message.chat.id
    fullname = message.text
    try:
        mutaxasis = Mutaxasis(fullname)
        Mutaxasis_dict[chat_id] = mutaxasis
        msg = bot.send_message(chat_id, '🌐 *Yosh*\n\n'
                                        'yoshingiz masalan: 23',
                               parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, register_age)
    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi boshidan ro`yhatdan o\'ting /register')


def register_age(message):
    try:
        chat_id = message.chat.id
        age = message.text
        if not age.isdigit():
            msg = bot.reply_to(message, 'Yosh faqat raqam bilan bo`lishi kerak. Necha yoshda siz?')
            bot.register_next_step_handler(msg, register_age)
            return

        mutaxasis = Mutaxasis_dict[chat_id]
        mutaxasis.age = age

        msg = bot.send_message(chat_id, '🇺🇿 *Manzil* \n\n'
                                        'Qaysi viloyatdansiz masalan: Qashqadaryo\.',
                               parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, register_state)
    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi boshidan ro`yhatdan o\'ting /register')


def register_state(message):
    chat_id = message.chat.id
    state = message.text
    try:
        mutaxasis = Mutaxasis_dict[chat_id]
        mutaxasis.state = state

        msg = bot.send_message(chat_id, '🇺🇿 *Manzil:*\n\n'
                                        'Qaysi shahar\, tuman yoki qishloq masalan Qarshi',
                               parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, register_city)
    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi boshidan ro`yhatdan o\'ting /register')


def register_city(message):
    chat_id = message.chat.id
    city = message.text
    try:
        mutaxasis = Mutaxasis_dict[chat_id]
        mutaxasis.city = city

        msg = bot.send_message(chat_id, '📞 *Telefon:*\n\n'
                                        'Telefon raqamingiz masalan \+998901234567\n'
                                        '❗️Diqqat contact ko\'rinishida yubormang',
                             parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, register_contact)
    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi boshidan ro`yhatdan o\'ting /register')


def register_contact(message):
    chat_id = message.chat.id
    contact = message.text
    try:
        mutaxasis = Mutaxasis_dict[chat_id]
        mutaxasis.contact = contact

        msg = bot.send_message(chat_id, '📧 *Email*\n\n'
                                        'emailingizni yuboring\n'
                                        '❗️Diqqat agar emailingiz bo\`lmasa yo\'q deb yuboring',
                               parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, register_email)
    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi kontaktda boshidan ro`yhatdan o\'ting /register')


def register_email(message):
    chat_id = message.chat.id
    email = message.text
    try:
        mutaxasis = Mutaxasis_dict[chat_id]
        mutaxasis.email = email

        msg = bot.send_message(chat_id, '🤝 *Narh:*\n\n'
                                        'Xurmatli mutaxasis to\'lov summasini kiriting\n'
                                        'masalan $100 yoki 1000000 '
                                        'yoki Tekin',
                               parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, register_price)
    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi  boshidan ro`yhatdan o\'ting /register')


def register_price(message):
    chat_id = message.chat.id
    price = message.text
    try:
        mutaxasis = Mutaxasis_dict[chat_id]
        mutaxasis.price = price

        msg = bot.send_message(chat_id, '🎓 *Kasb*\n\n'
                                        'Xurmatli mutaxasis Kasbingiz nima?\n'
                                        'masalan: Dasturchi Dizayner O\'qtuvchi',
                               parse_mode='MarkdownV2')


        bot.register_next_step_handler(msg, register_profession)
    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi  boshidan ro`yhatdan o\'ting /register')


def register_profession(message):
    chat_id = message.chat.id
    profession = message.text
    try:
        mutaxasis = Mutaxasis_dict[chat_id]
        mutaxasis.profession = profession

        msg = bot.send_message(chat_id, f'🎓 *{mutaxasis.profession}*\n\n'
                                        f'Qaysi yo\'nalish bo\'yicha malakangiz?\n'
                                        f'masalan: Python Java OOP 3D Fizika Matematika English\n'
                                        f'❗ Diqqat vergul qo\'ymasdan',
                               parse_mode='MarkdownV2')

        bot.register_next_step_handler(msg, register_profession_type)
    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi  boshidan ro`yhatdan o\'ting /register')


def register_profession_type(message):
    chat_id = message.chat.id
    profession_type = message.text
    try:
        mutaxasis = Mutaxasis_dict[chat_id]
        mutaxasis.profession_type = profession_type

        msg = bot.send_message(chat_id, '⏰ *Murojaat qilish vaqti:*\n\n'
                                        'Xurmatli mutaxasis murojaat vaqti?\n'
                                        'masalan 08:00 \- 06:00',
                               parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, register_time_support)
    except Exception as e:
        bot.reply_to(message, 'Xatolik yuz berdi  boshidan ro`yhatdan o\'ting /register')


def register_time_support(message):
    chat_id = message.chat.id
    time_support = message.text
    try:
        mutaxasis = Mutaxasis_dict[chat_id]
        mutaxasis.time_support = time_support

        msg = bot.send_message(chat_id, '🔍 *Maqsad:*\n\n'
                                        'Xurmatli mutaxasis maqsadingiz?\n'
                                        'masalan: Yaxshi jamoada ishlab tajribamni '
                                        'ortirish va katta loyihalarni ishlab chiqish\.',
                               parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, register_goal)
    except Exception as e:
        bot.reply_to(message, 'Xatolik yuz berdi  boshidan ro`yhatdan o\'ting /register')


def register_goal(message):
    chat_id = message.chat.id
    goal = message.text
    try:
        mutaxasis = Mutaxasis_dict[chat_id]
        mutaxasis.goal = goal

        msg = bot.send_message(chat_id, '🏞 *Shaxsiy Rasm*\n\n'
                                        'Xurmatli mutaxasis Rasmingizni yuboring\.\n'
                                        '❌ Diqqat rasmni document usulida tashlamang',
                               parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, register_img)
    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi  boshidan ro`yhatdan o\'ting /register')


all_ok_m = types.ReplyKeyboardMarkup(resize_keyboard=True)
delete = types.KeyboardButton('❌ Yo\'q')
done = types.KeyboardButton('✅ Ha')
all_ok_m.add(delete, done)

remove_keys = types.ReplyKeyboardRemove()


# def del_message(message):
#     chat_id = message.chat.id
#     mes_id = message.message_id
#     bot.delete_message(chat_id, mes_id)
#     return

@bot.message_handler(func=lambda message:True, content_types=['photo'])
def register_img(message):
    chat_id = message.chat.id
    username = message.chat.username

    try:
        img = message.photo[-1].file_id
        mutaxasis = Mutaxasis_dict[chat_id]
        mutaxasis.img = img

        is_username = f'💬 Telegram: @{username}\n'
        none = ''
        # admin kanalga
        # bot.send_photo('-1001453835973', photo=img,
        #                caption=f'<b>Mutaxasis ma\'lumotlari 👨‍💻👩‍💻</b>\n'
        #                        f'{current_date}\n\n'
        #                        f'👤 Mutaxasis: <b>{mutaxasis.fullname}</b>\n'
        #                        f'🎓 {mutaxasis.profession}: <b>{mutaxasis.profession_type}</b>\n'
        #                        f'🇺🇿 Manzil: {mutaxasis.state} vil. {mutaxasis.city}\n'
        #                        f'{is_username if username else none}'
        #                        f'📞 Telefon: {mutaxasis.contact}\n'
        #                        f'📧 Email: <b>{mutaxasis.email}</b>\n'
        #                        f'🤝 Narh:   <b>{mutaxasis.price}</b>\n'
        #                        f'🌐 Yoshi:   {mutaxasis.age}\n'
        #                        f'⏰ Murojaat qilish vaqti: {mutaxasis.time_support}\n'
        #                        f'🔍 Maqsad: {mutaxasis.goal}\n\n\n'
        #                        f'#{mutaxasis.profession} #{mutaxasis.profession_type} \n'
        #                        f'#{mutaxasis.state} #{mutaxasis.city} #Yoshi_{mutaxasis.age}\n\n'
        #                        f'✅ @MutaxasisUZ | Ochiq ma\'lumotlar'
        #
        #                ,parse_mode='html')
        # foydalanuvchiga
        bot.send_photo(chat_id, photo=img,
                       caption=f'<b>Mutaxasis ma\'lumotlari 👨‍💻👩‍💻</b>\n'
                               f'{current_date}\n\n'
                               f'👤 Mutaxasis: <b>{mutaxasis.fullname}</b>\n'
                               f'🎓 {mutaxasis.profession}: <b>{mutaxasis.profession_type}</b>\n'
                               f'🇺🇿 Manzil: {mutaxasis.state} vil. {mutaxasis.city}\n'
                               f'{is_username if username else none}'
                               f'📞 Telefon: {mutaxasis.contact}\n'
                               f'📧 Email: <b>{mutaxasis.email}</b>\n'
                               f'🤝 Narh:   <b>{mutaxasis.price}</b>\n'
                               f'🌐 Yoshi:   {mutaxasis.age}\n'
                               f'⏰ Murojaat qilish vaqti: {mutaxasis.time_support}\n'
                               f'🔍 Maqsad: {mutaxasis.goal}\n\n\n'
                               f'#{mutaxasis.profession}',
                       parse_mode='html')

        msg = bot.send_message(chat_id, f'👇 Xurmatli {mutaxasis.fullname} ma\'lumotlaringiz to\'g\'ri ekanligini '
                                        f'tastiqlang! ',
                               reply_markup=all_ok_m)
        # send_to_admin
        bot.register_next_step_handler(msg, send_to_adminn)

        # bot.delete_message(chat_id, mes_id)
    except Exception as e:
        bot.reply_to(message, 'Xatolik yuz berdi rasmni yuklashda boshidan ro`yhatdan o\'ting /register')

# def mes_step(message):
#     mes_id = message.message_id
#     chat_id = str(message.chat.id)
#
#     bot.register_next_step_handler(mes_id, send_to_admin)
#
#     user = mes_dict[chat_id]
#     user.mes_idc = mes_id

@bot.message_handler(func=lambda message: True)
def send_to_adminn(message):
    call_id = message.chat.id
    q = message.text
    username = message.chat.username

    try:
        is_username = f'💬 Telegram: @{username}\n'
        none = ''
        mutaxasis = Mutaxasis_dict[call_id]
        if q == '❌ Yo\'q':
            mes = bot.send_message(call_id, 'Juda sos ma\'lumotlaringiz yuborilmadi.'
                                            'Qaytatdan ro\'yhatdan o\'tish uchun /register',
                                   reply_markup=remove_keys)


        elif q == '✅ Ha':

            bot.send_photo('-1001453835973', photo=mutaxasis.img,
                           caption=f'<b>Mutaxasis ma\'lumotlari 👨‍💻👩‍💻</b>\n'
                                   f'{current_date}\n\n'
                                   f'👤 Mutaxasis: <b>{mutaxasis.fullname}</b>\n'
                                   f'🎓 {mutaxasis.profession}: <b>{mutaxasis.profession_type}</b>\n'
                                   f'🇺🇿 Manzil: {mutaxasis.state} vil. {mutaxasis.city}\n'
                                   f'{is_username if username else none}'
                                   f'📞 Telefon: {mutaxasis.contact}\n'
                                   f'📧 Email: <b>{mutaxasis.email}</b>\n'
                                   f'🤝 Narh:   <b>{mutaxasis.price}</b>\n'
                                   f'🌐 Yoshi:   {mutaxasis.age}\n'
                                   f'⏰ Murojaat qilish vaqti: {mutaxasis.time_support}\n'
                                   f'🔍 Maqsad: {mutaxasis.goal}\n\n\n'
                                   f'#{mutaxasis.profession} #{mutaxasis.profession_type} \n'
                                   f'#{mutaxasis.state} #{mutaxasis.city} #Yoshi_{mutaxasis.age}\n\n'
                                   f'✅ @MutaxasislarUZ | Ochiq ma\'lumotlar'

                           , parse_mode='html')

            bot.send_message(call_id, f'{mutaxasis.fullname} sizning ma\'lumotlaringiz adminga yuborildi ✅\n'
                                      f'E\'lon qoldirganingiz uchun rahmat E\'loningiz 24-48 soat ichida admin '
                                      f'tomonidan ko`rib chiqiladi va qo\'yiladi.\n'
                                      f'E`lon uchun /register',
                             reply_markup=remove_keys)

    except Exception as e:
        bot.send_message(call_id, 'Xatolik yuz berdi agar ro`yhatdan o`tmagan bo`lsangiz qaytatdan urunib '
                                  'ko`ring /register',
                         reply_markup=remove_keys)



bot.enable_save_next_step_handlers(delay=5)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

bot.polling(none_stop=True, interval=0, timeout=0)
