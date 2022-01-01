# fonts
Fonts developed by tracing various images that are probably found in public domain.
* mousewriting - just learning how to make fonts
* dance - dancers
* fruits - pictures of common fruits

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
* [ ] Build character database as combination of strokes in [SQLite](tools/strokes-list.md).
* [ ] From birdfont xml, extract glyhps svg.
* [ ] Edit the strokes for position, decoration, widths, sizes and styles.
* [ ] Rebuilld Birdfont XML.
* [ ] Tests for fitness of individual glyphs.
* [ ] Re-Edit strokes.
* [ ] Export the font.
* [ ] Test the font using web/css.
