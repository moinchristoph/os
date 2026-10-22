#!/usr/bin/env python3
"""Baut Dashboard/dashboard.html aus den Markdown-Dateien des Systems.

Liest Aufgaben.md, Business/*.md und das jüngste Tageslog, füllt damit
Dashboard/vorlage.html und schreibt Dashboard/dashboard.html.
Nur Standardbibliothek, keine Abhängigkeiten.
"""

import base64
import html
import json
import re
import sys
from datetime import datetime
from pathlib import Path

DASHBOARD = Path(__file__).resolve().parent
ROOT = DASHBOARD.parent
BUSINESS = ROOT / "Business"

WISSEN = [
    ("zielgruppen", "Zielgruppen", "zielgruppen.md"),
    ("angebote", "Produkte und Preise", "angebote.md"),
    ("positionierung", "Positionierung", "positionierung.md"),
    ("marke", "Marke", "marke.md"),
]


def lesen(pfad: Path) -> str:
    if not pfad.exists():
        return ""
    return pfad.read_text(encoding="utf-8")


def inline(text: str) -> str:
    text = html.escape(text, quote=False)
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    text = re.sub(r"OFFEN:", r'<mark class="offen">OFFEN:</mark>', text)
    return text


def tabelle(zeilen: list[str]) -> str:
    def zellen(zeile: str) -> list[str]:
        return [z.strip() for z in zeile.strip().strip("|").split("|")]

    kopf = zellen(zeilen[0])
    rumpf = [zellen(z) for z in zeilen[2:]]
    out = ['<div class="tabelle"><table><thead><tr>']
    out += [f"<th>{inline(z)}</th>" for z in kopf]
    out.append("</tr></thead><tbody>")
    for reihe in rumpf:
        out.append("<tr>" + "".join(f"<td>{inline(z)}</td>" for z in reihe) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def markdown(text: str, ebene_versatz: int = 1) -> str:
    """Kleiner Markdown-Umsetzer für die Kerndokumente: Überschriften,
    Listen, Checkboxen, Tabellen, Zitate, Absätze."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    zeilen = text.splitlines()
    out: list[str] = []
    absatz: list[str] = []
    liste: str | None = None
    i = 0

    def absatz_schliessen():
        if absatz:
            out.append(f"<p>{inline(' '.join(absatz))}</p>")
            absatz.clear()

    def liste_schliessen():
        nonlocal liste
        if liste:
            out.append(f"</{liste}>")
            liste = None

    while i < len(zeilen):
        zeile = zeilen[i].rstrip()
        roh = zeile.strip()

        if not roh:
            absatz_schliessen()
            liste_schliessen()
        elif roh.startswith("|") and i + 1 < len(zeilen) and re.match(r"^\s*\|[\s:|-]+\|\s*$", zeilen[i + 1]):
            absatz_schliessen()
            liste_schliessen()
            block = []
            while i < len(zeilen) and zeilen[i].strip().startswith("|"):
                block.append(zeilen[i])
                i += 1
            out.append(tabelle(block))
            continue
        elif m := re.match(r"^(#{1,6})\s+(.*)$", roh):
            absatz_schliessen()
            liste_schliessen()
            stufe = min(len(m.group(1)) + ebene_versatz, 6)
            out.append(f"<h{stufe}>{inline(m.group(2))}</h{stufe}>")
        elif m := re.match(r"^[-*]\s+\[( |x|X)\]\s+(.*)$", roh):
            absatz_schliessen()
            if liste != "ul":
                liste_schliessen()
                out.append('<ul class="check">')
                liste = "ul"
            erledigt = " erledigt" if m.group(1) != " " else ""
            out.append(f'<li class="aufgabe{erledigt}">{inline(m.group(2))}</li>')
        elif m := re.match(r"^[-*]\s+(.*)$", roh):
            absatz_schliessen()
            if liste != "ul":
                liste_schliessen()
                out.append("<ul>")
                liste = "ul"
            out.append(f"<li>{inline(m.group(1))}</li>")
        elif m := re.match(r"^\d+\.\s+(.*)$", roh):
            absatz_schliessen()
            if liste != "ol":
                liste_schliessen()
                out.append("<ol>")
                liste = "ol"
            out.append(f"<li>{inline(m.group(1))}</li>")
        elif roh.startswith(">"):
            absatz_schliessen()
            liste_schliessen()
            out.append(f"<blockquote>{inline(roh.lstrip('> '))}</blockquote>")
        elif roh.startswith("Zuletzt aktualisiert:"):
            absatz_schliessen()
            out.append(f'<p class="stand">{inline(roh)}</p>')
        else:
            liste_schliessen()
            absatz.append(roh)
        i += 1

    absatz_schliessen()
    liste_schliessen()
    return "\n".join(out)


def abschnitt(text: str, titel: str) -> str:
    """Inhalt unter einer ##-Überschrift, die mit `titel` beginnt."""
    m = re.search(rf"^##\s+{re.escape(titel)}.*?$(.*?)(?=^##\s|\Z)", text, flags=re.M | re.S)
    return m.group(1).strip() if m else ""


def ohne_titel(text: str) -> str:
    return re.sub(r"^#\s+.*\n", "", text, count=1)


def logo_html(einstellungen: dict) -> str:
    wortmarke = html.escape(einstellungen.get("wortmarke") or einstellungen.get("name") or "Dashboard")
    pfad = einstellungen.get("logo") or ""
    if not pfad:
        return f'<span class="wortmarke">{wortmarke}</span>'
    datei = ROOT / pfad
    if not datei.exists():
        print(f"Hinweis: Logo {pfad} nicht gefunden, nehme die Wortmarke.", file=sys.stderr)
        return f'<span class="wortmarke">{wortmarke}</span>'
    typ = {".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}.get(datei.suffix.lower())
    if not typ:
        print(f"Hinweis: Logoformat {datei.suffix} wird nicht unterstützt, nehme die Wortmarke.", file=sys.stderr)
        return f'<span class="wortmarke">{wortmarke}</span>'
    daten = base64.b64encode(datei.read_bytes()).decode("ascii")
    return f'<img class="logo" src="data:{typ};base64,{daten}" alt="{wortmarke}">'


def offene_punkte(sichtbar: int = 8) -> str:
    punkte = []
    for datei in sorted(BUSINESS.glob("*.md")):
        for zeile in lesen(datei).splitlines():
            if "OFFEN:" in zeile:
                frage = zeile.split("OFFEN:", 1)[1].strip(" |") or "(ohne Beschreibung)"
                punkte.append(f'<li><span class="quelle">{html.escape(datei.stem)}</span> {inline(frage)}</li>')
    if not punkte:
        return '<p class="leer">Keine offenen Punkte in Business/.</p>'
    rest = len(punkte) - sichtbar
    mehr = f'<li class="mehr">und {rest} weitere in Business/</li>' if rest > 0 else ""
    return f'<p class="zahl">{len(punkte)}</p><ul class="offen-liste">' + "".join(punkte[:sichtbar]) + mehr + "</ul>"


def letzter_verlauf(anzahl: int = 6) -> str:
    logs = sorted((ROOT / "Logs").glob("*/[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9].md"))
    if not logs:
        return '<p class="leer">Noch kein Tageslog. Starte mit /start.</p>'
    verlauf = abschnitt(lesen(logs[-1]), "Verlauf")
    eintraege = [z for z in verlauf.splitlines() if z.strip().startswith("- ")]
    if not eintraege:
        return f'<p class="leer">Im Log vom {logs[-1].stem} steht noch nichts im Verlauf.</p>'
    return f'<p class="stand">Log vom {logs[-1].stem}</p>' + markdown("\n".join(eintraege[-anzahl:]))


def main() -> int:
    vorlage_pfad = DASHBOARD / "vorlage.html"
    if not vorlage_pfad.exists():
        print("Fehler: Dashboard/vorlage.html fehlt.", file=sys.stderr)
        return 1
    try:
        einstellungen = json.loads(lesen(DASHBOARD / "einstellungen.json") or "{}")
    except json.JSONDecodeError as fehler:
        print(f"Fehler: Dashboard/einstellungen.json ist kein gültiges JSON ({fehler}).", file=sys.stderr)
        return 1

    aufgaben = lesen(ROOT / "Aufgaben.md")
    ziele = lesen(BUSINESS / "ziele.md")
    aktiv = abschnitt(aufgaben, "Aktiv")

    werte = {
        "TITEL": html.escape(einstellungen.get("name") or "Dashboard"),
        "LOGO": logo_html(einstellungen),
        "STAND": datetime.now().strftime("%d.%m.%Y, %H:%M"),
        "AKTIV": markdown(aktiv) if aktiv else '<p class="leer">Keine aktiven Aufgaben.</p>',
        "ZIELE": markdown(abschnitt(ziele, "Jahresziele")) or '<p class="leer">Noch keine Jahresziele in Business/ziele.md.</p>',
        "OFFEN": offene_punkte(),
        "VERLAUF": letzter_verlauf(),
    }
    for schluessel, titel, datei in WISSEN:
        inhalt = lesen(BUSINESS / datei)
        werte[f"WISSEN_{schluessel.upper()}"] = markdown(ohne_titel(inhalt)) if inhalt else f'<p class="leer">Business/{datei} fehlt noch.</p>'

    seite = lesen(vorlage_pfad)
    for schluessel, wert in werte.items():
        seite = seite.replace("{{" + schluessel + "}}", wert)
    rest = sorted(set(re.findall(r"\{\{([A-Z_]+)\}\}", seite)))
    if rest:
        print(f"Hinweis: unbekannte Platzhalter in vorlage.html: {', '.join(rest)}", file=sys.stderr)

    ziel = DASHBOARD / "dashboard.html"
    ziel.write_text(seite, encoding="utf-8")
    print(f"Dashboard gebaut: {ziel.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
