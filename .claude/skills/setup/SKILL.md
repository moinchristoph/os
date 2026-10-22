---
name: setup
governance: gelb
description: Richtet das KI-Betriebssystem einmalig ein – holt Business, Stand und Ziele, Produkte und Preise, Zielkunden, entwickelt mit Impeccable das Brand Design aus Website und bestehendem Content, legt die Sprachstile an, notiert gewünschte Systeme und baut das erste Dashboard in der eigenen Marke. Merkt sich den Fortschritt und macht bei erneutem Aufruf an der richtigen Stelle weiter. Auslöser – "/setup", "Setup starten", "richte mein System ein", "Einrichtung fortsetzen".
---

# Setup – das System einrichten

Ziel: Am Ende kennt das System das Business, die Angebote, die Zielkunden, die Marke und den Ton,
und es gibt ein erstes Dashboard im eigenen Design. Dauer insgesamt 60–90 Minuten, in Etappen möglich.

## Grundprinzipien für das ganze Setup

- **Vor jeder Phase ankündigen:** was jetzt passiert, was du dafür brauchst, welche Datei dabei entsteht, wie lange es ungefähr dauert. Dann fragen, ob es losgeht.
- **Eine Frage pro Nachricht**, außer eine Phase sagt ausdrücklich etwas anderes. Jede Antwortform ist ok: Stichworte, langer Text, eingefügte Website-Texte, Dateien, Screenshots.
- **Nachhaken, bis es konkret ist.** Allgemeine Antworten („alle, die Hilfe brauchen", „faire Preise") nicht übernehmen, sondern mit einer Folgefrage schärfen. Höchstens zwei Nachfragen pro Punkt, dann das Beste daraus machen.
- **„Weiß ich nicht" oder „später" ist erlaubt.** Dann `OFFEN: <konkrete Frage>` in die Datei schreiben und weiter.
- **Nichts erfinden.** Keine Zahlen, Preise, Kundenstimmen oder Eigenschaften, die nicht gesagt wurden.
- **Nach jeder Phase:** in 1–2 Zeilen bestätigen, was wo gespeichert wurde, dann `Logs/setup-status.md` aktualisieren.
- Die Fragen je Phase stehen in `references/fragen.md`. Dort steht auch, was aus den Antworten in welche Datei kommt.
- **Nie in `.claude/` schreiben.** Claude Code schützt diesen Ordner, jede Datei dort würde ein Freigabe-Fenster auslösen. Alles, was das Setup erzeugt, liegt in `Business/`, `Dashboard/`, `Logs/`, `Aufgaben.md`, `CLAUDE.md`, `DESIGN.md` und `PRODUCT.md`.
- **Fachbegriffe übersetzen.** Die Person kennt sich mit KI und Technik nicht aus. Begriffe wie Skill, Markdown, Repo, Terminal nur mit einem Halbsatz Erklärung, und nie einen Befehl zum Abtippen geben, wenn Claude ihn selbst ausführen kann.

## Schritt 0 – Wo stehen wir?

1. `Logs/setup-status.md` lesen.
   - Gibt es die Datei nicht → neues Setup. Datei aus dem Schema unten anlegen und mit der Begrüßung starten.
   - Gibt es sie → kurz sagen, welche Phasen erledigt sind, und an der ersten offenen Phase weitermachen. Steht dort, dass eine Phase übersprungen wurde, anbieten, sie jetzt nachzuholen.
2. Begrüßung bei neuem Setup (sinngemäß, kurz): „Ich richte jetzt dein KI-Betriebssystem ein. Das läuft in 8 Etappen, insgesamt etwa 60–90 Minuten. Du kannst jederzeit Pause machen, ich merke mir, wo wir sind. Am Ende kennt das System dein Business, deine Angebote, deine Kunden, deine Marke und deinen Ton, und du hast ein erstes Dashboard in deinem Design."

Schema für `Logs/setup-status.md`:

```markdown
# Setup-Status

Gestartet: YYYY-MM-DD

- [ ] 0 Vorprüfung
- [ ] 1 Business und Stand
- [ ] 2 Produkte und Leistungen
- [ ] 3 Zielkunden
- [ ] 4 Brand Design
- [ ] 5 Sprachstile
- [ ] 6 Systeme anbinden
- [ ] 7 Dashboard
- [ ] 8 Abschluss

## Notizen
<!-- übersprungene Punkte, Entscheidungen während des Setups -->
```

## Phase 0 – Vorprüfung (2 Minuten)

Ohne Rückfrage prüfen und das Ergebnis in einer kurzen Liste zeigen:

