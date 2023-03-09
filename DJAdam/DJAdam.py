from pyrogram import Client, filters

bot = Client(
          "DJ Adam",
          api_id = 16519771,
          api_hash = "83754b17b54fe9d6a602e70c458afddb",
          bot_token = "6165241065:AAHPgX6HbVbu2fceDToVKFwAa9g1aFs_6Z4"
)

@bot.on_message(filters.command('start')) #Creating a command.
def command1(bot, message): #Creating a function.
       bot.send_message(message.chat.id, "Hello! Use /help for help on how to use me. Or use the menu button.") #Calling a method.

@bot.on_message(filters.command('help')) #Creating a command.
def command2(bot, message): #Creating a function.
       message.reply_text("Here is a list of commands that you can use-\n\n/start - You can start the bot. you have used this already!\n\n/help - List of commands will appear, you have this one also!\n\n/photo - You will get some photos provided by @No_me_no_no. If you want to add more photos, just dm them to my owner.\n\n/song1 - This will send a music file. If you want to listen.\n\n/song2 - This is send another music file.\n\n/video1 - Plays a video\n\n/video2 - Play another video\n\nYou can also add me to your groups as a welcome bot!\n\nOwner will keep me updating and make sure I don't die.") #Calling a method.
     
#echobot  
#@bot.on_message(filters.text)
#def echobot(Client, message):
#     message.reply_text(message.text)
     
#welcomebot

GROUP = "pyrotestcall"
WELCOME_MESSAGE = "Helow {username}! Welcome to {chatname}!"

@bot.on_message(filters.chat(GROUP) & filters.new_chat_members)

def welcomebot(client, message):
     message.reply_text(WELCOME_MESSAGE)
     
#Send_photo
@bot.on_message(filters.command('photo'))
def command3(Client, message):
     bot.send_photo(message.chat.id, "https://imgur.com/t/anime_wallpaper/QLRTXVL")
     bot.send_photo(message.chat.id, "https://imgur.com/t/anime_wallpaper/toaUzHM")
     
#Send_audio
@bot.on_message(filters.audio & filters.private)
def audio(Client, message):
     message.reply(message.audio.file_id)
     
@bot.on_message(filters.command('song1'))
def command4(Client, message):
     bot.send_audio(message.chat.id, "CQACAgUAAxkBAAM6ZAiBNPg_eVIyEkk8NWgQj2ow8fEAAjoNAAJUREFU7ZfM4gUCXLseBA")
@bot.on_message(filters.command('song2'))
def command5(Client, message):
     bot.send_audio(message.chat.id, "CQACAgUAAxkBAANAZAiEdGIzz0sYpdtOh2NolO3aUF4AAkMNAAJUREFUJJiq4seYjZ4eBA")
     
#Send_video
@bot.on_message(filters.video & filters.private)
def video(Client, message):
     message.reply(message.video.file_id)
     
@bot.on_message(filters.command('video1'))
def command6(Client, message):
     bot.send_video(message.chat.id, "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4")
@bot.on_message(filters.command('video2'))
def command7(Client, message):
     bot.send_video(message.chat.id, "BAACAgUAAxkBAAOCZAjQyLHo1m5TDlc2Tqd2jfexewwAAqcNAAJUREFUin8dAVuoX8UeBA")

@bot.on_message(filters.text)
def delete_text(bot, message):
     bot.delete_messages(message.chat.id, message_id)

print("I AM ALIVE")
bot.run()
