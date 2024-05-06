function check_form(el){
    var login = el.login.value
    var name = el.name.value
    var surname = el.surname.value
    var pass = el.pass.value
    var repass = el.repass.value

    var answer = "Вы успешно зарегистрировались"
    document.getElementById("answer").style.color = "red"

    if (login == "" || name=="" || surname == "" || pass=="" || repass == "")
        answer = "заполните все поля"

    else if (pass.length < 3)
        answer = "Длинна пороля должно быть не менее 3"

    else if (pass != repass)
        answer = "Пороли должны совпадать"
    
    else
        document.getElementById("answer").style.color = "green"

    document.getElementById("answer").innerHTML = answer

    return false
}
