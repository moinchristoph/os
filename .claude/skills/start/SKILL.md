---
name: start
governance: gruen
description: Startet den Arbeitstag im KI-Betriebssystem – legt das Tageslog an, zeigt die relevanten Aufgaben und stellt sicher, dass maximal 3 Aufgaben aktiv sind. Auslöser – "/start", "Start", "Guten Morgen", "los geht's", "was steht heute an".
---

# Start – Tag beginnen

Ziel: In unter einer Minute ist klar, woran heute gearbeitet wird. Kurz halten, nicht dozieren.

## 1. Datum bestimmen

Führe `date "+%Y-%m-%d %A KW%V %H:%M"` aus (falls keine Shell verfügbar: Datum aus dem Kontext nehmen).
Pfad des heutigen Logs: `Logs/YYYY/YYYY-MM-DD.md`.

## 2. Kontext lesen

- `Aufgaben.md`
- `Business/ziele.md` (nur den Abschnitt zum aktuellen Fokus / Quartal)
- Das **letzte vorhandene Tageslog** (jüngste Datei in `Logs/YYYY/`) – vor allem `### Offen / Morgen`
- Falls vorhanden: der jüngste Wochenrückblick in `Logs/Rueckblicke/` (Abschnitt „Fokus nächste Woche")

## 3. Tageslog anlegen

Existiert das heutige Log schon → **nicht überschreiben**. Nur die Übersicht (Schritt 5) ausgeben und den Stand aus dem Log berücksichtigen.

Sonst anlegen nach diesem Schema:

```markdown
# Log YYYY-MM-DD (Wochentag, KW XX)

## Start
- Gestartet: HH:MM
- Fokus heute: <ein Satz, wird in Schritt 6 ergänzt>

## Aktive Aufgaben
1. …
2. …
3. …

## Verlauf
<!-- Eine Zeile pro Ergebnis: - HH:MM – Was → Datei(en) -->

## Feierabend
<!-- Wird vom Skill `feierabend` ausgefüllt -->
```

## 4. Aufgaben prüfen (3er-Regel)

- **Mehr als 3 aktiv** → fragen, welche in „Als Nächstes" zurückwandern. Erst danach weiter.
- **Weniger als 3 aktiv** → passende Kandidaten aus „Als Nächstes" und aus „Offen / Morgen" des letzten Logs vorschlagen (nicht selbst verschieben, erst nach OK).
- Aufgaben mit Fälligkeit heute/überfällig oder in den nächsten 3 Tagen hervorheben.
- Punkte aus „Offen / Morgen" des letzten Logs, die nicht in `Aufgaben.md` stehen, erwähnen und anbieten, sie aufzunehmen.

## 5. Übersicht ausgeben

Kompakt, in dieser Reihenfolge:

1. **Fokus** – eine Zeile: aktuelles Ziel aus `Business/ziele.md`, auf das die Woche einzahlt.
2. **Aktiv (max. 3)** – nummerierte Liste, mit Fälligkeit falls vorhanden.
3. **Fällig / dringend** – nur wenn es etwas gibt.
4. **Warten auf** – nur wenn es etwas gibt, eine Zeile pro Punkt.
5. **Von gestern offen** – nur wenn es etwas gibt.

Hinweise, nur wenn zutreffend (je eine Zeile):
- Das letzte Tageslog hat keinen ausgefüllten Feierabend-Abschnitt → anbieten, ihn kurz nachzutragen.
- Montag (oder erster Arbeitstag der Woche) und für die Vorwoche existiert kein `Logs/Rueckblicke/YYYY-KWXX.md` → an `/wochenrueckblick` erinnern.
- Erste Arbeitstage des Monats und für den Vormonat existiert kein `Logs/Rueckblicke/YYYY-MM-monat.md` → an `/monatsrueckblick` erinnern.
- `Business/ziele.md` wurde laut „Zuletzt aktualisiert" seit über 5 Wochen nicht angefasst → darauf hinweisen.

## 6. Abschluss

Frag genau eine Frage: **„Womit startest du?"**
Trag die Antwort als „Fokus heute" ins Log ein und leg direkt mit dieser Aufgabe los.
