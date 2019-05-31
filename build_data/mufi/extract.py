import glob
import os.path
import bs4

here = os.path.dirname(__file__)
with open(os.path.join(here, "../codes.py"), "w") as f:
    f.write("MUFI = {\n")
    for file in glob.glob(os.path.join(
        here, "*.html"
    )):
        with open(file) as r:
            doc = bs4.BeautifulSoup(r.read(), features="html.parser")
            for tr in doc.select("tbody tr"):
                _, transc, desc, code = tuple(tr.select("td"))
                transc, desc, code = transc.text.strip(), desc.text.strip(), code.text.strip()
                code = int(code, 16)
                section, position = code >> 8, code % 256
                f.write("    ({section}, {position}): '{transc}',  # {desc}\n".format(
                    section=section, position=position, desc=desc, transc=transc
                ))
    f.write("}")
