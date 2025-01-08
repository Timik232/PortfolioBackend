let submit =  document.querySelector('.sendMessage');
let turnoff = document.getElementById("turnoff");
let box = document.querySelector(".box");
let isTurn = false;

submit.addEventListener('submit', function(e) {
  e.preventDefault();
  let form = document.querySelector('.sendMessage');
  let vkUrlValue = document.getElementById('vk').value;
    let isVkAnswerChecked = document.getElementById('is_vk_answer').checked;
    if ((!vkUrlValue && isVkAnswerChecked) || (vkUrlValue && !vkUrlValue.includes("vk"))) {
        alert('Пожалуйста, заполните поле с корректной ссылкой на VK, чтобы отметить "Отвечать в VK".');
    } else {
        fetch(form.action, {
            method: 'POST',
            body: new FormData(form),
        }).then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
            .then(data => {
                alert('Сообщение успешно отправлено');
                location.reload();
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
            });
        alert("Ваше сообщение успешно отправлено!")
        location.reload();
    }
});

turnoff.addEventListener("click", () => {
  if (!isTurn){
    box.style.visibility = "hidden";
    isTurn = true;
    turnoff.textContent = "Включить эффекты"
  }
  else {
    box.style.visibility = "visible";
    turnoff.textContent = "Выключить эффекты"
    isTurn = false;
  }
});
