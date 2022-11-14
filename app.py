from flask import Flask, render_template, request, redirect
import smtplib

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():  # put application's code here
    string = None
    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        if name != None:
            print(name, email, subject, message)
            send_mail(name, email, subject, message)
            return "Your message has been sent. Thank you!😉"


        string = request.form.get('string')
        converted_text = string_to_morse_code(string)

        return render_template('result.html', text=converted_text, string=string)
    return render_template('index.html', string=string)



MORSE_CODE_DICT = {
    'A':'.- ', 'B':'-... ',
    'C':'-.-. ', 'D':'-.. ', 'E':'. ',
    'F':'..-. ', 'G':'--. ', 'H':'.... ',
    'I':'.. ', 'J':'.--- ', 'K':'-.- ',
    'L':'.-.. ', 'M':'-- ', 'N':'-. ',
    'O':'--- ', 'P':'.--. ', 'Q':'--.- ',
    'R':'.-. ', 'S':'... ', 'T':'- ',
    'U':'..- ', 'V':'...- ', 'W':'.-- ',
    'X':'-..- ', 'Y':'-.-- ', 'Z':'--.. ',
    '1':'.---- ', '2':'..--- ', '3':'...-- ',
    '4':'....- ', '5':'..... ', '6':'-.... ',
    '7':'--... ', '8':'---.. ', '9':'----. ',
    '0':'----- ', ',':'--..-- ', '.':'.-.-.- ',
    '?':'..--.. ', '/':'-..-. ', '-':'-....- ',
    '(':'-.--. ', ')':'-.--.- ', ' ':'....... ', ':':'---... ',
    '!':'-.-.-- ', ';':'-.-.-. ', '+':'.-.-. ', '=':'-...- ',
}

def string_to_morse_code(string):
    list_chars = [char for char in string]
    new_list = []
    for char in list_chars:
        new_char = MORSE_CODE_DICT[char.upper()]
        new_list.append(new_char)

    converted_text = "".join(new_list)
    return converted_text


MY_EMAIL = "anasajaanan.official@gmail.com"
MY_PASSWORD = "toljsfwhkdsxdlhn"

def send_mail(name, email, subject, message):
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="anasajaanan.official@gmail.com",
        msg=f"Subject:Contact from MorseCode\n\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}."
    )




if __name__ == '__main__':
    app.run(debug=True)

