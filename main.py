#drill 2
from pyscript import display, document


def results(e):
    document.getElementById("output").innerHTML = ''
    members = ['Bjorn Amargo', 'Bash Gervacio', 'Enzo Villegas', 'Vito De Guzman']
    fn = document.getElementById("fname").value.lower().strip()
    ln = document.getElementById("lname").value.lower().strip()
    full_name = fn + ' ' + ln
    name_checker = full_name in members
    display_message = (
        f'Sorry {full_name}, your name isnt on the list',
        f'Congrats {full_name}! You are now part of the Team.'
    )
    display(display_message[name_checker], target='output')
