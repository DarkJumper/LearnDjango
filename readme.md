# Django

Es muss zwingend ein Virtuel Envierment anglegt werden.
Das Projekt wird erstellt durch django-admin startproject *Name*.
Damit der Server gestartet werden kann muss ins dir des Projectes gewechselt werden. Dort  muss über das Terminal python manage.py ausgeführt werden.
Um unter Dateien zu erstellen muss in dem dir der  Seite der befehl python manage.py startapp *Name* angegeben werden um grund gerüst zu erstellen.

## Funktion der Dateien
### Projekt

### APP
| Datei  | Anmerkunng|
|----| ---- |
| Ordner (Migrations)    | Einrichtung der Datenbank (Automatisch von Django gepflegt) |
| admin.py                        | Konfigurations für die Admin Oberfläsche                                       |
| apps.py                           | Speziefische Programmier Möglichkeiten für die App                  |
| models.py                      | Definition der Model (Wichtig für Datenbank)                                |
| tests.py                           | Unit Tests für Software                                                                |
| views.py                         | Definierung der Ausgabe (HTML /CSS) |

## Basic einstellungen
### Settings
| Bezeichnung | Bedeutung/Einstellungen |
|----| ---- |
| SECRET_KEY                  | Sollte bei Offiziellen Projekten nicht veröffentlicht werden |
| DEBUG                            | Sollte nur Aktiv sein wenn man am Testen ist wenn Live dann am besten *FALSE* |
| ALLOWED_HOSTS       | Angabe der Erlaubten Hosts |
|INSTALLED_APPS         | Jede weiter app muss dort eingefügt werden in unserem beispiel muss "polls" eingetragen werden |
| DATABASES                   | Standart mäßg SQLite Datenbank |
| LANGUAGE>_CODE   | Es sollte auf  ``` "de-de" ``` gestellt werden (Sprache für den Webserver) |
| TIME_ZONE                   | Zeit zone der Webseite ```"Europe/Berlin" ``` |

## Programmieren der Models
### Models
 Es muss erstmal festgestellt werden was für Objekte gebraucht werden.
 In diesem Beispiel wären es:

```
Umfrageseite
-- Poll
--- Questions
--- Choices
---- title
---- votes  
```
> Die Objekte müssen in der Models.py eingefügt werden.

Damit die *models*  jetzt in die Datenbank eingefügt werden kann muss der befehl
``` python manage.py makemigrations ```
Django versucht nun ohne Datenverluste die neuen daten in die vorhanden zu intergrieren.
Damit die Daten jetzt in die Datenbank geändert wird muss der befehl `python manage.py migrate` ausgeführt werden.
So kann ohne großen aufwand änderungen an der Datenbank umgesetzt werden.

## Administrator Oberfläsche
#  Models freigabe
Damit ein Model für den Admin freigegeben wird muss `admin.site.register(*Modul*) ` eingefügt werden mit den Protokollen.

# Admin Oberfläschlich
Es muss ein Admin user erstellt werden dies kann durch den befehl `python manage.py creatsuperuser` erstellt werden.>
Dort wird dann nach einem name / Email (falls gewünscht) und ein Passwort (8 Zeichen) gefragt.
Anschließend kann über den benutzter sich in der Verwaltungs Oberfläsche eingeloggt werden.
Damit dort die Abfragen mit name o.ä. Angezeigt werden muss die `__str__` funktion o.ä. beschrieben werden.
Über die Django shell können ebenfalls zu gegriffen werden -> `python manage.py shell`.
Es kann auf einzelne Objekte dort zugegriffen werden mit `.objects.all()` *in unserem Beispiel wäre der Befehl `poll.objects.all()`*dies gibt dort eine liste aus. Mit  `.save()` kann jedes Objekt abgespeichert werden. 


## Views Bearbeiten
# 
