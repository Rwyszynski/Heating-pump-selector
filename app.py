from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


class Rodzajpompy:

    def __init__(self, marka, moc, typ, cena):
        self.marka = marka
        self.moc = moc
        self.typ = typ
        self.cena = cena

    def __repr__(self):
        return f'Wybrałeś pompę marki {self.marka} typ {self.typ} mocy {self.typ}'


class Informacje:
    def __init__(self):
        self.pompy = []

    def zaladuj(self):
        self.pompy.append(Rodzajpompy('Rotenso', '3kW', 'Airimi', 17000))
        self.pompy.append(Rodzajpompy('DeDietrich', 'Elensio', 2.5, 11700))
        self.pompy.append(Rodzajpompy('Buderus', 'WSW19600', 12, 58000)

    def kod(self, kody):
        for pompa in self.pompy:
            if pompa.kody == kody:
                return pompa
        return Rodzajpompy('nieznany', 'nieznany', 'nieznany', 'nienznany')


@app.route('/')
def index():

    return 'This is index'


@app.route('/kontakt')
def kontakt():
    return "<h1>Z tych marek korzystamy</h1>"


@app.route('/doborpompy', methods=['GET', 'POST'])
def doborpompy():

    if request.method == 'GET':
        return render_template('doborpompy.html')
    else:
        metry = 200
        if 'metry' in request.form:
            metry = request.form['metry']

        return render_template('doborpompy_wynik.html', metry=metry)
