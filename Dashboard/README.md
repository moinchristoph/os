# Dashboard

Zuletzt aktualisiert: –

Eine lokale HTML-Seite, die zeigt, wo das Business steht. `build.py` liest die Markdown-Dateien
des Systems und füllt `vorlage.html`. Ergebnis: `dashboard.html` (nicht versioniert).
Neu bauen und öffnen: `/dashboard` oder `python3 Dashboard/build.py && open Dashboard/dashboard.html`.

## Dateien

- `vorlage.html` – Aufbau und Design. Wird nur mit Impeccable geändert, danach immer `impeccable polish`.
- `build.py` – liest die Quellen, ersetzt die Platzhalter `{{…}}`.
- `einstellungen.json` – Name, Wortmarke, Logo-Pfad (z. B. `Business/marke/logo.svg`). Ohne Logo zeigt das Dashboard die Wortmarke.
- `daten/` – Rohdaten aus angebundenen Systemen (nicht versioniert, kann Personenbezug haben).

## Reiter

| Reiter | Inhalt | Quelle |
|---|---|---|
| Übersicht | aktive Aufgaben, offene Punkte, Jahresziele, zuletzt erledigt | `Aufgaben.md`, `Business/*.md`, jüngstes Tageslog |
| Wissen | Zielgruppen, Produkte und Preise, Positionierung, Marke | `Business/` |

## Datenquellen

Neue Quellen werden einzeln angebunden. Jede bekommt ihren eigenen Reiter oder eine Karte in der Übersicht.

| System | Wofür | Status |
|---|---|---|
<!-- Status: gewünscht | in Arbeit | angeschlossen YYYY-MM-DD -->

## Wunsch-Kennzahlen

<!-- Welche Zahlen sollen sichtbar werden, sobald die Quellen angebunden sind? -->
