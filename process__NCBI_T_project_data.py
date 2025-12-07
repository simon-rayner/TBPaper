import pandas
import pandas as pd
file_path = '/media/simonray/data24/data/uio_dropbox_sr/DResearch/Rosa/data/MTB__Genome__bioproject_result_v2.xlsx'
df__genomes = pd.read_excel(file_path)
print(df__genomes["Country"].unique())

df__genomes["GenomeCount"].sum()
sum_by_category = df__genomes.groupby('Country')['GenomeCount'].sum()
#sum_by_category.to_csv('/home/simonray/PycharmProjects/TBPaper/data/TB_sequenced_genomes_by_country_v2.csv', header=True)
df_genomes_by_country=df__genomes.groupby('Country')['GenomeCount'].sum().to_frame()
df_genomes_by_country.reset_index()
df_genomes_by_country.rename(columns={"Country","GenomeCount"})
df_genomes_by_country= pd.read_csv("/home/simonray/PycharmProjects/TBPaper/data/TB_sequenced_genomes_by_country_WHO_v2.csv")

tb_case_data_path="/home/simonray/PycharmProjects/TBPaper/data/TB_burden_countries_2025-12-07.csv"
df_tb_case_data=pandas.read_csv(tb_case_data_path)

df_tb_case_data__2024 = df_tb_case_data[df_tb_case_data['year'] == 2024]
df_tb_case_data__2024.to_csv("/home/simonray/PycharmProjects/TBPaper/data/TB_burden_countries_2024_data.csv")

df_tb_case_data__2024.loc[df_tb_case_data__2024['country'] == 'Viet Nam', 'country'] = 'Vietnam'
df_tb_case_data__2024.loc[df_tb_case_data__2024['country'] == 'Russian Federation', 'country'] = 'Russia'

df__tb_cases_and_genomes = pd.merge(df_tb_case_data__2024, df_genomes_by_country, left_on='country', right_on='Country', how='inner')
df__tb_cases_and_genomes.to_csv("/home/simonray/PycharmProjects/TBPaper/data/TB_burden_countries_2024__vs__genomes.csv")
unique_to_TB_cases = set(df_tb_case_data__2024['country']) - set(df_genomes_by_country['Country'])
unique_to_Genomes = set(df_genomes_by_country['Country']) - set(df_tb_case_data__2024['country'])


print(1)