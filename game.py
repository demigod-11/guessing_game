import math
from flask import redirect, render_template, request, session

def guess(n):
    return math.log(n, 2)

def guesses(n, call):
    high = n
    low = 0
    n = mid(high, low)
    if call == "large":
        high = n
    elif call == "less":
        low = n
    elif call == "found":
        return "found"
    else:
        return "wrong Input"
    return n
        

def mid(n, x):
    return (n + x) // 2

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message))