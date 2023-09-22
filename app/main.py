import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv("data.csv")
  labels, values = utils.get_porcentage(data)
  charts.generate_pie_chart(labels, values)
  
  country = input("Digite el pais => ")
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country2 = result[0]
    labels, values = utils.get_population(country2)
    charts.generate_bar_chart(country, labels, values)

if __name__ == "__main__":
  run()