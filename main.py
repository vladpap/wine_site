from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from excel_wines import get_wines_excel
from difference_years import get_difference_years_rus
import pandas
import settings


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    creation_company_year = 1920

    excel_content = pandas.read_excel(
        settings.excel_path,
        sheet_name='Лист1').fillna("")

    site_content = {
        "wine_category": get_wines_excel(excel_content),
        "years_with_you": get_difference_years_rus(creation_company_year)
    }

    template = env.get_template('template.html')

    rendered_page = template.render(site_content=site_content)

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
