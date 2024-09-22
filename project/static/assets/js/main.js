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

    const formData = new FormData(event.target);
    const selectedOption = formData.get('option');

    try {
        const response = await fetch('/post_order/', {
            method: 'POST',
            body: JSON.stringify({ option: selectedOption }),
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/json',
            },
        });

        response.ok ?
            alert(`Успешно добавлено в БД.`):
            alert('Ошибка при отправки в БД.');
    } catch (error) {
        console.error('Ошибка при отправке запроса:', error);
        alert('Произошла ошибка. Пожалуйста, попробуйте еще раз.');
    }
});