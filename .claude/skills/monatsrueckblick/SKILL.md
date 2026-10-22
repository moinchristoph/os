---
name: monatsrueckblick
governance: gruen
description: Erstellt den Monatsrückblick im KI-Betriebssystem aus Wochenrückblicken und Tageslogs, prüft den Fortschritt auf die Ziele und aktualisiert Business/ziele.md. Auslöser – "/monatsrueckblick", "Monatsrückblick", "Monat abschließen", "wie war mein Monat". Optionales Argument – Monat, z. B. "2026-08" oder "August".
---

# Monatsrückblick

Der Monatsrückblick ist der Moment, in dem die **Ziele aktualisiert** werden. Er ist strategischer als der Wochenrückblick: weniger „was habe ich getan", mehr „bin ich auf dem richtigen Weg".

## 1. Welcher Monat?

`date "+%Y-%m-%d"` ausführen.
- Argument angegeben → dieser Monat.
- Sonst: Tag 1–10 des Monats → **Vormonat**. Ab Tag 11 → **laufender** Monat (dann als Zwischenstand kennzeichnen).

Zieldatei: `Logs/Rueckblicke/YYYY-MM-monat.md`. Existiert sie schon → fragen: ergänzen oder neu schreiben?

## 2. Material lesen

- Alle Wochenrückblicke des Monats aus `Logs/Rueckblicke/`
- Tageslogs des Monats – bei vorhandenen Wochenrückblicken nur die Feierabend-Abschnitte überfliegen; fehlen Wochenrückblicke, die Logs vollständig lesen
- `Business/ziele.md` (komplett) und `Business/angebote.md`
- `Memory/INDEX.md` → Einträge des Monats
- Der letzte Monatsrückblick, falls vorhanden
- `Projects/*/PROJEKT.md` → Status der laufenden Projekte

## 3. Zahlen & Reflexion abfragen

Frag **in einer Nachricht** (Punkte dürfen übersprungen werden):
1. Zahlen des Monats: Anfragen, Aufträge, Umsatz – was du parat hast.
2. Worauf bist du diesen Monat stolz?
3. Was würdest du rückblickend anders machen?
4. Stimmen deine Ziele noch – oder hat sich etwas verschoben?

## 4. Rückblick schreiben

```markdown
# Monatsrückblick YYYY-MM (Monatsname)

## Der Monat in 5 Sätzen

## Zahlen
| Kennzahl | Wert | Vormonat |
|---|---|---|

## Zielfortschritt
| Ziel | Stand Monatsanfang | Stand jetzt | Einschätzung |
|---|---|---|---|

## Wichtigste Ergebnisse – nach Bereich
### Business
### Projects
### Website
### Content
### Kunden
### Dashboard

## Projekte – Status
| Projekt | Status | Nächster Meilenstein |
|---|---|---|

## Muster & Learnings
<!-- Was zieht sich durch die Wochen? Was hat funktioniert, was nicht? -->

## Stoppen / Starten / Weitermachen

## Fokus nächster Monat (max. 3)
```

Regeln: nur Belegtes, ehrliche Einschätzung, leere Bereiche mit „–". Keine Zahlen erfinden – fehlende Werte als „k. A." eintragen.

## 5. Ziele aktualisieren – Kernschritt

Schlage konkrete Änderungen an `Business/ziele.md` vor (als Vorher/Nachher-Liste):
- Fortschrittsstände der Ziele aktualisieren
- Monatsfokus auf den neuen Monat setzen
- erreichte Ziele nach „Erreicht" verschieben, überholte Ziele streichen oder anpassen

Erst nach OK schreiben. Dabei „Zuletzt aktualisiert" auf heute setzen und eine Zeile im Änderungsverlauf der Datei ergänzen.

## 6. Hygiene – jeweils nur nach OK

- `Memory/`: Einträge, die überholt sind oder inzwischen in einem Kerndokument stehen → aktualisieren oder im Index als `veraltet` markieren.
- `Aufgaben.md`: Punkte unter „Als Nächstes" / „Irgendwann", die seit Wochen liegen → streichen, terminieren oder bewusst behalten.
- `Projects/`: abgeschlossene Projekte → Ergebnisse in den Zielbereich verschieben, Status in `PROJEKT.md` auf „abgeschlossen".
- Zeile im heutigen Tageslog unter `## Verlauf` ergänzen.
