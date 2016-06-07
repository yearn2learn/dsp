#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


import csv

def read_data(data):
  with open(data, 'rb') as f:
    reader = csv.reader(f)
    next(reader, None)
    return list(reader)
  
def find_score_diff(parsed_data):
  teamDiff = []
  for team in parsed_data:
    teamDiff.append([team[0],int(team[5])-int(team[6])])
  teamDiff = sorted(teamDiff, key=lambda x: x[1], reverse=True)
  return teamDiff
	
def get_min_score_difference(parsed_data):
  min_score = min(parsed_data, key=lambda x: abs(x[1]))
  print 'The minimum score difference is {0} by {1}.'.format(min_score[1], min_score[0])
  return min_score

def get_team(index_value, parsed_data):
  print "Team: {0}".format(parsed_data[index_value][0])
  print "Games: {0}".format(parsed_data[index_value][1])
  print "Wins: {0}".format(parsed_data[index_value][2])
  print "Losses: {0}".format(parsed_data[index_value][3])
  print "Draws: {0}".format(parsed_data[index_value][4])
  print "Goals: {0}".format(parsed_data[index_value][5])
  print "Goals Allowed: {0}".format(parsed_data[index_value][6])
  print "Points: {0}".format(parsed_data[index_value][7])
  return parsed_data[index_value]

# RUN BELOW
all_data = read_data('football.csv')
scores = find_score_diff(all_data)
min_score = get_min_score_difference(scores)
get_team(5, all_data)

'''
# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.

  def read_data(data):
   # COMPLETE THIS FUNCTION
    with open(data, 'rb') as f:
      reader = csv.reader(f)
      return data_list = list(reader)
  
  def find_score_diff(self, parsed_data):
    next(reader, None)

  def get_min_score_difference(self, parsed_data):
    # COMPLETE THIS FUNCTION

  def get_team(self, index_value, parsed_data):
    # COMPLETE THIS FUNCTION
'''
