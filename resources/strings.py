from resources.conditions import ResponseStatus

PROTOCOL = "РКСОК/1.0"
PREFIX = "АМОЖНА? Р КСОК/1.0\r\n"
POSTFIX = "\r\n\r\n"
MESSAGE_PATTERN = r"(.*?)\s?([\s.]*)\s?\w{5}/1.0.*\s(.*)[.\r\n]*"


INCORRECT_REQUEST = f"{ResponseStatus.INCORRECT_REQUEST.value} {PROTOCOL}{POSTFIX}"
CORRECT = f"{ResponseStatus.OK.value}  {PROTOCOL}\r\n" + "{data}" +f"{POSTFIX}"
DONE = f"{ResponseStatus.OK.value} {PROTOCOL}{POSTFIX}"
NOTFOUND = f"{ResponseStatus.NOTFOUND.value} {PROTOCOL}{POSTFIX}"
