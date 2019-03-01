import csv

with open('out.csv', 'w') as csvfile:
	filewriter = csv.writer(csvfile, delimiter=',',
		quotechar='|', quoting=csv.QUOTE_MINIMAL)
	filewriter.writerow(['sens_1', '2000', '1000'])
	filewriter.writerow(['sens_2', '3000', '3000'])