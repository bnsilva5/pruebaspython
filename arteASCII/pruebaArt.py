import ascii_magic

output = ascii_magic.from_image_file('img/py2.jpg', mode=ascii_magic.Modes.HTML)
ascii_magic.to_html_file('nicholas2.html', output,additional_styles='background: #222;')