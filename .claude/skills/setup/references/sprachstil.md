# Einen Sprachstil anlegen

Gilt für das Setup (Phase 5) und für jeden späteren neuen Stil. Ein Stil ist eine Markdown-Datei in
`Business/sprachstile/`, kein eigener Skill. Der Skill `sprachstil` lädt die passende Datei. So läuft es
ohne Freigabe-Fenster und genauso in Cowork.

## 1. Proben analysieren

Die 3–5 Beispieltexte auf allen Ebenen auswerten:
- **Anrede:** Du/Sie, Begrüßung und Verabschiedung (wörtlich zitieren)
- **Satzbau:** typische Satzlänge, Rhythmus, Satzanfänge, Nebensätze
- **Wortschatz:** Lieblingswörter und wiederkehrende Formulierungen, Fachwort oder Alltagssprache, Anglizismen
- **Zeichensetzung:** Gedankenstriche, Klammern, Ausrufezeichen, Emojis (welche, wie oft, wo nie)
- **Tonalität:** warm oder nüchtern, direkt oder vorsichtig, Humor (Art und Dosis), Nähe oder Distanz
- **Heikle Situationen:** Preise, Absagen, Kritik, Verzögerungen. Fehlt eine Probe dazu, nach einem Beispiel fragen.
- **Tabus:** was nie vorkommt, plus die Antwort auf „Welche Wörter würdest du nie benutzen?"

## 2. Datei schreiben

Datei: `Business/sprachstile/<kanal>.md`, z. B. `instagram.md`, `website-en.md`, `mails-firmen.md`.

```markdown
# Sprachstil <Kanal>

Zuletzt aktualisiert: YYYY-MM-DD

**Wann:** <Kanal, Zweck, Zielgruppe, z. B. „Instagram-Posts und WhatsApp an Kursteilnehmer:innen">

## Kurzprofil
<3–4 Sätze: Wie klingt die Person hier? Für wen wird geschrieben?>

## Regeln
<15–25 Regeln, gegliedert nach den Ebenen aus der Analyse. Je Regel, wo sinnvoll:>
- **Regel** – Begründung
  - GUT: <Beispiel aus den echten Proben>
  - SO NICHT: <Gegenbeispiel>

## Tabus
- …

## Allgemeine Anti-KI-Regeln
- Keine Floskeln wie „In der heutigen Zeit", „Lass uns eintauchen", „Game-Changer".
- Kein „nicht X, sondern Y" als Stilmittel, keine Dreierlisten aus Gewohnheit.
- Keine Gedankenstriche als Satzzeichen, wenn sie in den Proben nicht vorkommen.

## Proben
<Die Originaltexte oder Auszüge, mit Quelle. Nie umschreiben. Namen von Kund:innen durch [Name] ersetzen.>
```

Die GUT-Beispiele kommen immer aus den echten Proben, nie erfunden. Basiert ein Stil mangels Proben auf einem anderen Stil, steht das im Kurzprofil.

## 3. Test

Zwei kurze Probetexte im neuen Stil schreiben, zu typischen Alltagssituationen aus dem Business (aus `Business/angebote.md` und `zielgruppen.md`). Fragen: „Hättest du das so geschickt?" Jede Korrektur sofort als Regel einarbeiten. Höchstens zwei Runden.

## 4. Eintragen

Zeile in `Business/marke.md`, Tabelle „Sprachstile": `| <Kanal> | Business/sprachstile/<kanal>.md | <wann> |`
