import csv
import json
rows_credits=[]
NAME="name"
JOB="job"
DIRECTOR="Director"
PRODUCER="Producer"
EX_PRODUCER="Executive Producer"
WRITER = "Writer"

TOP10=10
TOP15=15


CREDITS_ACTOR=22
CREDITS_CREW=23

MOVIES_GENRE=1
ORIGINAL_LANGUAGE=5
PRODUCTION_COMPANIES=9
PRODUCTION_COUNTRIES=10

def get_top_n(row_number,category_name,rows,n):
	"""Ejemplo
	genres_dict={}
	for row in rows_movies[1:]:
		genres=json.loads(row[MOVIES_GENRE])
		for genre in genres:
			name=str(genre[NAME])
			print name
			if(name not in genres_dict):
				genres_dict[name]=1
			else:
				genres_dict[name]+=1

	print len(genres_dict)
	top10_genres= [ (genre,genres_dict[genre]) for genre in   sorted(genres_dict, key=genres_dict.get, reverse=True)[:10]]
	print top10_genres"""
	dict_cat={}
	for row in rows[1:]:
		category=json.loads(row[row_number])
		for cat in category:
			categorizable=str(cat[category_name].encode('utf-8'))
			if(categorizable not in dict_cat):
				dict_cat[categorizable]=1
			else:
				dict_cat[categorizable]+=1
	top_n_cat= [ (categorizable,dict_cat[categorizable]) for categorizable in   sorted(dict_cat, key=dict_cat.get, reverse=True)[:n]]
	return top_n_cat

def get_top_n_no_multiple_options(row_number,rows,n):
	dict_cat={}
	for row in rows[1:]:
		categorizable=str(row[row_number].encode('utf-8'))
		if(categorizable not in dict_cat):
			dict_cat[categorizable]=1
		else:
			dict_cat[categorizable]+=1
	top_n_cat= [ (categorizable,dict_cat[categorizable]) for categorizable in   sorted(dict_cat, key=dict_cat.get, reverse=True)[:n]]
	return top_n_cat

def get_top_n_specific_second_category(row_number,category_name,second_category_name,second_category_value,rows,n):
	dict_cat={}
	for row in rows[1:]:
		category=json.loads(row[row_number])
		for cat in category:
			categorizable=str(cat[category_name].encode('utf-8'))
			second_categorizable=str(cat[second_category_name].encode('utf-8'))
			if(second_categorizable==second_category_value):
				if(categorizable not in dict_cat):
					dict_cat[categorizable]=1
				else:
					dict_cat[categorizable]+=1
	top_n_cat= [ (categorizable,dict_cat[categorizable]) for categorizable in   sorted(dict_cat, key=dict_cat.get, reverse=True)[:n]]
	return top_n_cat


with open('tmdb_5000_credits.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
   	for row in readCSV:
   		rows_credits.append(row)



rows_movies=[]
with open('tmdb_5000_movies.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
   	for row in readCSV:
   		rows_movies.append(row)

rows=[]
for r in range(len(rows_movies)):
	rows.append( rows_movies[r]+rows_credits[r])

print [ (i, rows[0][i]) for i in range(len(rows[0]))]
print "ACTORES",get_top_n(CREDITS_ACTOR,NAME,rows,TOP10)
print "GENEROS",get_top_n(MOVIES_GENRE,NAME,rows,TOP10)
print "LENGUAJE ORIGINAL",get_top_n_no_multiple_options(ORIGINAL_LANGUAGE,rows,TOP10)
print "PRODUCTORAS",get_top_n(PRODUCTION_COMPANIES,NAME,rows,TOP15)
print "PAISES PRODUCTORES",get_top_n(PRODUCTION_COUNTRIES,NAME,rows,TOP10)
print "DIRECTORS", get_top_n_specific_second_category(CREDITS_CREW,NAME,JOB,DIRECTOR,rows,TOP10)
print "PRODUCER", get_top_n_specific_second_category(CREDITS_CREW,NAME,JOB,PRODUCER,rows,TOP10)
print "EXECUTIVE PRODUCER", get_top_n_specific_second_category(CREDITS_CREW,NAME,JOB,EX_PRODUCER,rows,TOP10)
print "WRITER", get_top_n_specific_second_category(CREDITS_CREW,NAME,JOB,WRITER,rows,TOP10)