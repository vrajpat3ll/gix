STYLES = {
    "bold"             : 1,
    "italic"           : 3,
    "underline"        : 4,
    "strikethrough"    : 9,
    "gray"             : 30,
    "red"              : 31,
    "green"            : 32,
    "yellow"           : 33,
    "blue"             : 34,
    "magenta"          : 35,
    "cyan"             : 36,
    "white"            : 37,
    "inverted-gray"    : 40,
    "inverted-red"     : 41,
    "inverted-green"   : 42,
    "inverted-yellow"  : 43,
    "inverted-blue"    : 44,
    "inverted-magenta" : 45,
    "inverted-cyan"    : 46,
    "inverted-white"   : 47,
}


def stylise(msg:str, style: str):
    """add style / color to your string

    Args:
        msg (str): string to be stylised
        style (str): style | options -> [`bold`, `italic`, `underline`, `strikethrough`, `gray`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, `inverted-gray`, `inverted-red`, `inverted-green`, `inverted-yellow`, `inverted-blue`, `inverted-magenta`, `inverted-cyan`, `inverted-white`]

    Returns:
        str: stylised string
    """
    try:
        styled_msg = f"\033[{STYLES[style]}m" + msg + "\033[0m"
    except Exception as e:
        print("Error: incorrect style specified. Defaulting to original...")
        return msg
    
    return styled_msg