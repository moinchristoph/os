# Briefing: Ausbau 2.0 des KI-Betriebssystems

Status: **Entwurf von Claude, noch nicht freigegeben.** Erstellt am 2026-11-15 aus dem Ist-Stand des Repos (`294315a`).
Die Pakete A und B sind Vorschläge. Die Punkte in Paket C sind belegte Befunde aus dem Repo.

## Ziel

Die Vorlage bleibt, was sie ist: ein leerer Ordner, den `/setup` einrichtet. Der Ausbau schließt zwei Lücken
(Kundenanfragen haben keinen Ablauf, das Dashboard zeigt keine Zahlen) und räumt Widersprüche zwischen Regeln,
Skills und Einstellungen auf.

## Leitplanken

- Die Vorlage bleibt leer: keine persönlichen Daten, keine Beispieldaten in Nutzerdateien.
- Unverändert bleiben: Skill `website`, alles zu Impeccable, Skill `sprachstil` samt `references/sprachstil.md`.
- Neue Skills folgen dem Aufbau der bestehenden (Frontmatter `name`, `governance`, `description` mit Auslösern, nummerierte Schritte).
- `build.py` bleibt ohne Abhängigkeiten (nur Standardbibliothek).
- Reihenfolge: C1–C3, dann A, dann B, dann C4–C6. Ein Commit pro Schritt.

## Paket C, Teil 1 – Bereinigung vor dem Ausbau

### C1 – Widersprüche in Regeln und Skills auflösen

| Befund | Wo | Vorschlag |
|---|---|---|
| „8 Etappen", gezählt werden 9 (0 bis 8) | `README.md`, `setup/SKILL.md` (Begrüßung) | „9 Etappen" oder Vorprüfung nicht mitzählen und das so sagen |
| `Memory/` „wird nur über den Skill `merken` geschrieben", `monatsrueckblick` Schritt 6 ändert Memory-Einträge und Index | `CLAUDE.md` Routing, `monatsrueckblick/SKILL.md` | Routing-Zeile um die Hygiene im Monatsrückblick ergänzen |
| `setup` sagt „nie in `.claude/` schreiben", `neuer-ordner` Schritt 3.5 und 3.6 ändern drei Skill-Dateien in `.claude/` | `neuer-ordner/SKILL.md`, `merken/SKILL.md`, beide Rückblick-Skills | Bereichsliste aus der Routing-Tabelle in `CLAUDE.md` lesen statt sie in den Skills fest zu verdrahten. `neuer-ordner` fasst dann nur noch `CLAUDE.md` und `Memory/INDEX.md` an |
| Session-Start liest 3 Dateien, „Kontext laden" nennt 4 Stufen | `CLAUDE.md` | Session-Start auf „Kontext laden" verweisen lassen, eine Liste |
| `start` liest den „Abschnitt zum aktuellen Fokus / Quartal", in `ziele.md` heißen die Abschnitte „Quartalsziele" und „Monatsfokus" | `start/SKILL.md` | Abschnittsnamen wörtlich nennen |

### C2 – `.claude/settings.json` an die Regeln in `CLAUDE.md` angleichen

| Regel in `CLAUDE.md` | Stand in `settings.json` | Vorschlag |
|---|---|---|
| kein `rm -rf` **außerhalb** dieses Ordners | `deny: Bash(rm -rf*)` sperrt jedes `rm -rf` | Regeltext an die Einstellung angleichen (strenger ist hier richtig) |
| keine heruntergeladenen Skripte (`curl … \| bash`) | fehlt | `ask` für `Bash(curl*)` und `Bash(wget*)` |
| kein Löschen von Branches | fehlt | `deny: Bash(git branch -D*)`, `Bash(git push*--delete*)` |
| Rückfrage vor `package.json`/Lockfiles | fehlt | `ask` für Edit/Write auf `**/package.json` und Lockfiles |
| Rückfrage vor neuen Paketen und Plugins | fehlt | `ask` für `Bash(npm install*)`, `Bash(pip install*)`, `Bash(npx*)` |
| Schlüsselbund nie auslesen | nur `find-generic-password`/`find-internet-password` | `Bash(security dump-keychain*)` ergänzen |

### C3 – Befehle, die nur auf dem Mac laufen

`open Dashboard/dashboard.html` (`dashboard`, `setup`, `Dashboard/README.md`) und `date … KW%V` setzen macOS bzw. eine Shell voraus.
Vorschlag: je Stelle einen Satz für Windows und Linux (`start`, `xdg-open`), sonst den Pfad nennen. Kein Umbau.

## Paket A – Kundenanfragen bekommen einen Ablauf

`Kunden/README.md` nennt ein „anonymes Anfragen-Log" und „Vorlagen für Angebote und Mails". Beides existiert nicht, kein Skill schreibt dorthin.