| Prüfung | Wie | Wenn es fehlt |
|---|---|---|
| Impeccable installiert | Steht ein Skill `impeccable` in deiner Liste verfügbarer Skills (auch als Plugin, z. B. `impeccable:impeccable`)? Sonst nachsehen: `.claude/skills/impeccable/`, `~/.claude/skills/impeccable/`, `~/.claude/plugins/` (Ordner mit `impeccable`). | Installationsweg aus `README.md`, Abschnitt „Impeccable installieren", zeigen. Phasen 1–3 gehen trotzdem, **vor Phase 4 stoppen**, bis Impeccable da ist. |
| Git | `git --version` | Hinweis zur Installation (macOS: `xcode-select --install`). Nicht blockierend, nur Phase 8 braucht es. |
| Python 3 | `python3 --version` | Hinweis zur Installation. Vor Phase 7 nötig. |
| Umgebung | Gibt es eine Shell? | In Cowork ohne Shell: Prüfungen 2–3 überspringen, Dashboard in Phase 7 nur als Vorlage vorbereiten und sagen, dass der Build in Claude Code läuft. |

Impeccable wird nicht von Claude installiert. Den Weg zeigen, die Person installiert selbst und sagt Bescheid. In Claude Code ist das der einfachste Weg:
1. `/plugin marketplace add pbakaus/impeccable` im Chat eingeben und abschicken.
2. `/plugin` eingeben, **Discover** wählen, **Impeccable** installieren.
3. Claude Code neu starten, dann `/setup` eingeben. Das Setup macht an der gespeicherten Stelle weiter.

Vorher den Stand in `Logs/setup-status.md` speichern, damit der Neustart nichts verliert. `/impeccable init` und `/impeccable hooks on` aus der Impeccable-Anleitung sind nicht nötig, `PRODUCT.md` und `DESIGN.md` legt das Setup selbst an. In Cowork gibt es keinen `/plugin`-Befehl: dort Brand Design und Dashboard auf eine Sitzung in Claude Code verschieben.

## Phase 1 – Business und Stand (10 Minuten)

Fragen: `references/fragen.md`, Abschnitt „Phase 1".
Dateien: `Business/business-profil.md`, `Business/ziele.md`.

