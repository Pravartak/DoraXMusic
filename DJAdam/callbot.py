from DJAdam import config
from pyrogram import Client
from pytgcalls import PyTgCalls
from pytgcalls import idle
from pytgcalls.types import AudioPiped
...
client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
app = PyTgCalls(client)

app.start()
app.join_group_call(
        -1001796731397,
        AudioPiped(
            'http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4',
        )
    )
idle()
