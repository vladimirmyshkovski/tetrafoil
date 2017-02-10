from flask_redis import FlaskRedis
from ..utils.eventlet import eventlet
from flask_socketio import emit
import time

redis_store = FlaskRedis()

def redisReader():
	pubsub = redis_store.pubsub()
	pubsub.subscribe('msg')
	print ('Starting Redis subscriber')
	for msg in pubsub.listen():
	#print ('>>>>>', msg)
		print('Redis says : ' + str(msg['data']))
		#emit('message', {'msg':  msg['msg'], 'time': time.strftime("%H:%M"), 'name': manager}, room=room, namespace='/chat')
		print('emmited!')



def setupRedis():
	pool = eventlet.GreenPool()
	pool.spawn(redisReader)
	print('setupRedis')
