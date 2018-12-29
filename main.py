import click
import math

CRED = '\033[91m'
CGREEN = '\033[92m'
CEND = '\033[0m'

@click.group()
def main():
  """
  This program uses a mathematical model to predict photopollution based on population density for Munster, Ireland.  
  
  This work is part of BT Young Scientist project, 'Is It Possible to Create a Mathematical Model to Predict Photopollution Based on Population Density in Munster'
  
  To predict the photopollution for a town, you can do:

  $ python3 main.py town Limerick

  To predict the photopollution from population density, you can do:

  $ python3 main.py pd 2500
  """
  pass

@main.command()
@click.argument('location', required=False)
def town(location):
  """
  Predict from a town name.
  """
  # This is done here to speed up other methods
  import pandas as pd

  # If no location is given, prompt.
  if not location:
    location = click.prompt("Please input the name of the town")

  pd_filename = 'data/population_density/populationdensitycensustowns.csv'
  pd_data = pd.read_csv(pd_filename)
  town = pd_data[pd_data['Towns'].str.contains(location, case=False)]

  if town.empty:
    return click.echo(CRED + 'No data on the town: {}'.format(location) + CEND)

  pd = float(town['PD'])
  print_conditions(pd)

@main.command()
@click.argument('population_density', required=False)
def pd(population_density):
  """
  Predict from population density.
  """

  while not population_density or not isfloat(population_density):
    if population_density:
      click.echo(CRED + 'Please input a valid population density' + CEND)

    population_density = click.prompt("Please input the population density")

  print_conditions(population_density)

@main.command()
def version():
  """
  Show the version history of the tool
  """
  with open('CHANGELOG.md', 'r') as fin:
    click.echo(fin.read())

@main.command()
def license():
  """
  Show the license of the tool
  """
  with open('LICENSE', 'r') as fin:
    click.echo(fin.read())


def get_conditions(lux):
  # Hard code in limerick's lux
  limerick_lux = 41.535984211999995

  # Get score as a percent
  score = (lux / limerick_lux) * 100

  message = '"Excellent Stargazing Conditions"'
  if score >= 80:
    message = "Terrible Stargazing Conditions"
  elif score >= 60:
    message = "Poor Stargazing Conditions"
  elif score >= 40:
    message = "Fair Stargazing Conditions"
  elif score >= 20:
    message = "Good Stargazing Conditions"

  return CGREEN + message + CEND, score	

def print_conditions(pd):
  lux = lux = 0.03510566 * float(pd) - 14.32414198
  conditions, score = get_conditions(lux)
  if score >= 0:
    		click.echo("Photopollution in this location is approximately """ + str(int(math.ceil(lux))) + " LUX, this should " + """correlate to """ + conditions)
  else:
  		click.echo("Oops, it appears we are getting a negative LUX value. Your population density is extremely low, therefore, this correlates to Excellent Stargazing Conditions.")


def isfloat(value):
  """Check if a string is a float"""
  try:
    float(value)
    return True
  except ValueError:
    return False

if __name__ == "__main__":
    main()