from urllib.parse import quote
from urllib.parse import unquote


def quote_underscore(s, safe=''):
    if ' ' in s:
        s = quote(s, safe + ' ')
        return s.replace(' ', '_')
    return quote(s, safe)

def unquote_underscore(s):
    """unquote('%7e/abc_def') -> '~/abc def'"""
    s = s.replace('_', ' ')
    return unquote(s)

def pack_url_path(value, none='-'):
    if value is None:
        value = none
    value = value.lower()
    return quote_underscore(value)
    
def unpack_url_path(path, none='-'):
    if path == none:
        return None
    return unquote_underscore(path)
