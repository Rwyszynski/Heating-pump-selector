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
        self.pompy.append(Rodzajpompy('Buderus', 'WSW19600', 12, 58000))

    def kod(self, kody):
        for pompa in self.pompy:
            if pompa.kody == kody:
                return pompa
        return Rodzajpompy('nieznany', 'nieznany', 'nieznany', 'nienznany')


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/kontakt')
def kontakt():

    return render_template('kontakt.html')


@app.route('/doborpompy', methods=['GET', 'POST'])
def doborpompy():

    if request.method == 'GET':
        return render_template('doborpompy.html')
    else:
        if 'metry' in request.form:
            metry = request.form['metry']

        metry_ogrzewane = 200
        if 'metry_ogrzewane' in request.form:
            metry_ogrzewane = request.form['metry_ogrzewane']

        ilosc_osob = 2
        if 'ilosc_osob' in request.form:
            ilosc_osob = request.form['ilosc_osob']

        typ_domu = 'niezaizolowany'
        if 'typ_domu' in request.form:
            typ_domu = request.form['typ_domu']
            if typ_domu == 'niezaizolowany':
                typ_domu = 170
            elif typ_domu == 'pasywny':
                typ_domu = 20
            elif typ_domu == 'energooszczędny':
                typ_domu = 50
            else:
                typ_domu = 70

        budget = 'budget'
        if 'budget' in request.form:
            budget = request.form['budget']

        if 'zrodlo' in request.form:
            zrodlo = request.form['zrodlo']

        powietrze_woda = 'powietrze'
        if 'powietrze_woda' in request.form:
            powietrze_woda = request.form['powietrze_woda']

        moc_pompy = (int(typ_domu) * int(metry_ogrzewane) +
                     int(ilosc_osob)*300)/1000

        if moc_pompy > 12:
            czy_woda = "woda"
        else:
            czy_woda = "powietrze"

        return render_template('doborpompy_wynik.html', metry=metry, moc_pompy=moc_pompy, czy_woda=czy_woda, zrodlo=zrodlo)
