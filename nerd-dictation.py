# User configuration file typically located at `~/.config/nerd-dictation/nerd-dictation.py`
import re


# -----------------------------------------------------------------------------
# Replace Multiple Words

TEXT_REPLACE_REGEX = (
    ("\\b" "data type" "\\b", "data-type"),
    ("\\b" "copy on write" "\\b", "copy-on-write"),
    ("\\b" "key word" "\\b", "keyword"),
    ("\\b" "be factor" "\\b", "refactor"),
    ("\\b" "pre factor" "\\b", "refactor"),
    ("\\b" "agora core" "\\b", "Agregore"),
    ("\\b" "agora gore" "\\b", "Agregore"),
)

TEXT_REPLACE_REGEX = tuple(
    (re.compile(match), replacement)
    for (match, replacement) in TEXT_REPLACE_REGEX
)

# -----------------------------------------------------------------------------
# Replace Single Words

# VOSK-API doesn't use capitals anywhere so they have to be explicit added in.
WORD_REPLACE = {
    "i": "I",
    "api": "API",
    "linux": "Linux",
    "vex": "Vex",
    "vax": "Vex",


    # It's also possible to ignore words entirely.
    "um": "",
}


# Regular expressions allow partial words to be replaced.
WORD_REPLACE_REGEX = (
    ("^i'(.*)", "I'\\1"),
)
WORD_REPLACE_REGEX = tuple(
    (re.compile(match), replacement)
    for (match, replacement) in WORD_REPLACE_REGEX
)

# -----------------------------------------------------------------------------
# Add Punctuation

CLOSING_PUNCTUATION = {
    "period": ".",

    "comma": ",",
    "karma": ", ",
    "calmer": ", ",
    "comment": ", ",

    "question mark": "?",
    "exclamation mark": '!',

    "hyphen":  "-",
    "colin": ":",
    "semi colon": ";",

    "close quote": '"',
    "close bracket": ')',
    "close brace": '}',
    "close square": ']',
}

OPENING_PUNCTUATION = {
    "open quote": '"',
    "open bracket": '(',
    "open brace": '{',
    "open square": '[',
}

# -----------------------------------------------------------------------------
# Main Processing Function

def nerd_dictation_process(text):

    for match, replacement in TEXT_REPLACE_REGEX:
        text = match.sub(replacement, text)

    for match, replacement in CLOSING_PUNCTUATION.items():
        text = text.replace(" " + match, replacement)
        text = text.replace(match, replacement)

    for match, replacement in OPENING_PUNCTUATION.items():
        text = text.replace(match + " ", replacement)
        text = text.replace(match, replacement)

    words = text.split(" ")

    for i, w in enumerate(words):
        w_init = w
        w_test = WORD_REPLACE.get(w)
        if w_test is not None:
            w = w_test
        if w_init == w:
            for match, replacement in WORD_REPLACE_REGEX:
                w_test = match.sub(replacement, w)
                if w_test != w:
                    w = w_test
                    break

        words[i] = w

    # Strip any words that were replaced with empty strings.
    words[:] = [w for w in words if w]

    return " ".join(words)