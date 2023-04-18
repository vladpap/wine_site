from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from excel_wines import get_wines_excel
from difference_years import get_difference_years_rus


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

data = {"wine_categotys": get_wines_excel("content/wine3.xlsx"),
        "years_with_you": get_difference_years_rus(1920)}

template = env.get_template('template.html')

rendered_page = template.render(data=data)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