Direkt nachdem Name und Business-Name feststehen, die Platzhalter `{{NAME}}` (Vorname), `{{BUSINESS_NAME}}` und `{{BUSINESS_KURZ}}` (z. B. „ihr Coaching-Business für Teamleitungen") in `CLAUDE.md` ersetzen. Nur in `CLAUDE.md`, die Skills enthalten keine Platzhalter.
- **Vorher ankündigen:** „Ich trage jetzt deinen Namen in die Grundregeln ein. Claude Code fragt dabei einmal nach, ob ich die Datei `CLAUDE.md` ändern darf. Das ist ein Schutz, damit niemand unbemerkt die Regeln ändert. Klick bitte auf ‚Ja' bzw. ‚Allow'."
- Alle drei Platzhalter in **einem** Bearbeitungsschritt ersetzen, damit nur ein Fenster kommt.
- Wird die Freigabe abgelehnt: nicht erneut versuchen, notieren und in Phase 8 noch einmal anbieten. Alles andere läuft weiter.
- `{{BEKANNTE_DIENSTE}}` erst in Phase 6 füllen (wieder mit Vorwarnung).

Ziele: Jahresziel immer messbar machen (Zahl plus Datum). Bei „mehr Kunden" nachfragen: wie viele, bis wann, woran gemessen. Ist ein Umsatzziel genannt, zurückrechnen, wie viele Aufträge das mit den Preisen aus Phase 2 bedeutet. Diese Rechnung erst in Phase 2 machen und dann in `ziele.md` ergänzen.

## Phase 2 – Produkte und Leistungen (10–15 Minuten)

Fragen: `references/fragen.md`, Abschnitt „Phase 2". Datei: `Business/angebote.md`.

Zuerst das Preismodell klären, danach die passenden Nachfragen stellen:
- **Feste Pakete** → je Paket: Name, Inhalt, Preis, für wen, was am häufigsten gebucht wird.
- **Stundensatz / Tagessatz** → je Leistung: Satz, Mindestumfang, typischer Gesamtumfang eines Auftrags, Fahrtkosten.
- **Projektpreis** → wie der Preis entsteht (Grundpreis plus Faktoren), typische Spanne.
- **Mischung** → je Modell die passenden Fragen. Es gibt oft mehrere Leistungen mit unterschiedlichen Modellen, das ist normal.

Danach für alle: Zusatzleistungen, Rabatte und Aktionen, Anzahlung und Zahlungsweise, was ausdrücklich nicht angeboten wird. Am Ende die Rechnung aus Phase 1 machen (Umsatzziel ÷ durchschnittlicher Auftragswert = nötige Aufträge) und in `ziele.md` eintragen.

## Phase 3 – Zielkunden (10–15 Minuten)

Fragen: `references/fragen.md`, Abschnitt „Phase 3". Datei: `Business/zielgruppen.md`, Positionierungs-Teil in `Business/positionierung.md`.

Hier ist Schärfe das Wichtigste. Erst fragen, ob es ein oder mehrere Segmente gibt (maximal 3). Je Segment eine eigene Fragerunde. Die Probe am Ende: Kann man aus der Beschreibung eine konkrete Person vor sich sehen und weiß, wo man sie trifft? Wenn nicht, an der schwächsten Stelle nachhaken.

Kein Segment ohne „Wer passt ausdrücklich nicht".

## Phase 4 – Brand Design mit Impeccable (15–20 Minuten)

Voraussetzung: Impeccable ist installiert (Phase 0). Sonst hier anhalten, Status notieren und den Installationsweg zeigen.

1. **Material sammeln.** In einer Nachricht um alles bitten, was die Marke gut zeigt:
   - Website-URL und/oder Screenshots der Website (Startseite, eine Unterseite)
   - Karussells, Posts, Stories, Flyer, Präsentationen, die schon gemacht wurden und gut gefallen
   - Logo als Datei (SVG oder PNG), falls vorhanden
   - Farben und Schriften, falls bekannt
   - Optional: 1–3 Marken, deren Look gefällt, und eine, die gar nicht passt
   Alles in `Business/marke/referenzen/` ablegen (Dateinamen nach Regel), das Logo als `Business/marke/logo.svg` bzw. `logo.png`.
2. **Logo klären.** Gibt es kein Logo: fragen, wie der Name als Wortmarke geschrieben werden soll (Schreibweise, Groß/Klein, mit oder ohne Zusatz wie „Coaching"). Das ist dann das Logo für Dashboard und Website.
3. **Mit Impeccable auswerten.** Den Skill Impeccable laden. Die Marke gibt es schon, auch wenn sie nur aus Instagram-Farben und drei Adjektiven besteht. Deshalb gilt:
   - Zuerst `PRODUCT.md` im Hauptordner aus `Business/` zusammenfassen (Impeccable liest sie, sie ist im Hauptordner erlaubt). Nichts Neues hinzufügen.
   - Dann `DESIGN.md` mit Impeccable aus dem Material erfassen (`extract` bei Website oder Screenshots, `document` bei Beschreibungen). Genannte Farben, Wirkung und Tabus sind **feste Vorgaben** („The brief wins").
   - **Keine Welten-Auswahl öffnen.** Impeccable bietet bei neuen Oberflächen eine Auswahlseite mit Design-Welten an. Die passt nicht zu einer bestehenden Marke und verwirrt Einsteiger:innen. Nur wenn die Person ausdrücklich gar keine Vorstellung hat und Vorschläge sehen will, 2–3 Richtungen in Worten beschreiben und wählen lassen.
   Ergebnis: `DESIGN.md` im Hauptordner mit Farben, Schriften, Abständen, Bildsprache, Formensprache, Dos und Don'ts.
4. **Gemeinsam schärfen.** Das Ergebnis in Worten zusammenfassen (5–8 Zeilen) und fragen: Was stimmt, was fehlt, was soll sich ändern? Höchstens zwei Runden. Wenn die Referenzen widersprüchlich sind (z. B. Website alt, Instagram neu), fragen, welche Richtung gilt.
5. **Markendokument.** `Business/marke.md` füllen: Markenkern in einem Satz, Werte, Wirkung (3 Adjektive), Logo und Wortmarke, Verweis auf `DESIGN.md`, Liste der Sprachstile (kommt in Phase 5).

## Phase 5 – Sprachstile (10–20 Minuten)

Fragen: `references/fragen.md`, Abschnitt „Phase 5". Vorgehen je Stil: `references/sprachstil.md`.

1. Fragen, welche Stile es braucht. Vorschläge zum Ankreuzen: Website Deutsch, Website Englisch, Instagram, LinkedIn, Mails an Kund:innen, Newsletter, Angebote. Ein eigener Stil lohnt sich nur, wenn der Ton wirklich anders ist (andere Sprache, andere Zielgruppe, deutlich anderer Kanal). Sonst zusammenlegen und das kurz begründen.
2. Je Stil 3–5 echte Beispieltexte holen (einfügen, als Datei oder Website-URL). Gibt es für einen Stil noch keine Texte (z. B. Englisch), den nächstverwandten Stil als Basis nehmen und das im Skill vermerken.
3. Je Stil eine Datei `Business/sprachstile/<kanal>.md` nach `references/sprachstil.md` anlegen, inklusive Probetext-Test. Kein eigener Skill: Der fertige Skill `sprachstil` lädt die Dateien.
4. Liste der Stile in `Business/marke.md` eintragen, mit Einsatzzweck je Stil.

## Phase 6 – Systeme anbinden (5 Minuten)

Fragen: `references/fragen.md`, Abschnitt „Phase 6". Datei: `Dashboard/README.md`, Tabelle „Datenquellen".

Hier wird **nur abgefragt und notiert**, nichts verbunden. Klar sagen: „Das bauen wir Schritt für Schritt aus. Jede angebundene Quelle bekommt später ihren eigenen Reiter im Dashboard."
- Je gewünschtem System eine Zeile mit Status `gewünscht`.
- `{{BEKANNTE_DIENSTE}}` in `CLAUDE.md` mit den genannten Diensten plus Website-Domain füllen.
- Möchte die Person sofort etwas anbinden: als eigene Aufgabe in `Aufgaben.md` unter „Als Nächstes" eintragen, nicht im Setup erledigen.

## Phase 7 – Dashboard Stufe 1 (15 Minuten)

Vorgehen und Aufbau: `references/dashboard.md`. Voraussetzung: Python 3, Impeccable, `DESIGN.md` aus Phase 4.

1. `Dashboard/einstellungen.json` füllen (Name, Wortmarke, Logo-Pfad).
2. `python3 Dashboard/build.py` einmal laufen lassen, damit die Seite mit dem neutralen Grunddesign steht und alle Inhalte richtig ankommen.
3. Mit Impeccable `Dashboard/vorlage.html` an `DESIGN.md` anpassen. Das ist eine Überarbeitung einer bestehenden Seite, kein neues Design: keine Welten-Auswahl, kein Neuaufbau. Aufbau bleibt: Menüleiste links, Logo oben links, Reiter „Übersicht" und „Wissen". Geändert werden nur Gestaltung und Tokens, nicht die Platzhalter `{{…}}` und nicht die `data-`Attribute, die `build.py` füllt.
4. Neu bauen, ansehen (Screenshot im Browser oder per Impeccable), dann **`impeccable polish`** auf `Dashboard/vorlage.html`, neu bauen, nochmal ansehen.
5. `Dashboard/dashboard.html` öffnen (`open Dashboard/dashboard.html`) und fragen, ob es gefällt. Änderungswünsche wieder mit Impeccable umsetzen, danach immer `polish`.

## Phase 8 – Abschluss (5 Minuten)

1. Mit Shell und Git: `git init` (falls noch kein Repo), erster Commit „System eingerichtet". Hinweis: ein **privates** Repo auf GitHub als Backup anlegen, nie öffentlich, denn hier liegen Business-Daten. Pushen nur nach Rückfrage.
2. Alle `OFFEN:`-Punkte aus `Business/` sammeln und als eine Aufgabe in `Aufgaben.md` unter „Als Nächstes" eintragen.
3. Prüfen, dass in `CLAUDE.md` keine `{{…}}`-Platzhalter mehr stehen. Wurde die Freigabe in Phase 1 abgelehnt, jetzt noch einmal mit Vorwarnung anbieten.
4. Die erste Aufgabe gemeinsam festlegen und unter „Aktiv" eintragen.
5. `/start` einmal ausführen, damit das erste Tageslog entsteht. Die Zeile `- HH:MM – Setup abgeschlossen → Business/, DESIGN.md, Dashboard/` in den Verlauf schreiben.
6. Zum Schluss in 5–8 Zeilen zeigen, was jetzt im System liegt, und die drei Befehle für den Alltag nennen: `/start`, `/feierabend`, `/merken`.
7. `Logs/setup-status.md` auf erledigt setzen. Die Datei bleibt liegen, damit ein späteres `/setup` nur Lücken nachholt.

## Erneuter Aufruf nach abgeschlossenem Setup

Alle Phasen erledigt → nicht neu starten. Stattdessen anbieten:
- offene `OFFEN:`-Punkte abarbeiten,
- einen weiteren Sprachstil anlegen (Phase 5),
- eine Phase gezielt neu machen (z. B. Brand Design nach einem Rebranding).
