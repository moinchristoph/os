# Einen Sprachstil-Skill anlegen

Gilt für das Setup (Phase 5) und für jeden späteren neuen Stil.

## 1. Proben analysieren

Die 3–5 Beispieltexte auf allen Ebenen auswerten:
- **Anrede:** Du/Sie, Begrüßung und Verabschiedung (wörtlich zitieren)
- **Satzbau:** typische Satzlänge, Rhythmus, Satzanfänge, Nebensätze
- **Wortschatz:** Lieblingswörter und wiederkehrende Formulierungen, Fachwort oder Alltagssprache, Anglizismen
- **Zeichensetzung:** Gedankenstriche, Klammern, Ausrufezeichen, Emojis (welche, wie oft, wo nie)
- **Tonalität:** warm oder nüchtern, direkt oder vorsichtig, Humor (Art und Dosis), Nähe oder Distanz
- **Heikle Situationen:** Preise, Absagen, Kritik, Verzögerungen. Fehlt eine Probe dazu, nach einem Beispiel fragen.
- **Tabus:** was nie vorkommt, plus die Antwort auf „Welche Wörter würdest du nie benutzen?"

## 2. Skill schreiben

Datei: `.claude/skills/sprachstil-<kanal>/SKILL.md`, z. B. `sprachstil-instagram`, `sprachstil-website-en`.

```markdown
---
name: sprachstil-<kanal>
governance: gruen
description: Sprachregeln von {{NAME}} für <Kanal/Zweck>. Immer laden, bevor Texte für <Kanal> geschrieben oder überarbeitet werden. Auslöser – <typische Sätze, z. B. "schreib einen Post", "Website-Text", "Antwort an eine Kundin">.
---

# Sprachstil <Kanal>

## Kurzprofil
<3–4 Sätze: Wie klingt {{NAME}} hier? Für wen wird geschrieben?>

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
- Keine Gedankenstriche als Satzzeichen, wenn {{NAME}} sie in den Proben nicht nutzt.

## Proben
<Die Originaltexte oder Auszüge, mit Quelle. Nie umschreiben.>
```

Die GUT-Beispiele kommen immer aus den echten Proben, nie erfunden. Basiert ein Stil mangels Proben auf einem anderen Stil, steht das im Kurzprofil.

## 3. Test

Zwei kurze Probetexte im neuen Stil schreiben, zu typischen Alltagssituationen aus dem Business (aus `Business/angebote.md` und `zielgruppen.md`). Fragen: „Hättest du das so geschickt?" Jede Korrektur sofort als Regel einarbeiten. Höchstens zwei Runden.
