import config
import datetime
import logging

from time import time

# Configure logging
if config.debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

self = int(config.token.split(':')[0])

async def start(message):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
    event = message.get_command().lstrip('/')
    mid = message.message_id
    uid = message.from_user.id
    log = f'[{now} {event}] INFO: Self: {self}, Message {mid} from {uid}'
    cid = message.chat.id
    if cid != uid:
        log += f'@[Chat:{cid}]'
    caption = message.text
    log += f": '{caption}'"
    print(log)
    return time()

async def end(message, since):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S,%f')[:-3]
    event = message.get_command().lstrip('/')
    mid = message.message_id
    #output_elapsed = round((time.time()-since), 2)
    print(f'[{now} {event}] INFO: Message {mid} is handled as a command.')