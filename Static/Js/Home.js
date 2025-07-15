let csrf = document.getElementsByName('csrfmiddlewaretoken');
let email_subject = document.getElementById('email_subject');
let email_message = document.getElementById('email_message');
let send_email_button = document.getElementById('send_email_button');

function send_email(subject,message){
    let formData = new FormData();
    formData.append('csrfmiddlewaretoken', csrf[0].value);
    formData.append('subject',subject);
    formData.append('message',message);
    $.ajax({
        type:'POST',
        url:'/sendEmail/',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response){
           console.log(response)
        },
        error: function(error){
            console.log(error)
        }
    });    
}

send_email_button.addEventListener('click', ()=> {
    send_email(email_subject.value,email_message.value);
});