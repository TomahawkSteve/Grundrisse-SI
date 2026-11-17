# Grundrisse-SI – Schröder Grundriss-Studio

Web-App für Schröder Immobilien: Grundriss abfotografieren, ausrichten, beschriften, möblieren und als PDF/JPG (A4, 300 dpi) exportieren oder per E-Mail teilen.

## Nutzung
1. **Objekt**: Objekt-Nr., Anschrift, Etage, möbliert ja/nein, Designvorlage (Klassik, Eiche, Marine), E-Mail-Empfänger.
2. **Foto**: Plan fotografieren, Ecken auf das Papier ziehen, Linien bereinigen.
3. **Beschriften**: Räume setzen (Böden färben sich automatisch), Möbel platzieren, alte Beschriftungen wegradieren, Maßstab festlegen.
4. **Export**: PDF/JPG speichern oder per E-Mail senden (auf dem Handy direkt als Anhang über das Teilen-Menü).

## Technik
- `src/app.html` ist die Quelle. `python3 build.py` erzeugt daraus `index.html` für GitHub Pages.
- Alles läuft im Browser, keine Daten verlassen das Gerät.
