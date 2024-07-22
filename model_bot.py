import telebot
from telebot import types
import time


# Bot Telegram API key ***
def token_keep():
    token = '7264152538:AAELpQRzr1KrGJbBaPZgodmWat5X0jTtiZc'
    return token


bot = telebot.TeleBot(token_keep())

bot.get_me()

model_dict = {}


# model attributes
class Model:
    def __init__(self, customer):
        self.customer = customer
        self.model_name = None
        self.fi_date = None
        self.count = None
        self.model_ld = None
        self.model_fit = None
        self.model_bulk = None
        self.model_print = None
        self.model_pps = None
        self.harvested = None
        self.printed = None
        self.stichted = None
        self.packaged = None
        self.total_box = None
        self.img = None


# current time
current_date = time.strftime('%d-%m-%Y')  # format: 21-04-2020


# command start
@bot.message_handler(func=lambda message: True, commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Assalomu aleykum bu yerdan siz modellar ma`lumotlarini '
                              'topasiz. model yaratish uchun /register buyrug\'ini bosing.',
                     parse_mode='html')

    # bot.send_message('-1001453835973', f'#{user_id} {message.chat.first_name}')


# model register starting here customer name
@bot.message_handler(commands=['register'])
def register(message):
    chat_id = message.chat.id

    msg = bot.send_message(chat_id, '*Mijoz nomi:*\n'
                                    'Masalan: Bellatika',
                           parse_mode='MarkdownV2')
    bot.register_next_step_handler(msg, register_customer)


# model name
def register_customer(message):
    chat_id = message.chat.id
    customer = message.text
    # try:
    model = Model(customer)
    model_dict[chat_id] = model
    msg = bot.send_message(chat_id, '*model nomi:*\n\n',
                           parse_mode='MarkdownV2')
    bot.register_next_step_handler(msg, register_model_name)
    # except Exception:
    #     bot.reply_to(message, 'Xatolik yuz berdi boshidan ro`yhatdan o\'ting /register 0')


# model fi date
def register_model_name(message):
    model_name = message.text
    try:
        chat_id = message.chat.id
        model = model_dict[chat_id]
        model.model_name = model_name

        msg = bot.send_message(chat_id, '*FI Sanasi:* \n\n',
                               parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, register_fit_date)
    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi boshidan ro`yhatdan o\'ting /register 1')


# model count
def register_fit_date(message):
    chat_id = message.chat.id
    count = message.text

    try:
        model = model_dict[chat_id]
        model.count = count

        msg = bot.send_message(chat_id, '*Miqdori:*\n\n',
                               parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, register_count)
    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi boshidan ro`yhatdan o\'ting /register 2')


# model L/D
def register_count(message):
    chat_id = message.chat.id

    try:
        model = model_dict[chat_id]
        model.model_ld = message.text

        msg = bot.send_message(chat_id, '*Namuna L/D:*\n\n',
                               parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, register_model_ld)
    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi boshidan ro`yhatdan o\'ting /register 3')


# model FIT
def register_model_ld(message):
    chat_id = message.chat.id

    try:
        model = model_dict[chat_id]
        model.model_fit = message.text

        msg = bot.send_message(chat_id, '*Namuna FIT:*\n\n',
                               parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, register_model_fit)
    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi kontaktda boshidan ro`yhatdan o\'ting /register 4')


# model BULK
def register_model_fit(message):
    chat_id = message.chat.id
    try:
        model = model_dict[chat_id]
        model.model_bulk = message.text

        msg = bot.send_message(chat_id, '*Namuna BULK:*\n\n',
                               parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, register_model_bulk)
    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi  boshidan ro`yhatdan o\'ting /register 5')


# model print
def register_model_bulk(message):
    chat_id = message.chat.id
    try:
        model = model_dict[chat_id]
        model.model_print = message.text

        msg = bot.send_message(chat_id, '*Namuna Print:*\n\n',
                               parse_mode='MarkdownV2')

        bot.register_next_step_handler(msg, register_model_print)
    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi  boshidan ro`yhatdan o\'ting /register 6')


# model PPS
def register_model_print(message):
    chat_id = message.chat.id
    try:
        model = model_dict[chat_id]
        model.model_pps = message.text

        msg = bot.send_message(chat_id, '*Namuna PPS:*\n\n',
                               parse_mode='MarkdownV2')

        bot.register_next_step_handler(msg, register_pps)
    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi  boshidan ro`yhatdan o\'ting /register 7')


# model harvested
def register_pps(message):
    chat_id = message.chat.id
    try:
        model = model_dict[chat_id]
        model.harvested = message.text

        msg = bot.send_message(chat_id, '*Bichilgan:*\n\n',
                               parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, register_harvested)
    except Exception as e:
        bot.reply_to(message, 'Xatolik yuz berdi  boshidan ro`yhatdan o\'ting /register 8')


# model printed
def register_harvested(message):
    chat_id = message.chat.id
    try:
        model = model_dict[chat_id]
        model.printed = message.text

        msg = bot.send_message(chat_id, '*Pechat bosilgan:*\n\n',
                               parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, register_printed)
    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi  boshidan ro`yhatdan o\'ting /register 9')


# model stichted
def register_printed(message):
    chat_id = message.chat.id
    try:
        model = model_dict[chat_id]
        model.stichted = message.text

        msg = bot.send_message(chat_id, '*Tikilgan:*\n\n',
                               parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, register_stichted)
    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi  boshidan ro`yhatdan o\'ting /register 11')


