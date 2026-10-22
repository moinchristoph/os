---
name: website
governance: gelb
description: Baut oder erweitert die Website von {{NAME}} nach festem Weg – Astro als Framework, zuerst eine Template Library aus Sektionen mit Design-Tokens aus DESIGN.md, neue Seiten und Designs nur aus der Library, von Anfang an ein Deployment-Pfad mit Freigabe. Gestaltet mit Impeccable, endet immer mit impeccable polish. Deployt nie ohne Freigabe. Auslöser – "/website", "Website bauen", "neue Website", "Landingpage bauen", "neue Seite auf der Website", "Website umbauen".
---

# Website – Astro, Template Library, Deployment-Pfad

Drei Regeln, die immer gelten:

1. **Astro** ist das empfohlene Framework. Statische Seiten, schnell, gute SEO, Inhalte als JSON getrennt vom Design. Möchte {{NAME}} bei einem Baukasten bleiben (Squarespace, Wix, WordPress), das respektieren und dort nur Texte und Struktur liefern.
2. **Erst die Template Library, dann die Seiten.** Keine Seite wird frei gestaltet. Jede Seite ist eine Liste von Sektionen aus der Library, befüllt mit Inhalten aus JSON. Neues Design heißt: neue Sektion oder neue Variante in der Library, dann verwenden.
3. **Der Deployment-Pfad steht, bevor die erste Seite live geht.** Hochgeladen wird nur über `npm run deploy` mit Freigabe.

Gestaltet wird mit Impeccable nach `DESIGN.md`. **Jeder Gestaltungsschritt endet mit `impeccable polish`.**

## Phase A – Klären

Eine Nachricht, nur was fehlt:
- Gibt es schon eine Website? Wo läuft sie (Baukasten, Hosting-Anbieter)? Domain?
- Welche Seiten braucht es zuerst? (Startseite, Angebot, Über mich, Kontakt, Impressum, Datenschutz)
- Wo soll sie laufen? Klassischer Webspace mit SFTP (z. B. Strato, IONOS, all-inkl) oder Plattform (Netlify, Vercel, Cloudflare Pages, GitHub Pages)?

Voraussetzungen prüfen: Node.js (`node --version`, mindestens die aktuelle LTS), Impeccable, `DESIGN.md`.
Neue Pakete (Astro selbst, Integrationen) nur nach Rückfrage installieren: Name, Quelle, Grund nennen.

## Phase B – Gerüst

In `Website/site/` (eigener Ordner, eigenes Git-Repo, im System-Repo per `.gitignore` ausgeschlossen):

```
src/
  styles/tokens.css        die einzigen Werte: Farben, Schriften, Abstände, Radien aus DESIGN.md
  styles/base.css
  layouts/BaseLayout.astro, PageLayout.astro
  components/SectionRenderer.astro   type aus JSON → Komponente
  components/sections/     die Template Library
  data/site.json           Navigation, Footer, Geschäftsdaten, einmal für alle Seiten
  data/<seite>.json        Inhalte je Seite: meta und sections
  pages/
library.astro              Übersichtsseite aller Sektionen mit Beispielinhalten (noindex, nur lokal)
scripts/deploy.sh
```

Regeln für den Code (in `Website/site/CLAUDE.md` festhalten):
- Keine Werte außerhalb von `tokens.css`. Sektionen nutzen nur `var(--token)`.
- Inhalte gehören nach `src/data/*.json`, nie ins Template. Templates kennen keine Texte.
- Kopfzeile und Footer gibt es einmal, gerendert vom Layout, nie in einer Seitendatei.
- Keine neue Sektion ohne die drei Schritte: Komponente in `components/sections/`, Eintrag in `SectionRenderer.astro`, Zeile in der Tabelle in `DESIGN.md`.

## Phase C – Template Library

1. Aus `DESIGN.md` die Tokens schreiben.
2. Die Grundsektionen bauen, **eine nach der anderen**, jede zeigen, bevor die nächste kommt: Hero, Text, Text mit Bild, Leistungen/Pakete, Ablauf in Schritten, Kundenstimmen, FAQ, Call-to-Action, Kontaktformular, Rechtstext. Nur bauen, was die geplanten Seiten brauchen.
3. Jede Sektion erscheint auf `library.astro` mit Beispielinhalt. Das ist der Katalog, aus dem gebaut wird.
4. Nach jeder Sektion: ansehen (Desktop und Handy), dann **`impeccable polish`**, nochmal ansehen.

## Phase D – Seiten aus der Library

1. Je Seite eine JSON-Datei mit den gewählten Sektionen. Texte über den passenden Sprachstil-Skill, Fakten nur aus `Business/`.
2. Eine Seite entsteht Sektion für Sektion, nicht am Stück. Nach jeder Sektion zeigen.
3. Braucht eine Seite etwas, das es in der Library nicht gibt: erst als neue Sektion oder Variante in die Library (Phase C, Schritt 2–4), dann auf die Seite.
4. Rechtstexte (Impressum, Datenschutz) kommen von {{NAME}} oder aus einem Generator. Nie selbst formulieren oder umformulieren.
5. Vor dem Fertigmelden: `npm run check` (falls eingerichtet) und `npm run build`. Fehler fixen, nie wegschalten.

## Phase E – Deployment-Pfad

Einmal einrichten, bevor die erste Seite live geht. Ziel: ein Befehl `npm run deploy`, der nie ungefragt etwas veröffentlicht.

**Klassischer Webspace (SFTP):**
1. `scripts/deploy.sh`: baut, gleicht jede Datei in `dist/` mit dem Server ab (Prüfsumme oder Größe und Datum), listet neu und geändert, **lädt nichts hoch**.
2. Freigabe: Liste mit Nummern zeigen (gern als lokale Freigabeseite mit Vorschau). {{NAME}} wählt aus und gibt den Upload-Befehl mit Auswahl, z. B. `npm run deploy -- --hochladen 1-4,7`.
3. Upload nur der freigegebenen Dateien. **Nie auf dem Server löschen.** Sind mehr als 50 % der Dateien betroffen: stoppen und nachfragen.
4. Zugangsdaten: Server und Nutzer in `deploy/<anbieter>.conf` (nicht versioniert, `.conf.example` versioniert), Passwort nur im Schlüsselbund (macOS: `security add-generic-password`, {{NAME}} legt den Eintrag selbst an). Nie auslesen oder in Dateien schreiben.

**Plattform (Netlify, Vercel, Cloudflare Pages):**
1. Zuerst immer eine Vorschau-Version (Preview-Deploy) mit eigener URL.
2. {{NAME}} prüft die Vorschau und gibt frei.
3. Erst dann die Produktivversion. Token nur als Umgebungsvariable oder im Schlüsselbund.

Für beide Wege:
- `npm run deploy` in `.claude/settings.json` unter `ask` eintragen (Rückfrage, Änderung an Settings vorher bestätigen lassen).
- Einen Skill `deploy` anlegen, der genau diesen Ablauf beschreibt (Prüfen, Abgleich, Freigabe, Upload, Tageslog). Governance `rot`.
- Erster Deploy gemeinsam, Schritt für Schritt.

## Abschluss jeder Website-Sitzung

- Zeile im Tageslog: `- HH:MM – <was> → Website/site/…`
- Offene Punkte in `Website/README.md`, Abschnitt „Offen".
