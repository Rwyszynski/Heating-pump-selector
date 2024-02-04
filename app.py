from flask import Flask, render_template, url_for, request, redirect, g
import sqlite3

app_info = {
    'db_file': 'C:/Users/Robo/Desktop/Heating pump selector/dane/pompa.db'}

app = Flask(__name__)


def get_db():

    if not hasattr(g, 'sqlite_db'):
        conn = sqlite3.connect(app_info['db_file'])
        conn.row_factory = sqlite3.Row
        g.sqlite_db = conn
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):

    if hasattr(g, 'sqlite3_db'):
        g.sqlite_db.close()


class Rodzajpompy:

    def __init__(self, marka, moc, typ, cena, zro):
        self.marka = marka
        self.moc = moc
        self.typ = typ
        self.cena = cena
        self.zro = zro

    def __repr__(self):
        return f'Wybrałeś pompę marki {self.marka} typ {self.typ} mocy {self.typ}'


class Informacje:
    def __init__(self):
        self.pompy = []

    def zaladuj(self):
        self.pompy.append(Rodzajpompy(
            'Rotenso', 'Airimi', 2.5, 17000, 'powietrze'))
        self.pompy.append(Rodzajpompy(
            'DeDietrich', 'Elensio', 2.5, 11700, 'powietrze'))
        self.pompy.append(Rodzajpompy(
            'Buderus', 'WSW19600', 12, 58000, 'woda'))

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

        moc = 2.0
        if 'moc' in request.form:
            moc = request.form['moc']

        moc_pompy = (int(typ_domu) * int(metry_ogrzewane) +
                     int(ilosc_osob)*300)/1000

        if moc_pompy > 12:
            czy_woda = "woda"
        else:
            czy_woda = "powietrze"

        db = get_db()
        sql_command = 'select marka, typ, moc, cena, zro from pompowanie;'
        cur = db.execute(sql_command)
        transactions = cur.fetchall()

        return render_template('doborpompy_wynik.html', metry=metry, moc_pompy=moc_pompy, moc=moc, czy_woda=czy_woda, zrodlo=zrodlo, transactions=transactions)
