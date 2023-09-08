def isLeafYear(year):
 if ( year % 4==0 and year % 100!=0) or year % 400==0:
  return True
 else:
  return False
  
year=int(input("Enter year to be checked:"))

if isLeafYear(year):
 print('{} is a leaf  year.'.format(year))
else:
 print('{} is not leaf year.'.format(year))
