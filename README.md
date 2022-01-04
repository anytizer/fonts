# fonts
Fonts developed by tracing various images that are probably found in public domain.
* mousewriting - just learning how to make fonts
* dance - dancers' sillhoute
* fruits - pictures of common fruits
* devanagari - Devanagari font (to be renamed, built and released)
  * Some glyphs are just collected, and appear here for educational purpose.

![image](https://user-images.githubusercontent.com/5563341/148050202-caa38abf-4581-4dc1-8d69-c7b853ebec88.png)

## Made with
* Fonts traced and exported using [BirdFont](https://birdfont.org/#release) Plus version (`*.ttf` files)
* Logos made using AAA-Logo (`*.al4` files)

## ToDo
* Build devanagari - Unicode based characters with hundreds of [ligatures](tools/ligatures.py)
* Python scripts - edited with PyCharm, and Thonny under [Python 3.10.1](https://www.python.org/downloads/)
* Glyph strokes - under study
* Ligatures - under study

## Font Build Process in this project
* [ ] Build a list of strokes used in as used in Devanagari Nepali.
* [ ] Build character database as combination of strokes in [SQLite](tools/strokes-database.md).
* [ ] From birdfont xml, extract glyhps svg.
* [ ] Edit the strokes for position, decoration, widths, sizes and styles.
* [ ] Rebuilld Birdfont XML.
* [ ] Tests for fitness of individual glyphs.
* [ ] Re-Edit strokes.
* [ ] Export the font.
* [ ] Test the font using web/css.

## Disclaimer
Stroke names are used for comfort only.
They differ as that from Sanskrit and other languages.

## Help wanted
A linguist may suggest a correct way of calligraphy in this font set, and stroke names; so that I can adjust the database.
