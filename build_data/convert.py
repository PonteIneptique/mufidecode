import csv
import re
from typing import Tuple, List

letter = "([A-Z]|THORN|ETH)"
print("LATIN SMALL LIGATURE "+letter+" ?"+letter)
steps: List[Tuple[str, str]] = [
    # (Regex Capture, Regex Sub)
    # NOISE
    (" ROTUNDA", ""),
    ("LONG ", ""),
    ("NECKLESS ", ""),
    (" NECKLESS", ""),
    ("DOTLESS ", ""),
    (" DOTLESS", ""),
    # WITH CAPTURE
    ("LATIN SMALL LIGATURE "+letter, "##\g<1>"),  # LOWER
    ("LATIN CAPITAL LIGATURE "+letter, "\g<1>"),  # LOWER
    ("LATIN LETTER SMALL CAPITAL (?:CLOSED |OPEN |DOTLESS )?([A-Z])", "\g<1>"),
    ("LATIN SMALL CAPITAL LETTER (?:CLOSED |OPEN |DOTLESS )?([A-Z])", "\g<1>"),
    ("LATIN (?:SMALL|MEDIUSCULE) LETTER ([A-Z])", "#\g<1>"),  # SHOULD LOWER !
    ("LATIN ENLARGED LETTER (?:SMALL )?(?:DOTLESS )?"+letter, "#\g<1>"),  # SHOULD LOWER !
    ("LATIN ENLARGED LETTER SMALL "+letter, "#\g<1>"),
    ("LATIN CAPITAL LETTER ([A-Z])", "\g<1>"),
    # NOISE
    ("WITH (BAR|SLASH|STEM|(HIGH OVERLINE)|((RIGHT |LEFT )?(MAIN )?(DESCENDER|STROKE))|CURL)", ""),
    ("WITH (ACUTE)", ""),
    ("(UNCIAL|(SEMI-)?CLOSED|EXTENDED BAR|TALL|INSULAR|CAROLINGIAN|GOTHIC) (FORM)?", ""),
    ("(WITH|AND) (DOT|VERTICAL LINE|RING|INVERTED BREVE) (BELOW|ABOVE)", ""),
    ("(WITH|AND) DIAGONAL STROKE", ""),
    ("(WITH|AND) (DOUBLE )?(MEDIUM-)?(HIGH )?(MACRON|ACUTE|BREVE|DIAERESIS|OGONEK|CIRCUMFLEX|CURL|FLOURISH)", ""),
    ("WITH (#?[A-Z]) (BELOW|ABOVE)", "\g<1>"),
    ("WITH ((((LARGE|SMALL) LOWER)|SEPARATE|RIGHT UPPER|LEFT UPPER) )?LOOPS?", ""),
    ("SMALL CAPITAL ", ""),
    ("LIGATURE ", ""),
    (" WITH MEDIUM-HIGH OVERLINE", ""),
    ("^COMBINING ", ""),
    (" THROUGH DESCENDER AND TILDE", ""),
    (" WITH LEG AND STROKE THROUGH DESCENDER", ""),
    (" WITH TWO STROKES", ""),
    ("LIGATED WITH ", ""),
    ("WITH CENTRAL SLANTED STROKE", ""),
    ("WITH SLANTED DESCENDING STROKE", ""),
    ("WITH SHORT SLASH", ""),
    ("WITH TWO SHORT SLASHES (ABOVE|ABOVE) (LEFT|RIGHT)", ""),
    ("WITH SHORT SLASH (ABOVE|BELOW) (LEFT|RIGHT)", ""),
    (" SQUARE FORM", ""),
    ("AND ([A-Z])\s?$", "\g<1>"),
    (" BAR ABOVE", ""),
    ("WITH DIAGONAL DIAERESIS", ""),
    ("DESCENDING", ""),
    ("WITH DOTTED HOOKS", ""),
    ("(ABOVE|BELOW) (LEFT|RIGHT)", ""),
    ("ARM OF ", ""),
    ("WITH TWO SHORT SLASHES ", ""),
    ("LATIN ENLARGED LETTER SMALL ", ""),
    # ABBR
    ("LATIN ABBREVIATION SIGN( )?", ""),
    #PUNCT
    ("SEMICOLON", ";"),
    ("PUNCTUS INTERROGATIVUS", "!"),
    ("PUNCTUS EXCLAMATIVUS", "!"),
    ("PUNCTUS VERSUS", ";"),
    ("PUNCTUS ELEVATUS", ";"),
    ("MODIFIER CAPITAL LETTER ", ""),
    ("LATIN LETTER ", ""),
    ("FINAL ", ""),
    # Macrons
    ("HIGH MACRON WITH FIXED HEIGHT", "_"),
    ("MEDIUM-HIGH MACRON WITH FIXED HEIGHT", "_"),
    ("HIGH OVERLINE WITH FIXED HEIGHT", "_"),
    ("MEDIUM-HIGH OVERLINE WITH FIXED HEIGHT", "_"),
    # NUMBERS
    ("ROMAN NUMERAL CAPITAL ([A-Z]) WITH TWO BARS", "\g<1>"),
    ("ROMAN NUMERAL SMALL ([A-Z]) WITH TWO BARS", "#\g<1>"),
    # Money ?
    ("(FRENCH|ITALIAN|FLEMISH|DUTCH) LIBRA SIGN", "£"),
    ("MARK SIGN", "m"),
    ("FLOREN SIGN", "F"),
    ("FLOREN SIGN", "F"),
    # NOISE
    ("MEDIUM-", ""),
    ("OLD ", ""),
    ("FLOURISH ", ""),
    ("CAPITAL ", ""),
    ("SMALL ", "#"),
    ("SPACING BASE-LINE ", ""),
    (" HORIZONTAL TILDE", ""),
    ("^METRICAL SYMBOL( [A-Z ]+)", "m"),
    ("^([A-Z ]+)SIGN$", "_")
]
"""
A WITH OGONEK AND ACUTE
A WITH MACRON AND ACUTE
A WITH MACRON AND BREVE
A WITH DOUBLE ACUTE
A WITH #E ABOVE
A 
AE "WITH DOT (BELOW|ABOVE)"
AE "WITH (MACRON|ACUTE|BREVE|DIARESIS)( AND (MACRON|ACUTE|BREVE|DIARESIS))?"
AE "WITH MACRON AND BREVE"
AE "WITH BREVE"
AE WITH OGONEK
AE WITH DOUBLE ACUTE
AE WITH DIAERESIS
AE WITH DOT ABOVE
"""

