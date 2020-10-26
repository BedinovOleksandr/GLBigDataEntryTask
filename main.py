import pandas as pd

file = 'summer_products.csv'
sp = pd.read_csv(file, sep=',')


def make_report(csv_file):
    csv_file['avg'] = csv_file.groupby('origin_country')['price'].transform('mean')
    csv_file['five_percentage'] = csv_file.groupby('origin_country')['rating_five_count'].transform('sum') \
                            / csv_file.groupby('origin_country')['rating_count'].transform('sum') * 100
    result = csv_file[['avg', 'five_percentage', 'origin_country']].drop_duplicates().sort_values(by=['origin_country']).copy()
    return result


if __name__ == '__main__':
    make_report(sp).to_csv('result.csv', index=None)
    res = pd.read_csv('result.csv')
    print(res)