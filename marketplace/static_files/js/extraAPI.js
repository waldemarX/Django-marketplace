$(document).ready(function() {
    // Like button
    $(document).on("click", ".item_like", function(e) {
        e.preventDefault();

        var item_id = $(this).data("item-id");
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
                console.log('Like added: ', data.message)
                $("#likes_counter").text(data.likes);
            } else {
                console.error('Request error: ', data.message);
            }
        })
        .catch(error => console.error('Request error:', error));
    });
});