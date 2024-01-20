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

    // Check events
    var eventsAPI = '/api/events/is_watched/'
    fetch(eventsAPI, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        },
    })
    .then(response => response.json())
    .then(data => {
        data.forEach(event => {
            // Проверяем, что уведомление не просмотрено
            if (!event.watch_status && event.user_receiver.id != event.user.id ) {
                // Создаем HTML-элемент с использованием данных из объекта event
                var htmlString = `
                <li>
                    <a href="">
                        <img class="lazy" src="" alt="">
                        <div class="d-desc">
                            <span class="d-name"><b>${event.user_receiver.username}</b> ${event.event} your image</span>
                            <span class="d-time">${formatRelativeTime(event.event_date)}</span>
                        </div>
                    </a>  
                </li>`;  // Замените field1, field2 и т.д. на ваши реальные поля
    
                // Добавляем созданный HTML-элемент куда-то на вашу страницу
                var container = document.getElementById('eventContainer');  // Замените yourContainerId на ID вашего контейнера
                container.innerHTML += htmlString;
            }
        });
    })
    .catch(error => console.error('Error:', error));

    function formatRelativeTime(dateTimeString) {
        const date = new Date(dateTimeString);
        const now = new Date();
    
        const diffInSeconds = Math.floor((now - date) / 1000);
    
        const intervals = [
            { label: 'year', seconds: 31536000 },
            { label: 'month', seconds: 2592000 },
            { label: 'day', seconds: 86400 },
            { label: 'hour', seconds: 3600 },
            { label: 'minute', seconds: 60 },
            { label: 'second', seconds: 1 }
        ];
    
        for (const interval of intervals) {
            const count = Math.floor(diffInSeconds / interval.seconds);
    
            if (count >= 1) {
                return `${count} ${interval.label}${count > 1 ? 's' : ''} ago`;
            }
        }
    
        return 'Just now';
    }
});