# Dashboard aufbauen und erweitern

## Aufbau, der immer gilt

- **Menüleiste links**, oben links das Logo (`Business/marke/logo.*`) oder, ohne Logo, die Wortmarke aus `Dashboard/einstellungen.json`.
- **Reiter „Übersicht"**: aktive Aufgaben, offene Punkte, Jahresziele, zuletzt erledigt.
- **Reiter „Wissen"**: Zielgruppen, Produkte und Preise, Positionierung, Marke. Unterpunkte im Menü springen zum Abschnitt.
- Auf dem Handy wird die Menüleiste zur Leiste oben.
- Lokale HTML-Datei, keine Cloud, keine Abhängigkeiten. Kundendaten bleiben auf dem Rechner.

## Gestalten mit Impeccable

1. Impeccable laden, Kontext ist `DESIGN.md` im Hauptordner.
2. In `Dashboard/vorlage.html` nur ändern: die Tokens in `:root`, die Stile, Schriften (lokal oder Google Fonts), Abstände, Details wie Icons. Nicht ändern: die Platzhalter `{{…}}`, die Attribute `data-reiter`, `data-seite`, die `id`s der Wissens-Abschnitte.
3. Die Oberfläche ist ein Arbeitswerkzeug. Ruhig, gut lesbar, klare Hierarchie, die Marke zeigt sich in Farbe, Schrift und Logo, nicht in Effekten.
4. `python3 Dashboard/build.py`, ansehen, Fehler beheben.
5. **Immer zum Schluss `impeccable polish`** auf `Dashboard/vorlage.html`, danach neu bauen und noch einmal ansehen. Erst dann zeigen.

## Später erweitern: eine neue Datenquelle

1. Zeile in `Dashboard/README.md`, Tabelle „Datenquellen", auf `in Arbeit` setzen.
2. Daten holen: über einen Connector (Claude holt die Zahlen im Skill `/dashboard` und schreibt sie nach `Dashboard/daten/<quelle>.json`) oder über ein kleines Skript, wenn das System eine API hat. Zugangsdaten nur im Schlüsselbund.
3. `build.py` um eine Funktion ergänzen, die die JSON-Datei liest, und um einen Platzhalter.
4. In `vorlage.html` mit Impeccable eine Karte oder einen neuen Reiter anlegen, danach `impeccable polish`.
5. Schritt im Skill `/dashboard` ergänzen, damit die Quelle bei jedem Aufruf frisch geholt wird.
6. Status auf `angeschlossen YYYY-MM-DD`, Zeile im Tageslog.
