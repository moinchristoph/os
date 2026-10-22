---
name: feierabend
governance: gruen
description: Schließt den Arbeitstag im KI-Betriebssystem ab – sammelt alle Ergebnisse des Tages, trägt sie ins Tageslog ein, räumt Aufgaben.md auf und hält fest, was morgen ansteht. Auslöser – "/feierabend", "Feierabend", "Schluss für heute", "Tag abschließen".
---

# Feierabend – Tag abschließen

Ziel: Der Tag ist vollständig dokumentiert, der Kopf ist frei, morgen kann `/start` nahtlos anknüpfen.

## 1. Datum & Log

`date "+%Y-%m-%d %A KW%V %H:%M"` ausführen. Heutiges Log: `Logs/YYYY/YYYY-MM-DD.md`.
Existiert es nicht (Tag ohne `/start`), lege es nach dem Schema aus `.claude/skills/start/SKILL.md` an.

## 2. Ergebnisse des Tages einsammeln

Aus **allen** Quellen – nicht nur aus dieser Sitzung, denn oft wird parallel in Claude Code und Cowork gearbeitet:

1. `## Verlauf` im heutigen Log (Einträge aus anderen Sitzungen).
2. Diese Unterhaltung: was wurde erstellt, entschieden, erledigt?
3. Heute geänderte Dateien:
   `find . -type f -newermt "$(date +%Y-%m-%d) 00:00" -not -path "./.claude/*" -not -path "./Logs/*" -not -name ".DS_Store"`
   (falls keine Shell verfügbar: überspringen)
4. `Aufgaben.md`: welche Aufgaben sind abgehakt?

Dann **einmal** fragen: „Gab es heute noch etwas außerhalb des Systems – Termine, Kundengespräche, Anfragen, Entscheidungen –, das ins Log soll?"

## 3. Feierabend-Abschnitt schreiben

Den Abschnitt `## Feierabend` im heutigen Log ersetzen durch:

```markdown
## Feierabend
- Abgeschlossen: HH:MM

### Erledigt
- … (Bereich/Projekt)

### Ergebnisse & Dateien
- `Pfad/zur/datei.md` – was ist neu/geändert

### Entscheidungen & Erkenntnisse
- …

### Offen / Morgen
- …
```

Regeln:
- Konkrete Ergebnisse statt Tätigkeiten („Angebotsseite fertig getextet", nicht „an Website gearbeitet").
- Leere Unterabschnitte mit „–" füllen, nicht weglassen – die Rückblick-Skills verlassen sich auf die Struktur.
- Nichts erfinden. Was nicht belegt ist, nachfragen oder weglassen.

## 4. Aufgaben.md aufräumen

- Abgehakte Aufgaben löschen (sie stehen jetzt unter „Erledigt" im Log).
- Neue offene Punkte nach „Als Nächstes" oder „Warten auf" eintragen.
- Prüfen: maximal 3 unter „Aktiv". Wenn ein Platz frei geworden ist, **nicht** automatisch auffüllen – das wird morgen bei `/start` entschieden.

## 5. Merkenswertes abfangen

Steckt in den Erkenntnissen des Tages etwas, das dauerhaft relevant ist (neuer Preis, Kundeneinsicht, Entscheidung zur Positionierung, funktionierendes Content-Format)?
Dann **vorschlagen**, es per `merken`-Skill zu speichern – maximal 2 Vorschläge, nur nach OK ausführen.

## 6. Abschluss

Kurze Zusammenfassung ausgeben (3–5 Zeilen): erledigt, wichtigstes Ergebnis, was morgen als Erstes ansteht.
Freitags (oder am letzten Arbeitstag der Woche) zusätzlich: „Magst du noch den `/wochenrueckblick` machen?"
Dann: Schönen Feierabend wünschen. Keine neuen Themen aufmachen.
