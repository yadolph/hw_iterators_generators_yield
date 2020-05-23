import json


class WikiCountry:
	def __init__(self,input_file,output_file):
		self.num = -1
		self.input_file = input_file
		self.output_file = output_file

		with open(self.input_file) as f:
			self.countries = json.load(f)

		self.end = len(self.countries)

	def __iter__(self):
		return self

	def __next__(self):
		self.num += 1
		if self.num < self.end:
			country = self.countries[self.num]['translations']['rus']['common']
			country_link = 'https://ru.wikipedia.org/wiki/' + country.replace(' ' , '_')
			with open(self.output_file, 'a') as f:
				f.write(f'{country} - {country_link}\n')
				
		else:
			print(f'Ссылки записаны в файл {self.output_file}')
			raise StopIteration
		

for country in WikiCountry('countries.json','links.txt'):
	pass 