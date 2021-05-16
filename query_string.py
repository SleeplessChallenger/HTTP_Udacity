from urllib.parse import urlparse, parse_qs

u = urlparse('https://www.google.com/search?q=japan+foundation+'
			 'marugoto&rlz=1C5CHFA_enRU941RU944&oq=japan+foun&aqs'
			 '=chrome.2.0j69i57j0l8.3720j0j7&sourceid=chrome&ie=UTF-8')

print(u, 'whole string')

print(u.query, 'query part')

print(parse_qs(u.query), 'query part with parse_qs')

print(parse_qs('texture=fuzzy&animal=gray+squirrel'))
