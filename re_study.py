import re

# str = 'khuimap pizda, dzhygurda map'
# match = re.findall(r'\bmap\b', str)

# str = "eda, beda, pobeda, pobEdu"
# match = re.findall(r"[eE]d[au]", str)

str = "eda, beda, 55 pobeda, pobEdu"
match = re.findall(r"[^0-9]", str)




print(match)