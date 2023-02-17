from pytgcalls import PyTgCalls
from pytgcalls import idle
from pytgcalls.types import AudioPiped
...
chat_id = -1001600386203
app = PyTgCalls(PyrogramClient)
app.start()
app.join_group_call(
   chat_id,
   AudioPiped(
       'http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4',
   )
)
idle()
