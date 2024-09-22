const getCookie = name => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }

    return cookieValue;
};

let send_form = document.getElementById('vote');

send_form.addEventListener('submit', async (event) => {
    event.preventDefault();
    
    let selectedOptions = {};

    const radioInputs = document.querySelectorAll('#vote input[type="radio"]');

    radioInputs.forEach(input => {
        if (input.checked) {
            const name = input.name;
            selectedOptions[name] = input.value;
        }
    });

    console.log(selectedOptions);

    try {
        const response = await fetch('/post_order/', {
            method: 'POST',
            body: JSON.stringify({ result: selectedOptions }),
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/json',
            },
        });

        const data = await response.json();

        if (response.ok) {
            alert('Успешно добавлено в БД.');
        } else {
            alert(`Ошибка при отправке в БД: ${data.error}`);
        }
    } catch (error) {
        console.error('Ошибка при отправке запроса:', error);
        alert('Произошла ошибка. Пожалуйста, попробуйте еще раз.');
    }
});
