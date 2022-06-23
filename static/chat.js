$(document).on("submit", "#form", function(e){
                            e.preventDefault();
                     $.ajax({
                        type: "POST",
                        url: "/store",
                     data: {
                        username: $("#username").val(),
                        speak: $("#speak").val(),
                        chatting: $("#chatting").val(),
                        image: $("#image").val(),
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                     },
                     success: function(data){

                     }
                     });
                 document.getElementById("chatting").value = ""
            });