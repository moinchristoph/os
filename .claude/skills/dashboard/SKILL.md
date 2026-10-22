---
name: dashboard
governance: gruen
description: Baut das eigene Dashboard neu und öffnet es – liest Aufgaben, Ziele, Business-Wissen und das jüngste Tageslog, holt Zahlen aus angebundenen Systemen und schreibt Dashboard/dashboard.html. Liest nur, ändert nie etwas in angebundenen Systemen. Auslöser – "/dashboard", "Dashboard", "zeig mir mein Business", "wie steht das Business".
---

# Dashboard – neu bauen und öffnen

## 1. Angebundene Quellen holen

`Dashboard/README.md`, Tabelle „Datenquellen", lesen. Für jede Zeile mit Status `angeschlossen`:
die Zahlen über den genannten Connector oder das genannte Skript holen und nach `Dashboard/daten/<quelle>.json` schreiben.
Schlägt eine Quelle fehl: weitermachen, am Ende melden, welche Quelle fehlt und warum. Nie alte Zahlen als neu ausgeben.

Gibt es noch keine angeschlossene Quelle: diesen Schritt überspringen.

## 2. Bauen

`python3 Dashboard/build.py` ausführen.
- Fehler → Meldung zeigen und beheben, nicht übergehen.
- Hinweise (fehlendes Logo, unbekannte Platzhalter) → in einer Zeile weitergeben.

In Cowork ohne Shell: sagen, dass der Build in Claude Code läuft, und stattdessen die Übersicht als Text ausgeben (aktive Aufgaben, Jahresziele, Anzahl offene Punkte).

## 3. Öffnen

`open Dashboard/dashboard.html`. Dann in 2–3 Zeilen: was auffällt (überfällige Aufgaben, viele offene Punkte, Ziel ohne Fortschritt).

## Design ändern

Wünsche zum Aussehen oder neue Reiter → nach `.claude/skills/setup/references/dashboard.md` mit Impeccable umsetzen, **danach immer `impeccable polish`**, neu bauen, ansehen.
