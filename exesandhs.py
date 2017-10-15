def xo(s):
    if s.count('x') == s.count('o') and s.count('X') == s.count('O'):
        return True
    else:
        return False

xo("hfhghg")