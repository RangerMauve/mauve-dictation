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
    ("\\b" "a wait" "\\b", "await"),
    ("\\b" "hyper core" "\\b", "hypercore"),

    ("\\b" "get hub" "\\b", "Github"),
    ("\\b" "git hub" "\\b", "Github"),
    ("\\b" "good have" "\\b", "Github"),
    ("\\b" "get have" "\\b", "Github"),

    ("\\b" "fedor verse" "\\b", "Fediverse"),
    ("\\b" "fed averse" "\\b", "Fediverse"),
    ("\\b" "activity pub" "\\b", "ActivityPub"),

    ("\\b" "web recorder" "\\b", "Webrecorder"),

    ("\\b" "sadie panel" "\\b", "Sutty panel"),
    ("\\b" "sorry panel" "\\b", "Sutty panel"),
    ("\\b" "saudi panel" "\\b", "Sutty panel"),

    ("\\b" "hi fi" "\\b", "Hypha"),

    ("\\b" "agora core" "\\b", "Agregore"),
    ("\\b" "agora gore" "\\b", "Agregore"),
    ("\\b" "agricole" "\\b", "Agregore"),
    ("\\b" "agricola" "\\b", "Agregore"),
    ("\\b" "agra court" "\\b", "Agregore"),
    ("\\b" "agra gore" "\\b", "Agregore"),

    ("\\b" "a p eyes" "\\b", "APIs"),
    ("\\b" "a p i" "\\b", "API"),

    ("\\b" "cp you" "\\b", "CPU"),

    ("\\b" "w three see" "\\b", "W3C"),
    ("\\b" "I pfs" "\\b", "IPFS"),
    ("\\b" "I pianos" "\\b", "IPNS"),
    ("\\b" "you are a?l" "\\b", "URL"),
    ("\\b" "u r l" "\\b", "URL"),
    ("\\b" "you are else" "\\b", "URLs"),

    ("\\b" "\s?equals\s?" "\\b", "="),
    ("\\b" "\s?plus\s?" "\\b", "+"),
    ("\\b" "\s?hyphen\s?" "\\b", "-"),
    ("\\b" "\s?dash\s?" "\\b", "-"),
    ("\\b" "\s?asterisk\s?" "\\b", "*"),
    ("\\b" "\s?tilda\s?" "\\b", "~"),
    ("\\b" "\s?dot\s?" "\\b", "."),

    ("\\b" "\s?under\s?score\s?" "\\b", "_"),
    ("\\b" "\s?hash\s?tag\s?" "\\b", "#"),
    ("\\b" "\s?back\s?slash\s?" "\\b", "\\\\"),
    ("\\b" "\s?back\s?tick\s?" "\\b", "`"),
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
    "jason": "JSON",

    "vex": "Vex",
    "vax": "Vex",

    # It's also possible to ignore words entirely.
    "um": "",
    "huh": "",
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
    "karma": ",",
    "calmer": ",",

    "question mark": "?",
    "exclamation mark": '!',

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

def word_typing(text):
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

def do_nothing():
     return  ""

def word_scream(text):
     return word_typing(text).upper()

text_mode = "speak"

modes = {
    "speak":  word_typing,
    "silence":  do_nothing,
    "scream":  word_scream
}

# -----------------------------------------------------------------------------
# Main Processing Function

def nerd_dictation_process(text):
    if text_mode == "speak":
         return word_typing(text)
    return text
