// for articles.html
$(document).ready(function() {
    // Handling the click event on a button link
    $("#btn-submit").click(function(e) {
        e.preventDefault();  // Preventing default link behavior
        $("#form_quick_search").submit();  // Call submit() on the form
    });
});

// for author.html
function copyText(element) {
    var copyText = document.querySelector(element);
    var button = document.querySelector(".btn_copy");

    navigator.clipboard.writeText(copyText.textContent).then(function () {
        var originalText = button.textContent;
        button.textContent = 'Copied!';
        button.classList.add('clicked');

        setTimeout(function () {
            button.textContent = originalText;
            button.classList.remove('clicked');
        }, 750);
    }).catch(function () {
        button.textContent = 'Error';
    });
}

document.querySelector(".btn_copy").addEventListener("click", function () {
    copyText(".profile_wallet");
});

// for create-single.html
function previewImage() {
    // Получаем элементы
    var fileInput = document.getElementById('id_image');
    var preview = document.getElementsByClassName("nft__item_wrap")[0];
    var fileNameParagraph = document.getElementById('file_name');

    fileNameParagraph.textContent = "Selected file: " + fileInput.files[0].name;

    // Очищаем превью перед каждым новым выбором файла
    preview.innerHTML = '';

    // Проверяем, выбран ли файл
    if (fileInput.files && fileInput.files[0]) {
      var reader = new FileReader();

      // Событие загрузки изображения
      reader.onload = function(e) {
        // Создаем элемент изображения и добавляем его в превью
        var image = document.createElement('img');
        image.src = e.target.result;
        image.classList.add('lazy', 'nft__item_preview');
        preview.appendChild(image);
      };

      // Чтение данных из файла как Data URL
      reader.readAsDataURL(fileInput.files[0]);
    }
  }
  function triggerFileInput() {
      // Получаем элемент <input type="file">
      var fileInput = document.getElementById('id_image');

      // Вызываем событие click для элемента <input type="file">
      fileInput.click();
    }