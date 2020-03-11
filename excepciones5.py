import re
patron = re.compile("^https?:\/\/[\w\-]+(\.[\w\-]+)+[/#?]?.*$")
url="http://moodletest.proteco.mx"
if patron.search(url) is not None:
    print("Hizo match")
