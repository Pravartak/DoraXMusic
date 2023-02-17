import pyrogram
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls import idle
from pytgcalls.types import AudioPiped
api_id = 16519771
api_hash ="83754b17b54fe9d6a602e70c458afddb"
chat_id = -1001600386203
async def main():
async with Client("my_account", api_id, api_hash) as bot:
app = PyTgCalls(bot)
app.start()
app.join_group_call(
   chat_id,
   AudioPiped(
       'http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4',
   )
)
idle()
