# User configuration file typically located at `~/.config/nerd-dictation/nerd-dictation.py`
import re

# -----------------------------------------------------------------------------
# Replace Multiple Words

TEXT_REPLACE_REGEX = (
    ("\\b" "data type" "\\b", "data-type"),
    ("\\b" "copy on write" "\\b", "copy-on-write"),
    ("\\b" "key word" "\\b", "keyword"),
    ("\\b" "x ray" "\\b", "x-ray"),

    ("\\b" "be factor" "\\b", "refactor"),
    ("\\b" "pre factor" "\\b", "refactor"),

    ("\\b" "a wait" "\\b", "await"),
    ("\\b" "awaits" "\\b", "await"),
    ("\\b" "a sink" "\\b", "async"),
    ("\\b" "it a raider" "\\b", "iterator"),

    ("\\b" "localhost" "\\b", "localhost"),

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

    ("\\b" "been to" "\\b", "Ubuntu"),
    ("\\b" "debbie in" "\\b", "Debian"),

    ("\\b" "a p eyes" "\\b", "APIs"),
    ("\\b" "a p i" "\\b", "API"),

    ("\\b" "cp you" "\\b", "CPU"),

    ("\\b" "w three see" "\\b", "W3C"),
    ("\\b" "I pfs" "\\b", "IPFS"),
    ("\\b" "I pianos" "\\b", "IPNS"),
    ("\\b" "see id" "\\b", "cid"),
    ("\\b" "you are a?l" "\\b", "URL"),
    ("\\b" "u r l" "\\b", "URL"),
    ("\\b" "you are else" "\\b", "URLs"),

    ("\\b" "probably tree" "\\b", "prolly tree"),

    ("\\b" "m o g" "\\b", "emoji"),

    # these make it easier to program in go lang
    ("\\b" "go error" "\\b", "err"),
    ("\\b" "go format" "\\b", "go fmt"),

    ("\\b" "\s?equals\s?" "\\b", "="),
    ("\\b" "\s?plus\s?" "\\b", "+"),
    ("\\b" "\s?hyphen\s?" "\\b", "-"),
    ("\\b" "\s?dash\s?" "\\b", "-"),
    ("\\b" "\s?asterisk\s?" "\\b", "*"),
    ("\\b" "\s?tilda\s?" "\\b", "~"),
    ("\\b" "\s?dot\s?" "\\b", "."),

    ("\\b" "\s?under\s?score\s?" "\\b", "_"),
    ("\\b" "\s?hash\s?tag\s?" "\\b", "#"),
    ("\\b" "\s?at\s?sign\s?" "\\b", "@"),
    ("\\b" "\s?dollar\s?sign\s?" "\\b", "$"),
    ("\\b" "\s?back\s?slash\s?" "\\b", "\\\\"),
    ("\\b" "\s?slash\s?" "\\b", "/"),
    ("\\b" "\s?vertical bar\s?" "\\b", "|"),
    ("\\b" "\s?back\s?tick\s?" "\\b", "`"),
    ("\\b" "\s?new\s?line\s?" "\\b", "\n"),
)

TEXT_REPLACE_REGEX = tuple(
    (re.compile(match), replacement)
    for (match, replacement) in TEXT_REPLACE_REGEX
)

# -----------------------------------------------------------------------------
# Replace Single Words

# VOSK-API doesn't use capitals anywhere so they have to be explicitly added in.
WORD_REPLACE = {
    "i": "I",
    "api": "API",
    "linux": "Linux",
    "jason": "JSON",

    "haifa": "Hypha",

    "vex": "Vex",
    "vax": "Vex",

    "okay": "ok",
    "maine": "main",

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
    "close carrot": ">",
    "close tick": "'",
}

OPENING_PUNCTUATION = {
    "open quote": '"',
    "open bracket": '(',
    "open brace": '{',
    "open square": '[',
    "open carrot": '<',
    "close tick": "'",
}


SPACE_REGEX = re.compile("\\b" "\s?space bar\s?" "\\b")

# -----------------------------------------------------------------------------
# Type individual characters

NATO_ALPHABET = {
    "alpha": "a",
    "bravo": "b",
    "charlie": "c",
    "delta": "d",
    "echo": "e",
    "foxtrot": "f",
    "golf": "g",
    "hotel": "h",
    "india": "i",
    "juliet": "j",
    "kilo": "k",
    "lima": "l",
    "mike": "m",
    "november": "n",
    "oscar": "o",
    "papa": "p",
    "quebec": "q",
    "romeo": "r",
    "sierra": "s",
    "tango": "t",
    "uniform": "u",
    "victor": "v",
    "whiskey": "w",
    "x-ray": "x",
    "yankee": "y",
    "zulu": "z"
}

def make_tokens(text):
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
        if w in NATO_ALPHABET:
            w = NATO_ALPHABET[w]
        words[i] = w

    # Strip any words that were replaced with empty strings.
    words[:] = [w for w in words if w]

    return words


def word_typing(text):
    return SPACE_REGEX.sub(" ", " ".join(make_tokens(text)))

def word_scream(text):
     return word_typing(text).upper()

def word_snake(text):
    return "_".join(make_tokens(text))

def word_scream_snake(text):
    return word_snake(text).upper()

def word_camel(text):
    tokens = make_tokens(text)
    if not len(tokens):
        return ""
    first = tokens.pop(0)
    capped = [word.capitalize() for word in tokens]
    return first + "".join(capped)

def word_dictate(text):
    return "".join(make_tokens(text))

def word_proper_camel(text):
    camelized = word_camel(text)
    proper = camelized[:1].upper() + camelized[1:]
    return proper

text_mode = "speak"

modes = {
    "speak":  word_typing,
    "cap":  word_scream,
    "snake": word_snake,
    "screaming snake": word_scream_snake,
    "camel": word_camel,
    "proper camel": word_proper_camel,
    "dictate": word_dictate
}

# -----------------------------------------------------------------------------
# Main Processing Function

def nerd_dictation_process(text):
    global text_mode
    for mode in modes:
        activator = "mode "+mode
        if activator in text:
            text = text.replace(activator, "")
            text_mode = mode
    return modes[text_mode](text)
