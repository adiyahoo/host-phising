"""
    Author: adiyahoo
    yo@know
    Version: 23.16
"""

import random
import threading
import discord
import asyncio

from flask import Flask, request, make_response
from flask_restful import Resource, Api
from discord.ext import commands
from collections import defaultdict

# CONFIG WEBSITE
host = "0.0.0.0" # taruh ip public kamu / 0.0.0.0 
"""
Silakan tentukan port yang diinginkan untuk pengaturan website. 
Disarankan menggunakan port 5000 untuk menghindari konflik potensial. 
"""
port = 80 

# Token kamu 
token_discord_bot = ""
token_website = "" 

# Channel id discord kamu
channel_id_kirim_data_ori = 1119851938767442020 # untuk bot discord ngirim data ke channel
channel_log = 1120302555382169660 # ini channel untuk mengirim log / spam 
pesan_log = True # buat true jika mau aktif pesan log nya

# App
app = Flask(__name__)
app.env = 'production'
api = Api(app)
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# IP counter
ip_counter = defaultdict(int)
ip_lock = defaultdict(threading.Lock)

# Activities discord bot 
"""
    Ubah sesuka kelian yah :)
"""
activities = [
    discord.Game(name="AdiYahoo Ganteng"),
    discord.Game(name="Script For You"),
    discord.Game(name="Make Me Happy")
]

async def change_activity():
    while True:
        await bot.change_presence(activity=random.choice(activities))
        await asyncio.sleep(60)

@bot.event
async def on_ready():
    await bot.loop.create_task(change_activity())

class pesan_discord(): 
    async def masalah_1(channel_log_obj, ip):
        await channel_log_obj.send(f"buset ada yang coba ngehack website nya nih, btw ni ip nya: ```{ip}```")

    async def masalah_2(channel_log_obj, error): 
        await channel_log_obj.send(f"Terjadi kesalahan dengan kode, informasi error: ```{error}```")
    
    async def masalah_3(channel_log_obj, ip): 
        await channel_log_obj.send(f"Bang token nya jangan lupa sayang, oh ya ini ip yang coba: ```{ip}```")

    async def send_embed(channel, data):
        guild = channel.guild
        owner = guild.owner
        embed = discord.Embed(title="Informasi Akun RDP", color=discord.Color.blue())
        embed.add_field(name="💻 OS", value=data['os'], inline=False)
        embed.add_field(name="🌐 IP", value=data['ip'], inline=False)
        embed.add_field(name="👤 Username", value=data['username'], inline=False)
        embed.add_field(name="🔒 Password", value=data['password'], inline=False)
        embed.set_author(name="adiyahoo", url="https://www.instagram.com/adiy.aksaaa/", icon_url="https://cdn.discordapp.com/attachments/1115550786055839846/1119872884593143869/WhatsApp_Image_2023-06-18_at_13.14.16.jpeg")
        embed.set_footer(text="Stay curious and keep exploring. Happy hacking!")
        await channel.send(f"Info akun rdp sayang, {owner.mention}", embed=embed)


class bot_discord(): 
    # untuk mengirim pesan ke discord 
    @staticmethod
    def bot_kirim_pesan(data): 
        channel = bot.get_channel(channel_id_kirim_data_ori)
        if channel is not None:
            asyncio.run_coroutine_threadsafe(pesan_discord.send_embed(channel, data), bot.loop)
            return True
        else:
            print(f"Channel dengan ID {channel_id_kirim_data_ori} tidak ditemukan.")
            return f"Channel dengan ID {channel_id_kirim_data_ori} tidak ditemukan.", 404

        
    # mengirim pesan log
    @staticmethod
    def bot_kirim_log(ip, error, masalah): 
        channel_log_obj = bot.get_channel(channel_log)
        if channel_log_obj is not None: 
            if pesan_log:
                match masalah: 
                    case 1: 
                        asyncio.run_coroutine_threadsafe(pesan_discord.masalah_1(channel_log_obj, ip), bot.loop)
                    case 2: 
                        asyncio.run_coroutine_threadsafe(pesan_discord.masalah_2(channel_log_obj, error), bot.loop)
                    case 3:
                        asyncio.run_coroutine_threadsafe(pesan_discord.masalah_3(channel_log_obj, ip), bot.loop)
            else: 
                pass
        else: 
            print(f"Channel dengan ID {channel_log_obj} tidak ditemukan.")
            return f"Channel dengan ID {channel_log_obj} tidak ditemukan.", 404
               
# def check_folder(nama_folder):
#     if not os.path.exists(nama_folder):
#         os.mkdir(nama_folder)
#     else:
#         pass

class author(Resource):
    def get(self):
        html = '''
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
                    <p class="mb-4">Script code ini disediakan secara gratis dan tidak dijual.</p>
                    <p class="mb-4">"Rankings don't define your true potential. Your ability to code and your passion for it speak volumes about your talent and determination. Embrace your coding skills, continue to learn and improve, and you'll unlock a world of opportunities beyond what any ranking can measure."</p>
                    <div class="flex items-center justify-center mb-4">
                        <i class="fab fa-github text-gray-500 mr-2"></i>
                        <a href="https://github.com/AdiYahoo" class="text-gray-500">Link GitHub</a>
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
            '''
        response = make_response(html)
        response.headers['Content-Type'] = 'text/html'

        return response

class get_data(Resource): 
    def post(self):
        ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        try:
            data = request.get_json()
            if data['token'] == token_website: 
                with ip_lock[ip]: 
                    ip_counter[ip] += 1
                    if ip_counter[ip] <= 2:
                        check_pesan = bot_discord.bot_kirim_pesan(data) 
                        if check_pesan: 
                            return 'Berhasil', 200
                    else:
                        return 'Limit tercapai mau ngespam?', 403
            else:
                bot_discord.bot_kirim_log(ip, None, 1)   
                return 'Token anda salah', 401
        except KeyError as e: 
            bot_discord.bot_kirim_log(ip, None, 3)
            return f'Terjadi kesalahan, pesan: {e}', 500
        except Exception as e:
            bot_discord.bot_kirim_log(None, e, 2)
            return f'Terjadi kesalahan, pesan: {e}', 500

# menambahkan api 
api.add_resource(author, '/')
api.add_resource(get_data, '/post_data')

class run_app():    
    @staticmethod
    def run_flask(): 
        app.run(host=host, port=port, debug=False)

    @staticmethod
    def run_bot_discord():
        bot.run(token_discord_bot)

if __name__ == "__main__": 
    flask_thread = threading.Thread(target=run_app.run_flask)
    bot_thread = threading.Thread(target=run_app.run_bot_discord)

    flask_thread.start()
    bot_thread.start()

    flask_thread.join()
    bot_thread.join()