compiled_steps = [(re.compile(regex_capture), regex_sub) for regex_capture, regex_sub in steps]

Missed = {"openo": "o",
"ABBREVIATIONMARKSUPERSCRIPTURROUNDRFORM": "_",
"baselinezerosign": "0",
"ABBREVIATIONMARKWITHDOT": "_",
"ABBREVIATIONMARKSUPERSCRIPTRAOPENAFORMABOVE": "ur",
"ABBREVIATIONMARKSUPERSCRIPTURLEMNISKATEFORM": "ur",
"CURLHIGHPOSITION": "_",
"ABBREVIATIONMARKZIGZAGABOVEANGLEFORM": "_",
"ABBREVIATIONMARKZIGZAGABOVECURLYFORM": "_",
"DOTABOVEHIGHPOSITION": "_",
"CURLY": "_",
"TRIPLEDAGGER": "_",
"MIDDLERING": "_",
"MEDIEVALCOMMA": ",",
"PARAGRAPHUS": "_",
"COMMAPOSITURA": ",",
"HIGHCOMMAPOSITURA": ",",
"PUNCTUSWITHCOMMAPOSITURA": ".",
"COLONWITHMIDDLECOMMAPOSITURA": ";",
"THREEDOTSWITHCOMMAPOSITURA": ",",
"SIGNEDERENVOI": "_",
";DIAGONALSTROKE": ";",
"!LEMNISKATEFORM": "!",
"TWODOTSOVERCOMMAPOSITURA": ",",
"VIRGULASUSPENSIVA": ",",
"PUNCTUSFLEXUS": ".",
"SHORTVIRGULA": ",",
"DISTINCTIO": "/",
"WAVYLINE": "_",
";WITHHIGHBACK": ";",
";WITHHACKLE": ";",
"TRIPLEBREVEBELOW": "_",
"ROMANNUMERALREVERSEDONEHUNDREDWITHOVERLINE": "C",
"markedlettermsign": "m",
"flourishedlettermsign": "f",
"ABBREVIATIONMARKSUPERSCRIPTRAAFORMABOVE": "RAA"
}

output = {

}
with open("mufi.csv") as f:
    reader = csv.reader(f)
    for code, legend, transform in reader:
        for step_re, sub in compiled_steps:
            transform = step_re.sub(sub, transform)

        transform = transform.replace(" AND ", "").replace("OPEN", "").replace(" ", "").replace("THORN", "TH")
        if "#" in transform:
            transform = transform.replace("#", "").lower()

        if transform in Missed:
            transform = Missed[transform]

        output[(int(code[:2], 16), int(code[2:], 16))] = transform


print(output)

