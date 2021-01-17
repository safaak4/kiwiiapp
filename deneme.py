from instabot import bot
import os

bot = bot.Bot()
scriptDir = os.path.dirname(os.path.realpath(__file__))
bot.login(username = "username", password= "password")

bot.upload_photo(scriptDir + os.path.sep + "patternjpg.jpg", caption="deneme4")