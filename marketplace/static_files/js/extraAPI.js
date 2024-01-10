$(document).ready(function() {

    const item_id = $("#like1").data("item-id");
    const url = `/api/check_if_like/?item_id=${item_id}`;
    const like_btn = $("#like")
    

    // Like button
    $(document).on("click", ".item_like", function(e) {
        e.preventDefault();

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
                    console.log('Like added: ', data.message);
                    $("#likes_counter").text(data.likes);
                    like_btn.addClass("like_is_active");
                }
                else {
                    console.log('Like removed: ', data.message);
                    $("#likes_counter").text(data.likes);
                    like_btn.removeClass("like_is_active");
                }
                
            } else {
                console.error('Request error: ', data.message);
            }
        })
        .catch(error => console.error('Request error:', error));
    });

    fetch(url)
    .then(response => response.json())
    .then((data) => {
        if (data.is_like) {
            like_btn.addClass("like_is_active");
            console.log('Like is active ', data.message);
        }
    })
    .catch(error => console.error('Request error:', error));
});