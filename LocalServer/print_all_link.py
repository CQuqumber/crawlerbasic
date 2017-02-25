def get_next_target(page):
	start_link = page.find("<a href=")
	if start_link == -1:
		return None, 0
	else:
		start_quote = page.find('"',start_link)
		end_quote = page.find('"',start_quote + 1)
		url = page[start_quote + 1 : end_quote]
		return url, end_quote

def print_all_link(page):
	while True:
		url, end_pos = get_next_target(page)
		if url:
			print url
			page = page[end_pos : ]
		else:
			break

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''

print print_all_link(get_page("http://www.facebook.com"))
