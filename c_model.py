import gspread
from oauth2client.service_account import ServiceAccountCredentials
import telebot

# Define the scope
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("template").sheet1

API_TOKEN = '7264152538:AAELpQRzr1KrGJbBaPZgodmWat5X0jTtiZc'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help' commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    name = message.chat.first_name
    bot.reply_to(message, f"Hello! I'm a Telegram bot. How can I help you {name} today?")
    print(f'bot starting')
    print(f'{name} joined to bot')

# Handle all other messages
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    chat_id = message.chat.id
    # Define the search term
    search_term = message.text

    # Initialize a list to hold search results with row numbers
    results_with_row = []

    # Get all values from the sheet
    all_values = sheet.get_all_values()

    # Iterate through each row to find the search term
    for row_number, row in enumerate(all_values, start=2):
        if search_term in row:
            results_with_row.append((row_number, row))

    # Print the results with row numbers and full row data
    for row_number, row_data in results_with_row:
        print(message.text)
        print(f"User id {chat_id}\n{message.chat.first_name}\nRow {row_number} contains the search term: {search_term}")
        # print(row_data)

        bot.send_photo(chat_id=chat_id,
                       photo=f'{row_data[21]}',
                       caption=  f'MIJOZ: <b>{row_data[1]}</b>\n'
                                 f'MODEL: <b>{row_data[2]}</b>\n'
                                 f'MODEL IMZOLANGAN SANA: <b>{row_data[3]}</b>\n'
                                 f'FI SANASI:<b>{row_data[4]}</b>\n'
                                 f'MIQDORI:<b>{row_data[5]}</b>\n'
                                 f'NAMUNA L/D:<b>{row_data[6]}</b>\n'
                                 f'NAMUNA FIT:<b>{row_data[7]}</b>\n'
                                 f'NAMUNA BULK:<b>{row_data[8]}</b>\n'
                                 f'NAMUNA Print:<b>{row_data[9]}</b>\n'
                                 f'NAMUNA PPS:<b>{row_data[10]}</b>\n'
                                 f'BICHIM SONI:<b>{row_data[11]}</b>\n'
                                 f'BICHIM STATUSI:<b>{row_data[12]}</b>\n'
                                 f'PECHAT SONI:<b>{row_data[13]}</b>\n'
                                 f'PECHAT STATUSI:<b>{row_data[14]}</b>\n'
                                 f'TIKIM SONI:<b>{row_data[15]}</b>\n'
                                 f'TIKIM STATUSI: <b>{row_data[16]}</b>\n'
                                 f'QADOQLANGAN: <b>{row_data[17]}</b>\n'
                                 f'YOPILGAN KAROBKA SONI: <b>{row_data[18]}</b>\n'
                                 f'YOPILISHI KERAK: <b>{row_data[19]}</b>\n'
                                 f'MA\'LUMOT YANGILANGAN SANA: <b>{row_data[20]}</b>\n',
                       parse_mode='html')


@bot.message_handler(func=lambda message: True, content_types=['photo'])
def send_photo_id(message):

    img = message.photo[-1].file_id
    bot.reply_to(message, f"{img}")


bot.polling(none_stop=True, interval=0, timeout=0)
