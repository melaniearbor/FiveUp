var popupWindow=null;

function popup()
{
    popupWindow = window.open('message_add_success.html','name','width=200,height=200');
}

function add_message_disable() {
if(popupWindow && !popupWindow.closed)
popupWindow.focus();
}