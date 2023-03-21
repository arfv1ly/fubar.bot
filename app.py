#bot_template?

import rocketchat_API

from rocketchat_API.rocketchat import RocketChat


bot = RocketChat('login', 'password', server_url='workspace_url')
bot.chat_send_message({ 'rid': 'channel_id', 'msg': 'Hello World!' })

def greet(msg, user, channel_id):
    bot.send_message('hello @' + user, channel_id)

bot.add_auto_answer(['good news', 'i have good news', ], ['hell yeah!', 'tell me, tell me!', 'you are already good news ;)', ])
