@echo off

python strokes2db.py
python write_glyphs.py > _glyphs.py
python write_strokes.py > _strokes.py
python write_letters.py > _letters.py

python compose_merged.py > merged.birdfont
