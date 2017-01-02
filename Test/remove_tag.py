# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.



def remove_tags(ist):
    Text = []
    def get_next(ist):
        st_pos = ist.find("<")
        #print "st_pos: ",st_pos
        if st_pos == -1:
            return None, 0
        end_pos = ist.find(">",st_pos + 1)
        #print "end_pos: ",end_pos
        tag_txt = ist[st_pos + 1 : end_pos]
        end_tag_pos = ist.find("</"+tag_txt+">",end_pos )
        in_tag_txt = ist[end_pos+1:end_tag_pos]
        new_tag_pos =end_tag_pos + len("</"+tag_txt+">")

        return in_tag_txt, new_tag_pos

    while True:
        in_tag_txt, new_tag_pos = get_next(ist)
        if in_tag_txt:
            Text.append(in_tag_txt)
            ist = ist[new_tag_pos:]
        else:
            break
    return Text


print remove_tags("This is plain text.")
print remove_tags("<h1>Hello</h1><p>Trapping<h3>World</h3><h1>Hello</h1>Trapping")
