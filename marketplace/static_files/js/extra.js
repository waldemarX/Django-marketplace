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

var doc = document.querySelector(".btn_copy")
if (doc) {
    addEventListener("click", function () {
        copyText(".profile_wallet");
    });
}

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

// for write-article.html
function previewImageArticle() {
    // Получаем элементы
    var fileInput = document.getElementById('id_image');
    var preview = document.getElementsByClassName("post-image")[0];
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
        image.classList.add('lazy');
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

document.addEventListener("DOMContentLoaded", function() {
        var dropdownButton = document.getElementById("collectionDropdownBtn");
        var dropdownOptions = document.querySelectorAll("#item_collection ul li");
        var selectedCategoryInput = document.getElementById("id_category");
    
        dropdownOptions.forEach(function(option) {
            option.addEventListener("click", function() {
                var selectedCategory = this.dataset.value;
                selectedCategoryInput.value = selectedCategory;
                dropdownButton.textContent = "Selected: " + selectedCategory;
            });
        });
    });

window.addEventListener('DOMContentLoaded', (event) => {
	const titleInput = document.getElementById('id_title');
	const titleDisplay = document.getElementById('title_display');
	const textInput = document.getElementById('id_text');
	const textDisplay = document.getElementById('text_display');
	const categoryDisplay = document.getElementById('category_display');
	const categoryInput = document.getElementById('id_category');
	const collectionDropdownBtn = document.getElementById('collectionDropdownBtn');

	const wordLimit = 5;

	titleInput.addEventListener('input', function() {
		titleDisplay.textContent = this.value;
	});

	textInput.addEventListener('input', function() {
		const originalText = this.value.trim();
		const words = originalText.split(' ');

		if (words.length > wordLimit) {
			const truncatedText = words.slice(0, wordLimit).join(' ') + '...';
			textDisplay.textContent = truncatedText;
		} else {
			textDisplay.textContent = originalText;
		}
	});

	document.getElementById('item_collection').addEventListener('click', function(e) {
		if (e.target.tagName === 'SPAN') {
			const selectedCategory = e.target.textContent;
			categoryDisplay.textContent = selectedCategory;
			categoryInput.value = selectedCategory;
		}
	});
});

// for edit-profile.html
function darkenImage1() {
    var overlays = document.querySelectorAll('.img-container1 .overlay-banner');
    overlays.forEach(function(overlay) {
        overlay.style.opacity = '1';
    });

}

function lightenImage1() {
    var overlays = document.querySelectorAll('.img-container1 .overlay-banner');
    overlays.forEach(function(overlay) {
        overlay.style.opacity = '0';
    });
}

function darkenImage() {
    var overlays = document.querySelectorAll('.img-container .overlay');
    overlays.forEach(function(overlay) {
        overlay.style.opacity = '1';
    });

}

function lightenImage() {
    var overlays = document.querySelectorAll('.img-container .overlay');
    overlays.forEach(function(overlay) {
        overlay.style.opacity = '0';
    });
}

