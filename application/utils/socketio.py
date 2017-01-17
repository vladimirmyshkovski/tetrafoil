from flask import session, g, request
from flask_socketio import SocketIO, Namespace, emit, join_room, leave_room, \
close_room, rooms, disconnect
socketio = SocketIO()
from ..models import User

@socketio.on('connect', namespace='/notifs')
def handle_connection():
    if session['user_id']:
        user_room = 'user_{}'.format(session['user_id'])
        join_room(user_room)
        user = User.query.get(session['user_id'])
        emit('response', {'meta': 'WS connected', 'count': 0})
        User.push_user_notification(user)


def push_notification_to_all_users(title, message):
    socketio.emit('notification',
         {'title': title,
         'message': message},
         namespace='/notifs')

@socketio.on('disconnect', namespace='/notifs')
def handle_disconnection():
	print('Client disconnected', request.sid)




"""
@socketio.on('connect', namespace='/notifs')
def connect_handler():
    if get_current_user():
        user_room = 'user_{}'.format(session['user_id'])
        join_room(user_room)
        print(user_room)
        emit('response', {'meta': 'WS connected'})


@socketio.on('my event', namespace='/notifs')
def handle_my_custom_event():
	print('hanlde')
	emit('my response',{'message': '{0} has joined'.format(get_current_user.name)},broadcast=True)


def create_user_notification(user, action, title, message):
    notification = Notification(user=user,
                                action=action,
                                title=title,
                                message=message,
                                received_at=datetime.now())
    saved = save_to_db(notification, 'User notification saved')

    if saved:
        push_user_notification(user)

def push_user_notification(user):
    user_room = 'user_{}'.format(user.id)
    print('user room is ' + str(user_room))
    socketio.emit('response',
         {'meta': 'New notifications',
          'notifs': user.get_unread_notifs()},
         room=user_room,
         namespace='/notifs')
"""





