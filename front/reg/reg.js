function check_form(el){
    var name = el.name.value
    var pass = el.pass.value
    var repass = el.repass.value

    var answer = "Вы успешно зарегистрировались"
    document.getElementById("answer").style.color = "red"

    if (name=="" || pass=="" || repass == "")
        answer = "заполните все поля"

    else if (name.length < 3)
        answer = "Длинна имени должно быть не менее 3"

    else if (pass.length < 3)
        answer = "Длинна пороля должно быть не менее 3"

    else if (pass != repass)
        answer = "Пороли должны совпадать"
    
    else
        document.getElementById("answer").style.color = "green"

    document.getElementById("answer").innerHTML = answer

    return false
}