- **A1 – Skill `anfrage`** (`gelb`): erfasst eine Anfrage anonym in `Kunden/anfragen.md` (Datum, Kanal, Segment aus `zielgruppen.md`, Leistung aus `angebote.md`, Status: neu, Gespräch, Angebot, gewonnen, verloren, mit Grund). Kein Name, keine Kontaktdaten. Auslöser: „neue Anfrage", „Anfrage eintragen", „Anfrage ist geworden zu …".
- **A2 – Skill `angebot`** (`gelb`): schreibt einen Angebotsentwurf nach `Kunden/privat/` (nicht versioniert). Preise nur aus `Business/angebote.md`, Ton über `sprachstil`, bei `OFFEN:` nachfragen. Versendet nichts.
- **A3 – Anbindung an den Rhythmus:** `feierabend` fragt bereits nach Anfragen und trägt sie künftig über `anfrage` ein. `wochenrueckblick` und `monatsrueckblick` lesen die Zahlen aus `Kunden/anfragen.md`, statt sie abzufragen.

## Paket B – Dashboard Stufe 2

- **B1 – Projekte und Fälligkeiten:** Karte „Projekte" aus `Projects/README.md`. Überfällige und in 3 Tagen fällige Aufgaben aus `Aufgaben.md` (`· fällig: YYYY-MM-DD`) hervorheben.
- **B2 – Anfragen-Kennzahlen:** Karte in der Übersicht aus `Kunden/anfragen.md`: Anfragen im laufenden Monat, Quote gewonnen, Stand gegen die „Rechnung zum Umsatzziel" in `ziele.md`.
- **B3 – Datenquellen wirklich einlesen:** Der Skill `dashboard` schreibt `Dashboard/daten/<quelle>.json`, `build.py` liest diese Dateien nicht. Ein festes, kleines JSON-Format festlegen (Titel, Stand, Kennzahlen als Liste), `build.py` rendert je Datei eine Karte im Reiter „Zahlen". Fehlt die Datei oder ist sie älter als 7 Tage, steht das sichtbar dabei.

Gestaltung der neuen Karten nach den Regeln in `references/dashboard.md` (Impeccable, danach `polish`). In der Vorlage bleibt das neutrale Grunddesign.

## Paket C, Teil 2 – Nachziehen nach dem Ausbau

### C4 – `build.py` härten und testen

- `inline()` übernimmt Link-Ziele ungeprüft: nur `http(s)`, `mailto` und relative Pfade zulassen, Anführungszeichen maskieren.
- Der Markdown-Umsetzer kennt keine eingerückten Unterlisten und keine Code-Blöcke. Beides ergänzen oder sauber als Text ausgeben.
- `Dashboard/test_build.py` mit `unittest`: leere Vorlage, gefüllte Testdaten in einem temporären Ordner, kaputtes JSON.

### C5 – Übersichten nachziehen

Befehlstabelle in `CLAUDE.md`, Befehlstabelle und Ordnerliste in `README.md`, `Kunden/README.md`, `Dashboard/README.md` (Reiter, Datenformat),
`setup/references/dashboard.md` (Aufbau). Im `.gitignore` prüfen, ob `Kunden/anfragen.md` versioniert werden soll (Vorschlag: ja, weil anonym).

### C6 – Abschlussprüfung

Skript `pruefen.py` im Ordner `Dashboard/` oder als Schritt im Test: jeder Skill-Ordner steht in beiden Befehlstabellen, jedes Frontmatter hat
`name`, `governance`, `description`, `settings.json` ist gültiges JSON, außer den vier bekannten Platzhaltern in `CLAUDE.md` gibt es keine `{{…}}`.

## Abnahme – drei Testläufe in einem Wegwerf-Ordner außerhalb des Repos

1. **Leere Vorlage:** frische Kopie des Branches, `python3 Dashboard/build.py` endet mit Code 0, ohne Hinweise, ohne ungefüllte Platzhalter. `python3 -m unittest` in `Dashboard/` läuft durch. Die Konsistenzprüfung aus C6 meldet nichts.
2. **Gefülltes System:** in der Kopie Testdaten anlegen (Ziele, drei Aufgaben mit Fälligkeit, ein Projekt, fünf Anfragen, eine `daten/*.json`). Das Dashboard zeigt Projekt, überfällige Aufgabe, Anfragen-Zahlen und die Datenkarte mit den erwarteten Werten.
3. **Skill-Durchlauf von Hand:** `anfrage` und `angebot` Schritt für Schritt nach `SKILL.md` ausführen. Ergebnis: Zeile in `Kunden/anfragen.md` ohne Personenbezug, Entwurf in `Kunden/privat/` mit Preisen aus `angebote.md`, Zeile im Tageslog. `git status` zeigt den Entwurf nicht.

## Offene Entscheidungen

1. Sind A (Anfragen und Angebote) und B (Dashboard Stufe 2) die richtigen Ausbauten, oder war etwas anderes gemeint?
2. C1, dritte Zeile: Bereichsliste aus `CLAUDE.md` lesen (Vorschlag) oder die Freigabe-Fenster bei `neuer-ordner` hinnehmen?
3. C2: neue `ask`-Regeln für `curl`, `npm install`, `npx` bedeuten mehr Rückfragen im Alltag. Alle übernehmen oder nur die `deny`-Ergänzungen?
4. Dieses Briefing liegt in `Projects/system-ausbau/`. Vor dem Merge nach `main` löschen, damit die Vorlage leer bleibt?
