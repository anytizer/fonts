# fonts

Collection of tools and python scripts to produce Devanagari Fonts.
There are repeated strokes in Devanagari, like, vertical stem, horizontal like etc.
This project identifies unique strokes used so far a Nepali subset from Devanagari.

This is a proof of concept work where:
* [] 2 or more developers can design the different characters of a font at the same time.
* [] Nepali font with a list of database driven strokes per character.
* [] Fixing font made easy.

Fonts developed by tracing various images. The images traced were probably found in public domain.

* mousewriting - just learning how to make fonts
* dance - dancers' sillhoute
* fruits - pictures of common fruits

## Under development:
* devanagari - to be renamed, built and released

Some glyphs are just referenced (Poppins at Google Fonts), and may appear here for educational purpose.

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
* [ ] Build a list of basic strokes as used in Devanagari Nepali.
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
A linguist may suggest a correct way of calligraphy in this font set, and stroke names; so that I can adjust the database of SVGs.
