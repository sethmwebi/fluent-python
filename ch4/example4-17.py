import string
import unicodedata


def shave_marks_latin(txt):
    """Remove all diacritic marks from Latin base characters"""
    norm_txt = unicodedata.normalize("NFD", txt)
    latin_base = False
    preserve = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue  # ignore diacritic on Latin base char
        preserve.append(c)
        # if it isn't a combining char, it's a new base char
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
    shaved = "".join(preserve)
    return unicodedata.normalize("NFC", shaved)


single_map = str.maketrans("""‚ƒ„ˆ‹‘’“”•–—˜›""", """'f"^<''""---~>""")

multi_map = str.maketrans(
    {
        "€": "EUR",
        "…": "...",
        "Æ": "AE",
        "æ": "ae",
        "Œ": "OE",
        "œ": "oe",
        "™": "(TM)",
        "‰": "<per mille>",
        "†": "**",
        "‡": "***",
    }
)

converted_single_map = {k: chr(v) for k, v in single_map.items()}

multi_map.update(converted_single_map)


def dewinize(txt: str):
    """Replace Win1252 symbols with ASCII chars or sequences"""
    return txt.translate(multi_map)


def asciize(txt: str):
    no_marks = shave_marks_latin(dewinize(txt))
    no_marks = no_marks.replace("ß", "ss")
    return unicodedata.normalize("NFKC", no_marks)


order = "“Herr Voß: • ½ cup of Œtker™ caffè latte • bowl of açaí.”"
print(asciize(order))
