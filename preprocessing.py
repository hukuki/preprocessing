import string
import re
import unicodedata


weird_chars_keys = "á×‘ãòŷІ≤ý˂ ≈οà′éȗȋ–—‐а’“š≥É‚êïìŜóú⁄å‒”ô℮è―˃ʺÌ¡„−íäķậēÏ"
weird_chars_values = 'ax\'aoyI<y< =oa\'eui---a\'"ş>E,eiiSou/a-"oee->"İi,-iakaeİ'

def clear_text(text):
    text = unicodedata.normalize('NFKC', text) # Normalize unicode 
    text = re.sub(r'\s+', ' ', text) # Remove extra spaces
    text = text.translate(str.maketrans('âîûÂÎÛ', 'aiuAİU')) # Normalize Turkish characters by removing circumflex
    text = text.translate(str.maketrans(weird_chars_keys, weird_chars_values)) # Fix weird characters
    text = text.strip() # Remove leading and trailing spaces
    return text





"""
weird_char_mapping = {
    'á': "a",
    '×': "x",
    '‘': "'",
    'ã': "a", 
    'ò': "o", 
    'ŷ': "y",
    'І': "I",
    '≤': "<",
    'ý': "y",
    '˂': "<",
    ' ': " ",
    '≈': "=",
    'ο': "o", 
    'à': "a", 
    '′': "'", 
    'é': "e", 
    'ȗ': "u", 
    'ȋ': "i",
    '–': "-", 
    '—': "-", 
    '‐': "-", 
    'а': "a", 
    '’': "'", 
    '“': "\"", 
    'š': "ş", 
    '≥': ">", 
    'É': "E", 
    '‚': ",", 
    'ê': "e", 
    'ï': "i", 
    'ì': "i", 
    'Ŝ': "S", 
    'ó': "o",
    'ú': "u",
    '⁄': "/", 
    'å': "a", 
    '‒': "-", 
    '”': "\"", 
    'ô': "o", 
    '℮': "e", 
    'è': "e", 
    '―': "-", 
    '˃': ">", 
    'ʺ': "\"", 
    'Ì': "İ",
    '¡': "i",
    '„': ",", 
    '−': "-", 
    'í': "i",
    'ä': "a", 
    'ķ': "k", 
    'ậ': "a",
    'ē': "e", 
    'Ï': "İ",
}"""