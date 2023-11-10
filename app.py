import math

from flask import Flask, render_template
from random import random

# Flask App initialisieren und TodoDao-Objekt erstellen
app = Flask(__name__)

"""
ideas: code snippets repo, 
"""


@app.route("/")
def add_todo():
    return "Endpoints: " + render_template("index.html")


@app.route("/A1G")
def A1G():
    """
    Ich kann die Eigenschaften von Funktionen beschreiben (z.Bsp. pure function) und den Unterschied zu anderen
    Programmierstrukturen erläutern (z.Bsp. zu Prozedur).
    """

    def pure_function(value):
        return str(value)

    def impure_function(value):
        return str(random() * 16 * value)

    return f"input = 5<br>pure function (no  side effects): {pure_function(5)}<br>impure function (side effects possible): {impure_function(5)}"


@app.route("/A1F")
def A1F():
    """
    Ich kann das Konzept von *immutable values* erläutern und dazu Beispiele anwenden. Somit kann ich dieses Konzept
    funktionaler Programmierung im Unterschied zu anderen Programmiersprachen erklären
    (z.Bsp. im Vergleich zu referenzierten Objekten)
    """

    def immutable_function(new_list):
        if not new_list:
            return 0
        for i in new_list:
            updated = new_list[1:]
            return i + immutable_function(updated)

    result = immutable_function([1, 2, 3, 4, 5])
    return str(result)


@app.route("/A1E")
def A1E():
    """
    Ich kann aufzeigen wie Probleme in den verschiedenen Konzepten (OO, prozedural und funktional) gelöst werden und
    diese miteinander vergleichen.
    """
    return "<a href='/A1E/OOP'><button>Go to OOP solution</button></a><br>" \
           "<a href='/A1E/procedural'><button>Go to procedural solution</button></a><br>" \
           "<a href='/A1E/functional'><button>Go to functional solution</button></a><br>"


@app.route("/A1E/OOP")
def OOP():
    class Car:
        def __init__(self, brand, model):
            self.brand = brand
            self.model = model

        def display_info(self):
            return f"Brand: {self.brand}, Model: {self.model}"

    my_car = Car("Toyota", "Corolla")
    return my_car.display_info()


@app.route("/A1E/procedural")
def procedural():
    def add_and_multiply(value):
        added = value + 3
        multiplied = value * 3
        return f"3 and 10... added: {added}, multiplied: {multiplied}"

    value = 10
    return str(add_and_multiply(value))


@app.route("/A1E/functional")
def functional():
    def multiply_numbers(a, b):
        return a * b

    def add_numbers(a, b):
        return a + b

    return f"3 and 5:<br><br>added = {add_numbers(3, 5)}<br><br>multiplied = {multiply_numbers(3, 5)}"


@app.route("/B1G")
def B1G():
    """
    Ich kann ein Algorithmus erklären
    """
    return ...


@app.route("/B1F")
def B1F():
    """
    Ich kann Algorithmen in funktionale Teilstücke aufteilen
    """
    return ...


@app.route("/B1E")
def B1E():
    """
    Ich kann Funktionen in zusammenhängende Algorithmen implementieren
    :return:
    """
    return ...


@app.route("/B2G")
def B2G():
    """
    Ich kann Funktionen als Objekte behandeln und diese in Variablen speichern und weitergeben.
    """
    return ...


@app.route("/B2F")
def B2F():
    """
    Ich kann Funktionen als Argumente für andere Funktionen verwenden und dadurch höherwertige Funktionen erstellen.
    :return:
    """
    return ...


@app.route("/B2E")
def B2E():
    """
    Ich kann Funktionen als Objekte und Argumente verwenden, um komplexe Aufgaben. (Anwenden von Closures)
    """
    return ...


@app.route("/B3G")
def B3G():
    """
    Ich kann einfache Lambda-Ausdrücke schreiben, die eine einzelne Operation durchführen, z.B. das
    Quadrieren einer Zahl oder das Konvertieren eines Strings in Großbuchstaben.
    """
    return ...


@app.route("/B3F")
def B3F():
    """
    Ich kann Lambda-Ausdrücke schreiben, die mehrere Argumente verarbeiten können.
    """
    return ...


@app.route("/B3E")
def B3E():
    """
    Ich kann Lambda-Ausdrücke verwenden, um den Programmfluss zu steuern, z.B. durch Sortieren von Listen basierend auf
    benutzerdefinierten Kriterien.
    """
    return ...


@app.route("/B4G")
def B4G():
    """
    Ich kann die Funktionen Map, Filter und Reduce einzeln auf Listen anwenden.
    """
    return ...


@app.route("/B4F")
def B4F():
    """
    Ich kann Map, Filter und Reduce kombiniert verwenden, um Daten zu verarbeiten und zu manipulieren, die komplexere
    Transformationen erfordern.
    """
    return ...


@app.route("/B4E")
def B4E():
    """
    Ich kann Map, Filter und Reduce verwenden, um komplexe Datenverarbeitungsaufgaben zu lösen, wie z.B. die Aggregation
    von Daten oder die Transformation von Datenstrukturen.
    """
    return ...


@app.route("/C1G")
def C1G():
    """
    Ich kann einige Refactoring-Techniken aufzählen, die einen Code lesbarer und verständlicher machen.
    """
    return ...


@app.route("/C1F")
def C1F():
    """
    Ich kann mit Refactoring-Techniken einen Code lesbarer und verständlicher machen.
    """
    return ...


@app.route("/C1E")
def C1E():
    """
    Ich kann die Auswirkungen des Refactorings auf das Verhalten des Codes einschätzen und sicherstellen, dass das
    Refactoring keine unerwünschten Nebeneffekte hat.
    """
    return ...


if __name__ == '__main__':
    app.run(debug=True)
