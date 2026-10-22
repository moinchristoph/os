---
name: wochenrueckblick
governance: gruen
description: Erstellt den Wochenrückblick von {{NAME}} im KI-Betriebssystem aus den Tageslogs – Ergebnisse, Zielfortschritt, Learnings und Fokus für die nächste Woche. Auslöser – "/wochenrueckblick", "Wochenrückblick", "wie war meine Woche", "Woche abschließen". Optionales Argument – Kalenderwoche, z. B. "KW38".
---

# Wochenrückblick

## 1. Welche Woche?

`date "+%Y-%m-%d %A KW%V"` ausführen.
- Argument angegeben (z. B. `KW38`) → diese Woche.
- Sonst: Donnerstag–Sonntag → **laufende** Woche. Montag–Mittwoch → **Vorwoche**.
- Sag in einem Satz, welche Woche du auswertest (KW + Datumsbereich Mo–So).

Zieldatei: `Logs/Rueckblicke/YYYY-KWXX.md` (ISO-Woche, zweistellig). Existiert sie schon → {{NAME}} fragen: ergänzen oder neu schreiben?

## 2. Material lesen

- Alle Tageslogs Mo–So der Woche aus `Logs/YYYY/`
- `Business/ziele.md`
- `Aufgaben.md`
- Der Rückblick der Vorwoche (Abschnitt „Fokus nächste Woche"), falls vorhanden
- `Memory/INDEX.md` → Einträge mit Datum in dieser Woche

Fehlen Logs für einzelne Arbeitstage, nenne das offen („Für Mi gibt es kein Log") und frag, ob etwas nachzutragen ist.

## 3. Reflexion – kurz fragen, bevor du schreibst

Stell diese drei Fragen **in einer Nachricht** und warte auf die Antwort:
1. Was war dein wichtigster Fortschritt diese Woche?
2. Was hat dich gebremst oder Energie gekostet?
3. Was nimmst du dir für nächste Woche vor?

## 4. Rückblick schreiben

```markdown
# Wochenrückblick YYYY-KWXX (TT.MM.–TT.MM.YYYY)

## Die Woche in 3 Sätzen

## Erledigt – nach Bereich
### Business
### Projects
### Website
### Content
### Kunden
### Dashboard
### Sonstiges (Termine, Kundengespräche, …)

## Zielfortschritt
| Ziel (aus Business/ziele.md) | Beitrag diese Woche | Einschätzung |
|---|---|---|
<!-- Einschätzung: auf Kurs / zu langsam / kein Beitrag -->

## Vorsatz vs. Realität
<!-- Fokus aus dem letzten Rückblick: was davon wurde umgesetzt? -->

## Was lief gut

## Was hat gebremst

## Offene Schleifen
<!-- Punkte, die in mehreren Logs unter „Offen / Morgen" auftauchen und nicht erledigt wurden -->

## Fokus nächste Woche (max. 3)
1.
2.
3.
```

Regeln:
- Nur belegen, was in Logs steht oder {{NAME}} gesagt hat. Leere Bereiche mit „–".
- Ehrlich sein: Wenn die Woche nichts auf die Ziele eingezahlt hat, steht das so drin.
- Muster benennen (z. B. „Content rutscht seit 3 Wochen nach hinten").

## 5. Nachbereitung – jeweils nur nach OK

- „Fokus nächste Woche" in `Aufgaben.md` übernehmen (3er-Regel beachten).
- Dauerhaft relevante Learnings per `merken`-Skill speichern (max. 2 Vorschläge).
- Zeile im heutigen Tageslog unter `## Verlauf` ergänzen: `- HH:MM – Wochenrückblick KWXX erstellt → Logs/Rueckblicke/YYYY-KWXX.md`
