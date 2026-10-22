---
name: neuer-ordner
governance: gelb
description: Legt im KI-Betriebssystem einen neuen Hauptordner (Bereich) an und trägt die zugehörige Routing-Regel in die CLAUDE.md ein, damit Dokumente künftig korrekt einsortiert werden. Auslöser – "/neuer-ordner", "leg einen neuen Ordner an", "neuer Bereich", "ich brauche einen Ordner für". Optionales Argument – Name des Ordners.
---

# Neuer Ordner – Bereich mit Routing-Regel anlegen

Ein neuer Hauptordner ist nur dann sinnvoll, wenn er eine **eigene Routing-Regel** verdient. Sonst wird das System unübersichtlich.

## 1. Prüfen, ob es einen neuen Bereich braucht

Routing-Tabelle in `CLAUDE.md` lesen. Passt das Thema in einen bestehenden Bereich (oft: Unterordner in `Projects/` oder `Content/`)?
→ Dann das vorschlagen und begründen. Besteht die Nutzerin oder der Nutzer auf dem neuen Ordner: anlegen.

## 2. Klären (eine Nachricht, nur was noch fehlt)

- Name des Ordners (ein Wort, großgeschrieben wie die anderen: `Business`, `Projects`, …; keine Umlaute)
- Was gehört hinein? (1 Satz)
- Was gehört ausdrücklich **nicht** hinein bzw. wie grenzt er sich von den bestehenden Bereichen ab? (1 Satz)

## 3. Anlegen

1. Ordner erstellen.
2. `<Ordner>/README.md` schreiben: Zweck, was hinein gehört, was nicht, Namenskonvention für Dateien.
3. In `CLAUDE.md` eine neue Zeile in die Routing-Tabelle einfügen – direkt **vor** der Zeile `Memory/` (ohne Leerzeile, sonst bricht die Tabelle).
   Format: `| \`Name/\` | Gehört hinein | Gehört NICHT hinein |`
4. Überschneidet sich der neue Bereich mit einem bestehenden, die „Gehört NICHT hinein"-Spalte des bestehenden Bereichs anpassen.
5. `Memory/INDEX.md`: neuen Abschnitt `## <Name>` ergänzen, und im `merken`-Skill (`.claude/skills/merken/SKILL.md`) den Bereich in der `bereich:`-Zeile des Schemas ergänzen.
6. Die Rückblick-Skills (`wochenrueckblick`, `monatsrueckblick`): im Schema unter „nach Bereich" eine Zeile `### <Name>` ergänzen.

## 4. Bestehendes umziehen

Prüfen, ob vorhandene Dateien in den neuen Bereich gehören. Liste vorschlagen, erst nach OK verschieben.

## 5. Bestätigen

Kurz: Ordner angelegt, Routing-Regel (wörtlich zitieren), ggf. verschobene Dateien. Zeile im Tageslog unter `## Verlauf` ergänzen.
