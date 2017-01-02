def remove_tags(stringlist):

	start_tag = stringlist.find('<')
	while start_tag != -1:
		end_tag = stringlist.find('>',start_tag )
		stringlist = stringlist[:start_tag:] + " " +stringlist[end_tag +1:]
		start_tag = stringlist.find('<')
	return stringlist.split()










print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
print remove_tags("<h1>This</h1><p>is plain text.")

print remove_tags("This is plain text.")
print remove_tags("<h1>Hello</h1><p>Trapping<h3>World</h3><h1>Hello</h1>Trapping")