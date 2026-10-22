---
name: merken
governance: gruen
description: Speichert eine Zusammenfassung als dauerhaftes Kontextwissen in der Memory-Datenbank des KI-Betriebssystems (Ordner Memory/). Auslöser – "/merken", "merk dir das", "merke dir", "das musst du dir merken", "speicher das als Wissen", in Cowork auch "/memory". Optionales Argument – was gemerkt werden soll.
---

# Merken – Kontextwissen speichern

Ziel: Wissen aus dem Gespräch so ablegen, dass es in drei Monaten ohne das Gespräch verständlich und auffindbar ist.

## 1. Was soll gemerkt werden?

- Argument angegeben → das.
- „Merk dir das" ohne Argument → das zuletzt besprochene Thema bzw. Ergebnis der Unterhaltung.
- Wirklich unklar → eine kurze Rückfrage. Sonst nicht nachfragen, sondern machen.

## 2. Dublette prüfen

`Memory/INDEX.md` lesen. Gibt es schon einen Eintrag zum selben Thema → **diesen aktualisieren** (Inhalt ergänzen, `aktualisiert:` setzen) statt einen neuen anzulegen.

## 3. Memory-Datei schreiben

Pfad: `Memory/YYYY-MM-DD-kurzer-slug.md` (Datum per `date +%Y-%m-%d`).

```markdown
---
titel: <prägnant, suchbar>
datum: YYYY-MM-DD
aktualisiert: YYYY-MM-DD
bereich: Business | Projects | Content | Kunden | Website | Dashboard | Allgemein
tags: [tag1, tag2]
quelle: <woher stammt das – Gespräch, Kundencall, Artikel, eigene Erfahrung>
---

## Kern
<2–4 Sätze: die Essenz, so formuliert, dass sie ohne Vorwissen verständlich ist>

## Details
- <Fakten, Zahlen, Zitate, Begründungen – so knapp wie möglich, so vollständig wie nötig>

## Bedeutung für mich
<Wann ist das relevant? Was folgt daraus für Entscheidungen, Texte, Angebote?>
```

Regeln:
- Zusammenfassen, nicht transkribieren. Konkrete Zahlen, Namen und Formulierungen aber wörtlich erhalten.
- Relative Zeitangaben in absolute Daten umwandeln („nächsten Monat" → „Oktober 2026").
- Ein Thema pro Datei. Zwei Themen → zwei Dateien.
- Keine Passwörter, Zugangsdaten oder Bankdaten speichern.

## 4. Index aktualisieren

In `Memory/INDEX.md` im passenden Bereichs-Abschnitt eine Zeile ergänzen (neueste oben):
`- YYYY-MM-DD · [Titel](dateiname.md) – ein Satz, worum es geht · #tag1 #tag2`

## 5. Routing prüfen

Betrifft das Gemerkte ein **Kerndokument**? Beispiele:
- neuer Preis / neues Paket → `Business/angebote.md`
- Einsicht über Wunschkunden → `Business/zielgruppen.md`
- Entscheidung zu Auftritt/Abgrenzung → `Business/positionierung.md`
- neues oder geändertes Ziel → `Business/ziele.md`
- neue Aufgabe → `Aufgaben.md`

Wenn ja: die konkrete Änderung in einem Satz vorschlagen („Soll ich den Preis in `Business/angebote.md` auf 3.400 € ändern?") und erst nach OK ausführen.
Wenn nein: nichts weiter tun.

## 6. Bestätigen

Eine Zeile: was gespeichert wurde und wo. Dazu ggf. der Routing-Vorschlag. Kein weiterer Text.
Zeile im heutigen Tageslog unter `## Verlauf` ergänzen: `- HH:MM – Gemerkt: <Titel> → Memory/<datei>`
