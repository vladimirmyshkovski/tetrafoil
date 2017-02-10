from flask import session, g, request
from ..models import User
import time
import eventlet
from flask_login import current_user
from ..utils.redis import redis_store
from flask_socketio import SocketIO, Namespace, emit, join_room, leave_room, \
close_room, rooms, disconnect, send
from geolite2 import geolite2

reader = geolite2.reader()
socketio = SocketIO()
eventlet.monkey_patch()


class Notifs(Namespace):
    def on_connect(message):
        user_room = 'user_{}'.format(current_user.id)
        join_room(user_room)
        #user = current_user
        emit('response', {'meta': 'WS connected', 'count': 0})
        #User.push_user_notification(user)
        socketio.sleep(1)


    def on_disconnect(message):
    	print('Client disconnected', request.sid)


class Chat(Namespace):

    def on_manager_connect(self, message):
        print(request.user_agent)
        print(request.accept_languages)
        print(request.remote_addr)
        print(reader.get("46.216.11.9"))
        global managers
        managers = {'id': message['userId'], 'name': User.query.get(message['userId']).email, 'sid': request.sid, 'room': message['userId']}
        print(managers)
        print(str(message['userId']) + ' законнекчен!')
        socketio.sleep(1)


    def on_manager_joined(self, message):
        print(message['msg'])
        #global managers
        #managers = {'id': message['userId'], 'name': User.query.get(message['userId']).email, 'sid': request.sid, 'room': message['userId']}
        print(managers['sid'])
        join_room(managers['room'])
        print(str(managers['id']) + ', Вы вошли в чат!')
        emit('manager_status', {
            'msg': managers['name'] + ', Вы вошли в чат!', 
            'time': time.strftime("%H:%M"), 
            'name': managers['name']}, 
            room=managers['room'])
        socketio.sleep(1)


    def on_manager_text(self, message):
        redis_store.publish('msg', message['msg'])
        emit('manager_message', {
            'msg':  message['msg'],
            'time': time.strftime("%H:%M"), 
            'name': managers['name']}, 
            room=clients['room'])


    def on_manager_left(self, message):
        print(message['msg'])
        leave_room(managers['room'])    
        emit('client_status', {
            'msg': managers['name'] + ' покинул чат!',
            'time': time.strftime("%H:%M"), 
            'name': managers['name']}, 
            room=managers['room'])
        print(managers['name'] + ' покинул чат!')









    def on_client_connect(self, message):
        global clients
        clients = {'sid': request.sid, 'room': managers['id']}
        print('Клиент законнекчен!')
        print(message['msg'])
        print(clients)
        print('room is :' + str(managers['room']))
        socketio.sleep(2)

    def on_client_joined(self, message):
        clients = {'name': message['name'], 'sid': request.sid, 'room': managers['id']}
        session['client_name'] = message['name']
        print(clients)
        print(clients['sid'])
        join_room(managers['room'])
        print(str(clients['name']) + ' присоеденился к чату!')
        emit('client_status', {
            'msg': clients['name'] + ' присоеденился к чату!', 
            'time': time.strftime("%H:%M"), 
            'name': clients['name']}, 
            room=managers['room'])
        emit('manager_status', {
            'msg': managers['name'] + ' присоеденился к чату!', 
            'time': time.strftime("%H:%M"), 
            'name': managers['name']}, 
            room=clients['sid'])
        socketio.sleep(2)

    def on_client_text(self, message):
        redis_store.publish('msg', message['msg'])
        emit('client_message', {
            'msg':  message['msg'],
            'time': time.strftime("%H:%M"), 
            'name': session.get('client_name')}, 
            room=managers['room'])


    def on_client_left(self, message):
        print(message['msg'])
        leave_room(managers['room'])    
        emit('client_status', {
            'msg': clients['name'] + ' покинул чат!',
            'time': time.strftime("%H:%M"), 
            'name': clients['name']}, 
            room=managers['room'])
        print(clients['name'] + ' покинул чат!')

'''
    def on_client_joined(message):
        client_name = message['name']
        room = managers['manager_room'][0]
        client_sid = request.sid 
        clients.append({
            'client_name': client_name,
            'client_room': room,
            'client_sid': request.sid
            })
        join_room(room)
        emit('client_status', {'msg': str(client_name) + ' has entered the room.', 'time': time.strftime("%H:%M"), 'name': client_name}, room=room)

    def on_client_text(message):
        print('123')
        msg = message['msg']
        redis_store.publish('msg', msg)
        name = clients['clients_name']
        name = managers['managers_room']
        emit('client_message', {'msg':  message['msg'], 'time': time.strftime("%H:%M"), 'name': name}, room=room)

@socketio.on('client_left', namespace='/chat')
def left(message):
    room = session.get('room', '')
    name = message['name']
    leave_room(room)    
    emit('status', {'msg': ' has left the room.', 'name': name}, room=room)

@socketio.on('client_joined', namespace='/chat')

@socketio.on('client_text', namespace='/chat')
def text(message):
    room = 1
    client = 5
    msg = message['msg']
    redis_store.publish('msg', msg)
    print('client says: ' + message['msg'] + ' to room : ' + str(room))
    emit('client_message', {'msg':  message['msg'], 'time': time.strftime("%H:%M"), 'name': client}, room=room)

@socketio.on('client_left', namespace='/chat')
def left(message):
    client = 5 
    room = current_user.id
    leave_room(room)    
    emit('client_status', {'msg': ' has left the room.', 'name': client}, room=room)
'''

socketio.on_namespace(Notifs('/notifs'))
socketio.on_namespace(Chat('/chat'))
