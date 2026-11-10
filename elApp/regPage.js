const regForm = document.getElementById("regForm")

if (!regForm) {
    console.error("Форма с id='regForm' не найдена на странице!");
}

regForm.addEventListener('submit', function(event) {

    event.preventDefault();

    const usernameEl = document.getElementById("username");
    const emailEl = document.getElementById("username");
    const passwordEl = document.getElementById("username");

    if (!usernameEl || !emailEl || !passwordEl) {
        alert("Ошибка в HTML: Не найдены поля ввода! Проверьте id='username', id='email' и id='password'");
        return;
    }

    const regDatas = {
        username: usernameEl.value,
        email: emailEl.value,
        password: passwordEl.value,
    }

    console.log("datas sending: ", regDatas);

    fetch('http://127.0.0.1:8000/api/PURRmission/reg/', {

        method: "POST",
        headers: {
            'Content-type': 'application/json',
        },
        body: JSON.stringify(regDatas)

    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(err => { throw err; });
        }
        return response.json()
    })
    .then(data => {
        console.log('REG PASS: ', data)
        regForm.innerHTML = `Validation is succed. Welcome to us, ${regDatas.username}!`
        alert("reg is succed!")
    })
    .catch(error => {
        console.error("ERROR: ", error);
        alert("ERROR: " + JSON.stringify(error));
    });
})
