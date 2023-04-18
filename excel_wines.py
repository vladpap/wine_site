import pandas
import collections
from pprint import pprint


def get_wines_excel(excel_path, sheet_name='Лист1'):
    excel_data_df = pandas.read_excel(excel_path, sheet_name=sheet_name).fillna("")

    excel_categorys = excel_data_df.columns.ravel()[0]

    count_categorys = collections.Counter(excel_data_df[excel_categorys].tolist())

    list_wines_from_category = {}
    for wine_category in count_categorys:
        df_filter = excel_data_df["Категория"].isin([wine_category])
        list_wines_from_category[wine_category] = excel_data_df[df_filter].to_dict(orient='records')

    return dict(sorted(list_wines_from_category.items()))


def main():
    pprint(get_wines_excel('assets/wine3.xlsx'))


if __name__ == "__main__":
    main()
