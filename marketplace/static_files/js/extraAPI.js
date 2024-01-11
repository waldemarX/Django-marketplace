$(document).ready(function() {
    // Like button
    $(document).on("click", ".item_like", function(e) {
        e.preventDefault();

        var item_id = $("#like1").data("item-id");
        var like_btn = $("#like")

        var likesURL = $(this).attr("href");
        var csrf_token = $("[name=csrfmiddlewaretoken]").val()

        fetch(likesURL, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrf_token,  // Добавление CSRF-токена
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            credentials: 'same-origin',  // Включение отправки куки для CSRF-токена
            body: JSON.stringify({
                item_id: item_id,
            }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                if (data.event === 'like') {
                    console.log('Like added');
                    $("#likes_counter").text(data.likes);
                    like_btn.addClass("like_is_active");
                }
                else {
                    console.log('Like removed');
                    $("#likes_counter").text(data.likes);
                    like_btn.removeClass("like_is_active");
                }
                
            } else {
                console.error('Request error: ', data.message);
            }
        })
        .catch(error => console.error('Request error:', error));
    });

});