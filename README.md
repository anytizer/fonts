# fonts (work in progress)

Collection of tools and python scripts to produce Devanagari/Nepali font.
There are repeated strokes in Devanagari/Nepali, like: vertical stem (danda), horizontal line (dikaa, Sanskirt: Shiro Rekha) etc.
This project identifies unique strokes used so far in a Nepali subset of Devanagari.
You need to understand basic Nepali writing to understand this project.

This is a proof of concept work where:
* [ ] 2 or more caligraphers can design the different characters of a font at the same time.
* [ ] Nepali font with a list of database driven strokes per character.
* [ ] Fixing font made easy.

There are several hundreds of ligatures possible and designing each character set for them is practically impossible. This project aims to create Nepali fonts with less than 100 basic stokes.

## Old projects:
Fonts developed by tracing various images. The images traced were probably found in public domain.

* mousewriting - just learning how to make fonts
* dance - dancers' sillhoute
* fruits - pictures of common fruits

Some glyphs are just referenced (Poppins at Google Fonts), and may appear here for educational purpose.

# Reference Letter 5
![image](https://user-images.githubusercontent.com/5563341/148050202-caa38abf-4581-4dc1-8d69-c7b853ebec88.png)

This is a base letter to showcase design, slim lines, knots, tails etc.

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