# model packaged
def register_stichted(message):
    chat_id = message.chat.id
    try:
        model = model_dict[chat_id]
        model.packaged = message.text
        msg = bot.send_message(chat_id, '*Qadoqlangan:*\n\n',
                               parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, register_packaged)
    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi  boshidan ro`yhatdan o\'ting /register 12')


# model total box
def register_packaged(message):
    chat_id = message.chat.id
    try:
        model = model_dict[chat_id]
        model.stichted = message.text
        msg = bot.send_message(chat_id, '*Jami korobka soni:*\n\n',
                               parse_mode='MarkdownV2')
        bot.register_next_step_handler(msg, register_total_box)
    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi  boshidan ro`yhatdan o\'ting /register 13')


# model total box
def register_total_box(message):
    chat_id = message.chat.id
    try:
        model = model_dict[chat_id]
        model.total_box = message.text

        msg = bot.send_message(chat_id, 'Model rasmini yuboring: ')
        bot.register_next_step_handler(msg, register_img)

    except Exception:
        bot.reply_to(message, 'Xatolik yuz berdi  boshidan ro`yhatdan o\'ting /register 14')


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

# model photo 
@bot.message_handler(func=lambda message: True, content_types=['photo'])
def register_img(message):
    chat_id = message.chat.id
    username = message.chat.username

    try:
        img = message.photo[-1].file_id
        model = model_dict[chat_id]
        model.img = img

        is_username = f'💬 Telegram: @{username}\n'
        none = ''
        bot.send_photo(chat_id, photo=img,
                       caption=f'Mijoz: <b>{model.customer}</b>\n'
                               f'Model: <b>{model.model_name}</b>\n'
                               f'FI Sanasi:{model.fi_date}\n'
                               f'Miqdori: {model.count}\n'
                               f'Namuna L/D: <b>{model.model_ld}</b>\n'
                               f'Namuna FIT:   <b>{model.model_fit}</b>\n'
                               f'Namuna BULK:   <b>{model.model_bulk}</b>\n'
                               f'Namuna Print: <b>{model.model_print}</b>\n'
                               f'Namuna PPS: <b>{model.model_pps}</b>\n'
                               f'Bichilgan <b>{model.harvested}</b>\n'
                               f'Pechat Bosilgan <b>{model.printed}</b>\n'
                               f'Tikilgan <b>{model.stichted}</b>\n'
                               f'Bichilgan <b>{model.packaged}</b>\n'
                               f'Jami korobka soni: <b>{model.total_box}</b>',
                       parse_mode='html')

        msg = bot.send_message(chat_id, f'👇 Xurmatli <b>{message.chat.first_name}</b> ma\'lumotlar to\'g\'ri '
                                        f'ekanligini tastiqlang! ',
                               reply_markup=all_ok_m, parse_mode='html')
        # send_to_admin
        bot.register_next_step_handler(msg, send_to_adminn)

        # bot.delete_message(chat_id, mes_id)
    except Exception as e:
        bot.reply_to(message, 'Xatolik yuz berdi rasmni yuklashda boshidan ro`yhatdan o\'ting /register 15')


@bot.message_handler(func=lambda message: True)
def send_to_adminn(message):
    call_id = message.chat.id
    q = message.text
    username = message.chat.username

    # try:
    is_username = f'💬 Telegram: @{username}\n'
    none = ''
    model = model_dict[call_id]
    if q == '❌ Yo\'q':
        mes = bot.send_message(call_id, 'Juda sos ma\'lumotlaringiz yuborilmadi.'
                                        'Qaytatdan ro\'yhatdan o\'tish uchun /register',
                               reply_markup=remove_keys)


    elif q == '✅ Ha':
        bot.send_photo(call_id, photo=model.img,
                       caption=f'Mijoz: <b>{model.customer}</b>\n'
                               f'Model: <b>{model.model_name}</b>\n'
                               f'FI Sanasi:<b>{model.fi_date}</b>\n'
                               f'Miqdori: <b>{model.count}</b>\n'
                               f'Namuna L/D: <b>{model.model_ld}</b>\n'
                               f'Namuna FIT:   <b>{model.model_fit}</b>\n'
                               f'Namuna BULK:   <b>{model.model_bulk}</b>\n'
                               f'Namuna Print: <b>{model.model_print}</b>\n'
                               f'Namuna PPS: <b>{model.model_pps}</b>\n'
                               f'Bichilgan <b>{model.harvested}</b>\n'
                               f'Pechat Bosilgan <b>{model.printed}</b>\n'
                               f'Tikilgan <b>{model.stichted}</b>\n'
                               f'Bichilgan <b>{model.packaged}</b>\n'
                               f'Jami korobka soni: {model.total_box}',
                       parse_mode='html')

        bot.send_message(call_id, f' ma\'lumotlar muvaffaqiyatli saqlandi ✅\n'
                                  f'Yangi model uchun /register',
                         reply_markup=remove_keys)

    # except Exception as e:
    #     bot.send_message(call_id, 'Xatolik yuz berdi agar ro`yhatdan o`tmagan bo`lsangiz qaytatdan urunib '
    #                               'ko`ring /register 15',
    #                      reply_markup=remove_keys)


bot.enable_save_next_step_handlers(delay=2)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

bot.polling(none_stop=True, interval=0, timeout=0)

# bot.infinity_polling()
