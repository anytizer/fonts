# python write_letters.py > _letters.py

from _sqlite import conn


def s_dot(csv=";"):
    strokes = ", ".join(["s." + stroke.strip() for stroke in csv.split(",")])
    return strokes


sql = """
select
    letter_name name,
    letter_variable variable,
    letter_strokes strokes
from tw_letters
where letter_strokes != ''
order by variable, letter_name
;"""
curr = conn.cursor()
rs = curr.execute(sql, ())


print("from _strokes import strokes")
print()
print("s = strokes()")
print()
print("class letters:")
for letter in rs:
    print("    {0:10} = [{1}]".format(letter["variable"], s_dot(letter["strokes"])))
