$(document).ready(function(){
	$(function(){
$("#addClass").click(function () {
  $('#sidebar_secondary').addClass('popup-box-on');
    });
  
    $("#removeClass").click(function () {
  $('#sidebar_secondary').removeClass('popup-box-on');
    leave_room()
    });
})

    

                var chat_namespace = '/chat'
                var socket_chat = io.connect(location.protocol + "//" + location.host + chat_namespace, {reconnect: false});

                socket_chat.on('connect', function() {
                    socket_chat.emit('manager_connect', {'userId': g.userId});
                });

                socket_chat.on('manager_status', function(data) {
                        $('#chat-box').append('<div class="chat_message_wrapper chat_message_right">' +
                        '<div class="chat_user_avatar">' +
                        '<a href="#" target="_blank" >' +
                        '<img class="md-user-image" style="border-radius: 999px" alt="" title="" src="https://kak2z.ru/galavatars/images/9/561.png">' +
                        '<!--img alt="" title=""  src="" class="md-user-image"-->' +
                        '</a>' +
                        '</div>' +
                        '<ul class="chat_message last" id="chat-wrapper">' +
                        '<li>' +
                        '<p>' + data.msg + '</p>' +
                        '<span class="chat_message_time">' + data.time + '</span>'+
                        '</li>' +
                        '</ul>' +
                        '</div>');
                    $('#chat').scrollTop($('#chat')[0].scrollHeight);
                });

                socket_chat.on('client_status', function(data) {
                        $('#chat-box').append('<div class="chat_message_wrapper">' +
                        '<div class="chat_user_avatar">' +
                        '<a href="#" target="_blank" >' +
                        '<img class="md-user-image" style="border-radius: 999px" alt="" title="" src="https://kak2z.ru/galavatars/images/9/561.png">' +
                        '<!--img alt="" title=""  src="" class="md-user-image"-->' +
                        '</a>' +
                        '</div>' +
                        '<ul class="chat_message last" id="chat-wrapper">' +
                        '<li>' +
                        '<p>' + data.msg + '</p>' +
                        '<span class="chat_message_time">' + data.time + '</span>'+
                        '</li>' +
                        '</ul>' +
                        '</div>');
                    $('#chat').scrollTop($('#chat')[0].scrollHeight);
                });

                socket_chat.on('manager_message', function(data) {
                        $('#chat-box').append('<div class="chat_message_wrapper chat_message_right">' +
                        '<div class="chat_user_avatar">' +
                        '<a href="#" target="_blank" >' +
                        '<img class="md-user-image" style="border-radius: 999px" alt="" title="" src="https://kak2z.ru/galavatars/images/9/561.png">' +
                        '<!--img alt="" title=""  src="" class="md-user-image"-->' +
                        '</a>' +
                        '</div>' +
                        '<ul class="chat_message last" id="chat-wrapper">' +
                        '<li>' +
                        '<p>' + data.msg + '</p>' +
                        '<span class="chat_message_time">' + data.time + '</span>'+
                        '</li>' +
                        '</ul>' +
                        '</div>');
                });

                socket_chat.on('client_message', function(data) {
                        $('#chat-box').append('<div class="chat_message_wrapper">' +
                        '<div class="chat_user_avatar">' +
                        '<a href="#" target="_blank" >' +
                        '<img class="md-user-image" style="border-radius: 999px" alt="" title="" src="https://kak2z.ru/galavatars/images/9/561.png">' +
                        '<!--img alt="" title=""  src="" class="md-user-image"-->' +
                        '</a>' +
                        '</div>' +
                        '<ul class="chat_message last" id="chat-wrapper">' +
                        '<li>' +
                        '<p>' + data.msg + '</p>' +
                        '<span class="chat_message_time">' + data.time + '</span>'+
                        '</li>' +
                        '</ul>' +
                        '</div>');
                });


               	$('#submit_message').keypress(function(e) {
                    var code = e.keyCode || e.which;
                    if (code == 13) {
                        text = $('#submit_message').val();
                        if (text.length === 0) {
                        	console.log('empty message!')
                        }
                        else {
                        	console.log('from client: ' + String(text))
                        	$('#submit_message').val('');
                        	socket_chat.emit('manager_text', {msg: text});
                        }
                    }
                });

            function leave_room() {
                socket_chat.emit('manager_left', {'msg': 'suck'}, function() {
                    socket_chat.disconnect();

                    // go back to the login page
                    //window.location.href = "{{ url_for('site.index') }}";
                });
            };

        $('.chat-icon').click(function(){
            $('#sidebar_secondary').addClass('popup-box-on');
            socket_chat.emit('manager_joined', {'msg': 'fuck'});
        });

        $('#removeClass').click(function(){
            $('#sidebar_secondary').removeClass('popup-box-on')
        });

})
