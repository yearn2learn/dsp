import re, csv

class Faculty:
  def __init__(self, data):
    self.data = self.read_data(data)

  def read_data(self, data):
    with open(data, 'rb') as f:
      return f.read()

  def write_csv(self, file, data):
    with open(file, 'w') as f:
      writer = csv.writer(f)
      for row in eval('self.all_'+data):
        print 'Writing {0}: {1}'.format(data, row)
        writer.writerow([row])

  def parse(self):
    prof = []
    prof = re.findall(r'(\w.*?), *(.*?),(\w.*),(\w.*)', self.data, re.I)
    print "Number of professors: {}.".format(len(prof))
    return prof

  def find_type(self, column, repl=True, spl=True, data='self.professors'):
    # List of Type from Each Prof, Name-0 Degree-1 Title-2 Email-3
    all_type = map(lambda x: x[column].replace(str(repl), "").split(str(spl)), eval(data))
    # Flatten List
    all_type = [item for sublist in all_type for item in sublist]
    return all_type

  def make_unique(self, type_list):
    return set(eval("self"+"."+type_list))

  def count(self, to_find, column):
    count = 0
    for x in eval("self"+".all_"+column):
      if x == to_find:
        count += 1
    # Uncomment below if you would like a nicer format
    print "Number of {0}: {1}.".format(to_find, count)
    return count

  def count_type(self, column):
    count_type_list = {}
    for each in eval("self"+"."+column+"_types"):
      count_type_list[each] = self.count(each, column)
    return count_type_list

  def get_domains(self):
    domains = re.findall(r'\w.*@(\w.*)', self.data, flags=re.I)
    return domains

  def make_dict(self):
    faculty_dict = {}
    fac_reg = re.compile('(?P<first>\w.*) .*? (?P<last>[A-Z].*?), *(?P<degree>.*?),(?P<title>\w.*) (of|is) Biostatistics,(?P<email>\w.*@(?P<domain>\w.*))')
    for m in fac_reg.finditer(self.data):
      # Below was used for Q6
      # faculty_dict.setdefault(m.group('last'), []).append( [ m.group('degree'), m.group('title'), m.group('email') ] )
      faculty_dict[ m.group('first'), m.group('last') ] = [ m.group('degree'), m.group('title'), m.group('email') ]
#    return sorted(faculty_dict.items(), key=lambda x: x[0][1])  # Could sort here but prefer the unsorted dict and then sort on its own
    return faculty_dict

  def print_dict(self):
    for k, v in sorted(self.professor_dict.items(), key=lambda x: x[0][1]):
        print k, v


# RUN >>>>>

# PART I >>>>>>>>>
Penn = Faculty('faculty.csv')
Penn.professors = Penn.parse()

Penn.all_degrees = Penn.find_type(1, ".", " ")
Penn.all_titles = Penn.find_type(2)
Penn.all_emails = Penn.find_type(3)
Penn.all_domains = Penn.get_domains()
# Penn.find_type(1, data='self.all_domains')

Penn.degrees_types = Penn.make_unique("all_degrees")
Penn.titles_types = Penn.make_unique("all_titles")
Penn.domains_types = Penn.make_unique('all_domains')

Penn.degrees_count = Penn.count_type("degrees")
Penn.titles_count = Penn.count_type("titles")
Penn.domains_count = Penn.count_type("domains")

# PART II >>>>>>>>>
Penn.write_csv("emails.csv", "emails")

# PART III >>>>>>>>
Penn.professor_dict = Penn.make_dict()
Penn.print_dict()
