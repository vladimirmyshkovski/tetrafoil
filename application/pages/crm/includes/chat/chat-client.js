$(document).ready(function(){
	$(function(){
  $('#sidebar_secondary').addClass('popup-box-on');
  $('.leed-input-name').removeClass('hide')
  
    $("#removeClass").click(function () {
  $('#sidebar_secondary').removeClass('popup-box-on');
      leave_room()
    });
})

                var client_chat_namespace = '/chat'
                var socket_chat_client = io.connect(location.protocol + "//" + location.host + client_chat_namespace, {reconnect: false});

                socket_chat_client.on('connect', function() {
                    socket_chat_client.emit('client_connect', {'msg':'msg'});
                });

                socket_chat_client.on('manager_status', function(data) {
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
                socket_chat_client.on('client_message', function(data) {
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

                socket_chat_client.on('manager_message', function(data) {
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
                        	socket_chat_client.emit('client_text', {'msg': text});
                        }
                    }
                });

                $('#leed-input-name').keypress(function(e) {
                    var code = e.keyCode || e.which;
                    if (code == 13) {
                        leed_name = $('#leed-input-name').val();
                        if (leed_name.length === 0) {
                            console.log('Name length must be > 0!')
                        }
                        else {
                            console.log('Leed_name is: ' + String(leed_name))
                            $('#leed-input-name').val('');
                            $('.leed-input-name').addClass('hide')
                            //socket_chat_client.emit('text', {'msg': leed_name});
                            socket_chat_client.emit('client_joined', {'name': leed_name});
                            alert(leed_name)
                        }
                    }
                });

            function leave_room() {
                socket_chat_client.emit('client_left', {}, function() {
                    socket_chat_client.disconnect();

                    // go back to the login page
                    window.location.href = "{{ url_for('site.index') }}";
                });
            };

        $('.chat-icon').click(function(){
            $('#sidebar_secondary').toggleClass('popup-box-on');
        });
        $('#removeClass').click(function(){
            $('#sidebar_secondary').removeClass('popup-box-on')
        });

})
