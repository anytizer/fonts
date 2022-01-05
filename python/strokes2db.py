# From strokes files into strokes database
from bs4 import BeautifulSoup as soup

import glob
import os
import uuid

from _configs import file_get_contents
from _sqlite import conn


groups = [
    "basics",
    "vowels",
    "letters",
    "maatraa",
    "numerals",
    "ligatures",
    "symbols",
]


def xmlUx0021SVGPathData(bs: soup):
    _svg = ""
    nodes = bs.find_all("collection")
    for node in nodes:
        if node.attrs.get("unicode", "") == "U+21":
            paths = node.find_all("path")
            path_svgs = []
            for path in paths:
                path_svgs.append(path.attrs.get("data", ""))
            _svg = ";".join(path_svgs)

    return _svg


if __name__ == "__main__":
        stroke_data = []
        for group in groups:
            for file in glob.glob("../strokes-devanagari/{0}/*.birdfont".format(group)):
                birdfont_xml = file_get_contents(file)
                bs = soup(birdfont_xml, "lxml")

                pk = str(uuid.uuid4()).upper()
                # group = group
                name = os.path.splitext(os.path.basename(file))[0]
                description = file_get_contents(f"_desc/{group}/{name}.txt")
                svg = xmlUx0021SVGPathData(bs)

                stroke_data.append((pk, group, name, description, svg))

        curr = conn.cursor()
        curr.execute("DELETE FROM tw_strokes;")
        sql = "INSERT INTO tw_strokes (stroke_id, stroke_group, stroke_name, stroke_description, stroke_svg) VALUES (?, ?, ?, ?, ?);"
        curr.executemany(sql, stroke_data)

        conn.commit()
        conn.close()
