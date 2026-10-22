# KI-Betriebssystem für Selbstständige

Ein Ordner, der dein Business kennt. Du arbeitest darin mit Claude (Claude Code oder Claude Cowork), und statt in jedem Chat bei Null anzufangen, weiß Claude, was du anbietest, für wen, zu welchen Preisen, wie deine Marke aussieht und wie du klingst. Jeden Tag ein bisschen mehr.

Die Vorlage ist leer. Beim ersten Start richtet `/setup` sie mit dir ein.

## Was du bekommst

- **Eine feste Ordnerstruktur** mit klaren Regeln, was wohin gehört: Business, Projekte, Content, Kunden, Website, Dashboard, Gedächtnis, Tageslogs.
- **Einen Tagesrhythmus:** `/start` am Morgen, `/feierabend` am Abend, `/wochenrueckblick` und `/monatsrueckblick`. Höchstens 3 aktive Aufgaben, damit der Fokus bleibt.
- **Ein Gedächtnis:** Mit „Merk dir das" landet Wissen dauerhaft im System.
- **Deine Marke im System:** Aus deiner Website und deinen bisherigen Posts entsteht mit Impeccable ein Design-System. Pro Kanal gibt es einen eigenen Sprachstil, damit Texte nach dir klingen.
- **Ein eigenes Dashboard** in deinem Design: Aufgaben, Ziele, offene Punkte, dein Wissen über Zielgruppen und Angebote. Weitere Systeme (Kalender, Anzeigen, Website-Statistik) bindest du nach und nach an.
- **Einen sicheren Rahmen:** Claude liest keine Passwortdateien, fragt vor allem, was nach außen geht, und löscht nichts ungefragt.

## Voraussetzungen

| Was | Wofür | Wo |
|---|---|---|
| Claude Code oder Claude Cowork | Damit arbeitest du im Ordner | [claude.com](https://claude.com) |
| Impeccable (Skill) | Brand Design, Dashboard, Website | [impeccable.style/docs](https://impeccable.style/docs/), Quelle: [github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| Python 3 | Dashboard bauen | auf dem Mac meist vorhanden, sonst [python.org](https://www.python.org) |
| Git | Versionen und Backup | macOS: `xcode-select --install` |
| Node.js (nur für eine eigene Website) | Astro | [nodejs.org](https://nodejs.org) |

Installiere Impeccable nach der Anleitung in der Impeccable-Dokumentation, bevor du `/setup` startest. Wenn dir das zu technisch ist, lass dir einmal von jemandem helfen, es dauert wenige Minuten. Das Setup prüft das und macht ohne Impeccable zuerst alles andere, nur Brand Design und Dashboard warten.

## So startest du

1. Oben auf **„Use this template"** klicken (eigenes, **privates** Repo) oder das ZIP herunterladen und entpacken.
2. Den Ordner in Claude Code öffnen (oder in Cowork als Arbeitsordner wählen).
3. `/setup` eingeben oder „Setup starten" sagen.

Das Setup dauert 60 bis 90 Minuten und läuft in 8 Etappen. Du kannst jederzeit Pause machen, beim nächsten `/setup` geht es an derselben Stelle weiter.

Einmal am Anfang fragt Claude Code in einem kleinen Fenster, ob es die Datei `CLAUDE.md` ändern darf. Dort wird dein Name eingetragen. Klick auf „Erlauben". Das Fenster ist ein Schutz, damit niemand unbemerkt die Regeln ändert.

| Etappe | Was passiert |
|---|---|
| 0 Vorprüfung | Impeccable, Python, Git da? |
| 1 Business und Stand | Was du machst, wo du stehst, dein Jahresziel (z. B. Umsatz) |
| 2 Produkte und Leistungen | Pakete, Stunden- oder Tagessätze, Ablauf, Extras |
| 3 Zielkunden | Für wen genau, Auslöser, Einwände, wo du sie erreichst, wer nicht passt |
| 4 Brand Design | Website, Screenshots, Karussells und Posts teilen, Impeccable leitet dein Design-System ab, Logo oder Wortmarke |
| 5 Sprachstile | Welche Kanäle (Website DE/EN, Instagram, LinkedIn, Mails …), je Kanal ein eigener Stil aus deinen Texten, abgelegt in `Business/sprachstile/` |
| 6 Systeme | Welche Tools du später anbinden willst |
| 7 Dashboard | Erstes Dashboard in deiner Marke, Menü links, Logo oben links, Reiter Übersicht und Wissen |
| 8 Abschluss | Git, offene Punkte, erste Aufgabe, erster `/start` |

## Befehle im Alltag

| Befehl | Was er tut |
|---|---|
| `/start` | Tageslog anlegen, Aufgaben zeigen, Fokus festlegen |
| `/feierabend` | Tag dokumentieren, Aufgaben aufräumen |
| `/wochenrueckblick` | Woche auswerten, Fokus für die nächste |
| `/monatsrueckblick` | Monat auswerten, Ziele aktualisieren |
| `/merken` | Wissen dauerhaft speichern |
| `/sprachstil` | Texte in deinem Ton schreiben, neuen Stil anlegen |
| `/neues-projekt` | Projekt mit Ziel und Frist anlegen |
| `/neuer-ordner` | Neuen Bereich mit Regel anlegen |
| `/dashboard` | Dashboard neu bauen und öffnen |
| `/website` | Website mit Astro bauen: erst eine Template Library, dann Seiten, mit sicherem Deploy-Weg |

Alle Befehle funktionieren auch als normaler Satz („Guten Morgen", „Feierabend", „Merk dir das").

## Ordner

```
CLAUDE.md        Die Spielregeln für Claude (wird im Setup personalisiert)
Aufgaben.md      Deine Aufgaben, max. 3 aktiv
DESIGN.md        Dein Design-System (entsteht im Setup)
Business/        Profil, Ziele, Angebote, Zielgruppen, Positionierung, Marke, Kundenstimmen
Projects/        Vorhaben mit Anfang und Ende
Content/         Posts, Newsletter, Anzeigentexte, Redaktionsplan
Kunden/          Vorlagen, anonymes Anfragen-Log
Website/         Website-Inhalte, Code in Website/site/
Dashboard/       Dein Dashboard
Memory/          Gemerktes Wissen
Logs/            Tageslogs und Rückblicke
.claude/         Skills und Sicherheitseinstellungen
```

## Wichtig zum Datenschutz

- Nach dem Setup liegen hier Business-Daten. Dein Repo muss **privat** sein.
- Verträge, Kundendaten und Dashboard-Rohdaten sind in `.gitignore` ausgeschlossen und bleiben auf deinem Rechner.
- Passwörter und API-Schlüssel gehören nie in diesen Ordner, sondern in den Schlüsselbund oder in Umgebungsvariablen.
- Die Regeln in `CLAUDE.md` sind Anweisungen. Technisch abgesichert wird über `.claude/settings.json`, das gilt in Claude Code. In Cowork gelten nur die Regeln.

## Lizenz

CC BY-NC-SA 4.0, siehe `LICENSE`. Nutzen und anpassen für dein eigenes Business ist frei. Weiterverkaufen oder als eigenes Produkt anbieten ist nicht erlaubt.
