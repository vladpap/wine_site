import pandas
import collections
from pprint import pprint


def get_wines_excel(excel_data_df):
    excel_category = excel_data_df.columns.ravel()[0]

    count_category = collections.Counter(excel_data_df[excel_category].tolist())

    wines_from_category = {}
    for wine_category in count_category:
        df_filter = excel_data_df["Категория"].isin([wine_category])
        wines_from_category[wine_category] = excel_data_df[df_filter].to_dict(orient='records')

    return dict(sorted(wines_from_category.items()))


def main():
    excel_data = pandas.read_excel("content/wine3.xlsx", sheet_name='Лист1').fillna("")
    pprint(get_wines_excel(excel_data))


if __name__ == "__main__":
    main()
