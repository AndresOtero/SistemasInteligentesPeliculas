import csv
import json
rows_credits=[]
NAME="name"
JOB="job"
DIRECTOR="Director"
PRODUCER="Producer"
EX_PRODUCER="Executive Producer"
WRITER = "Writer"
FIRST=0
TOP1 =1
TOP10=10
TOP15=15
TOP20=20
TOP21=21
TOP100=100
TOP200=200
TOP1000=1000

MAX=10000
AT_LEAST_10=10
AT_LEAST_5=5
AT_LEAST_4=4
AT_LEAST_2=2
AT_LEAST_1=1
ZERO=0

CREDITS_ACTOR=22
CREDITS_CREW=23
MOVIES_GENRE=1
ORIGINAL_LANGUAGE=5
PRODUCTION_COMPANIES=9
PRODUCTION_COUNTRIES=10
AVERAGE=18
COUNT=19

#----------------------------------------NUMBER OF APPEARANCES------------------------------------

def number_of_appearances_over_total_from_top_n_to_m_in_category(row_number,category_name,rows,m,n):
	return appearances_in_list(row_number,category_name,rows,get_top_list(get_top_from_m_to_n(row_number,category_name,rows,m,n)))

def number_of_appearances_over_total_from_top_n_to_m_in_category_with_exclusion(row_number,category_name,rows,m,n,exclution_list):
	return appearances_in_list_with_exclusion(row_number,category_name,rows,get_top_list(get_top_from_m_to_n(row_number,category_name,rows,m,n)),exclution_list)

def number_of_appearances_over_total_from_top_n_to_m_in_category_no_multiples_options(row_number,rows,m,n):
	return appearances_in_list_no_multiple_options(row_number,rows,get_top_list(get_top_from_m_to_n_no_multiple_options(row_number,rows,m,n)))

def number_of_appearances_over_total_from_top_n_to_m_in_category_specific_second_category(row_number,category_name,second_category_name,second_category_value,rows,m,n):
	return appearances_in_list_specific_second_category(row_number,category_name,second_category_name,second_category_value,rows,get_top_list(get_top_from_m_to_n_specific_second_category(row_number,category_name,second_category_name,second_category_value,rows,m,n)))

def number_of_appearances_over_total_from_k_to_q_appearances_in_category_specific_second_category(row_number,category_name,second_category_name,second_category_value,rows,k,q):
	return appearances_in_list_specific_second_category(row_number,category_name,second_category_name,second_category_value,rows,get_top_list(get_from_k_to_q_appearances_specific_second_category(row_number,category_name,second_category_name,second_category_value,rows,k,q)))

def number_of_appearances_over_total_from_k_to_q_appearances_in_category_specific_second_category_with_exclusion(row_number,category_name,second_category_name,second_category_value,rows,k,q,exclution_list):
	return appearances_in_list_specific_second_category_with_exclusion(row_number,category_name,second_category_name,second_category_value,rows,get_top_list(get_from_k_to_q_appearances_specific_second_category(row_number,category_name,second_category_name,second_category_value,rows,k,q)),exclution_list)


#----------------------------------------TOP LIST------------------------------------
def get_top_list(top_n):
	return [x[0] for x in top_n]


#----------------------------------------APPEARANCES------------------------------------


def appearances_in_list(row_number,category_name,rows,top_list):
	dict_cat={}
	num=0
	total=float(len(rows))
	for row in rows[1:]:
		category=json.loads(row[row_number])
		category_list=[ str(cat[category_name].encode('utf-8')) for cat in category]
		if any([i for i in category_list if i in top_list]):
			num=num+1
	return (num/total)

def appearances_in_list_with_exclusion(row_number,category_name,rows,top_list,exclution_list):
	dict_cat={}
	num=0
	total=float(len(rows))
	for row in rows[1:]:
		category=json.loads(row[row_number])
		category_list=[ str(cat[category_name].encode('utf-8')) for cat in category]
		if any([i for i in category_list if i in top_list]) and not ( any ([i for i in category_list if i in exclution_list])):
			num=num+1
	return (num/total)

def appearances_in_list_no_multiple_options(row_number,rows,top_list):
	dict_cat={}
	num=0
	total=float(len(rows))
	for row in rows[1:]:
		categorizable=str(row[row_number].encode('utf-8'))
		if(categorizable in top_list):
			num=num+1
	return (num/total)

def appearances_in_list_specific_second_category(row_number,category_name,second_category_name,second_category_value,rows,top_list):
	dict_cat={}
	num=0
	total=float(len(rows))
	for row in rows[1:]:
		category=json.loads(row[row_number])
		category_list =[ str(cat[category_name].encode('utf-8')) for cat in category if str(cat[second_category_name].encode('utf-8'))==second_category_value]
		if any([i for i in category_list if i in top_list]):
			num=num+1
	return (num/total)

def appearances_in_list_specific_second_category_with_exclusion(row_number,category_name,second_category_name,second_category_value,rows,top_list,exclution_list):
	dict_cat={}
	num=0
	total=float(len(rows))
	for row in rows[1:]:
		category=json.loads(row[row_number])
		category_list =[ str(cat[category_name].encode('utf-8')) for cat in category if str(cat[second_category_name].encode('utf-8'))==second_category_value]
		if any([i for i in category_list if i in top_list]) and not ( any ([i for i in category_list if i in exclution_list])):
			num=num+1
	return (num/total)

#----------------------------------------GET TOP------------------------------------

def get_top_from_m_to_n(row_number,category_name,rows,m,n):
	dict_cat={}
	for row in rows[1:]:
		category=json.loads(row[row_number])
		for cat in category:
			categorizable=str(cat[category_name].encode('utf-8'))
			if(categorizable not in dict_cat):
				dict_cat[categorizable]=1
			else:
				dict_cat[categorizable]+=1
	top_n_cat= [ (categorizable,dict_cat[categorizable]) for categorizable in   sorted(dict_cat, key=dict_cat.get, reverse=True)[m:n]]
	return top_n_cat


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


#----------------------------------------GET TOP NO MULTIPLES OPTIONS------------------------------------

def get_top_from_m_to_n_no_multiple_options(row_number,rows,m,n):
	dict_cat={}
	for row in rows[1:]:
		categorizable=str(row[row_number].encode('utf-8'))
		if(categorizable not in dict_cat):
			dict_cat[categorizable]=1
		else:
			dict_cat[categorizable]+=1
	top_n_cat= [ (categorizable,dict_cat[categorizable]) for categorizable in   sorted(dict_cat, key=dict_cat.get, reverse=True)[m:n]]
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


#----------------------------------------GET TOP NO SPECIFIC SECOND CATEGORY------------------------------------


def get_top_from_m_to_n_specific_second_category(row_number,category_name,second_category_name,second_category_value,rows,m,n):
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
	top_n_cat= [ (categorizable,dict_cat[categorizable]) for categorizable in   sorted(dict_cat, key=dict_cat.get, reverse=True)[m:n]]
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

#----------------------------------------GET AT LEAST K SPECIFIC SECOND CATEGORY------------------------------------


def get_from_k_to_q_appearances_specific_second_category(row_number,category_name,second_category_name,second_category_value,rows,k,q):
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
	top_n_cat= [ (categorizable,dict_cat[categorizable]) for categorizable in   sorted(dict_cat, key=dict_cat.get, reverse=True ) if dict_cat[categorizable]>=k and dict_cat[categorizable]<=q]
	return top_n_cat



#----------------------------------------SCRIPTS------------------------------------


with open('../data/tmdb_5000_credits.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
   	for row in readCSV:
   		rows_credits.append(row)


rows_movies=[]
with open('../data/tmdb_5000_movies.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
   	for row in readCSV:
   		rows_movies.append(row)

rows=[]
for r in range(len(rows_movies)):
	rows.append( rows_movies[r]+rows_credits[r])

print rows[0]

print "---------------------ACTORES TOP 100---------------------","\n"
#print "Lista de ACTORES",get_top_list(get_top_from_m_to_n(CREDITS_ACTOR,NAME,rows,FIRST,TOP100))
print "porcentaje de peliculas con ACTORES top 100",number_of_appearances_over_total_from_top_n_to_m_in_category(CREDITS_ACTOR,NAME,rows,FIRST,TOP100)

print "\n---------------------GENEROS---------------------","\n"
DRAMA=get_top_list(get_top_from_m_to_n(MOVIES_GENRE,NAME,rows,FIRST,TOP1))
COMEDIA= get_top_list(get_top_from_m_to_n(MOVIES_GENRE,NAME,rows,1,2))
THRILLER= get_top_list(get_top_from_m_to_n(MOVIES_GENRE,NAME,rows,2,3))
print "PORCENTAJE GENEROS DRAMA",number_of_appearances_over_total_from_top_n_to_m_in_category_with_exclusion(MOVIES_GENRE,NAME,rows,FIRST,TOP1,COMEDIA+THRILLER)
print "PORCENTAJE GENEROS COMEDIA",number_of_appearances_over_total_from_top_n_to_m_in_category_with_exclusion(MOVIES_GENRE,NAME,rows,1,2,DRAMA+THRILLER)
print "PORCENTAJE GENEROS DRAMA",number_of_appearances_over_total_from_top_n_to_m_in_category_with_exclusion(MOVIES_GENRE,NAME,rows,2,3,DRAMA+COMEDIA)

print "\n---------------------LENGUAJE ORIGINAL---------------------","\n"
print "TOP1 LENGUAJE ORIGINAL",get_top_list(get_top_n_no_multiple_options(ORIGINAL_LANGUAGE,rows,1))
print "PORCENTAJE LENGUAJE ORIGINAL",number_of_appearances_over_total_from_top_n_to_m_in_category_no_multiples_options(ORIGINAL_LANGUAGE,rows,FIRST,TOP1)

print "\n---------------------PRODUCTORAS ---------------------","\n"
TOP10_PRODUCTORAS=get_top_list(get_top_from_m_to_n(PRODUCTION_COMPANIES,NAME,rows,FIRST,TOP10))
#print "PRODUCTORAS TOP 10",TOP10_PRODUCTORAS
print "PORCENTAJE  PRODUCTORAS TOP 10",number_of_appearances_over_total_from_top_n_to_m_in_category(PRODUCTION_COMPANIES,NAME,rows,FIRST,TOP10)

#print "PRODUCTORAS 11-100",get_top_list(get_top_from_m_to_n(PRODUCTION_COMPANIES,NAME,rows,11,TOP100))
print "PORCENTAJE  PRODUCTORAS TOP11-100",number_of_appearances_over_total_from_top_n_to_m_in_category_with_exclusion(PRODUCTION_COMPANIES,NAME,rows,11,TOP100,TOP10_PRODUCTORAS)

print "\n---------------------PAISES PRODUCTORES---------------------","\n"
print "PAISES PRODUCTORES",get_top_list(get_top_from_m_to_n(PRODUCTION_COUNTRIES,NAME,rows,FIRST,TOP1))
print "PAISES PRODUCTORES",number_of_appearances_over_total_from_top_n_to_m_in_category(PRODUCTION_COUNTRIES,NAME,rows,FIRST,TOP1)

print "\n---------------------DIRECTORES ---------------------","\n"
#print "DIRECTORES",get_top_list(get_from_k_to_q_appearances_specific_second_category(CREDITS_CREW,NAME,JOB,DIRECTOR,rows,AT_LEAST_5,MAX))
print "DIRECTORES AL MENOS 5 PELICULAS",number_of_appearances_over_total_from_k_to_q_appearances_in_category_specific_second_category(CREDITS_CREW,NAME,JOB,DIRECTOR,rows,AT_LEAST_5,MAX)
#print "\n---------------------DIRECTORES ENTRE 4 Y 2 PELICULAS---------------------","\n"
#prBint "DIRECTORES",get_top_list(get_from_k_to_q_appearances_specific_second_category(CREDITS_CREW,NAME,JOB,DIRECTOR,rows,AT_LEAST_2,AT_LEAST_2))
print "DIRECTORES ENTRE 4 Y 2",number_of_appearances_over_total_from_k_to_q_appearances_in_category_specific_second_category(CREDITS_CREW,NAME,JOB,DIRECTOR,rows,AT_LEAST_2,AT_LEAST_4)
#print "\n---------------------DIRECTORES CON 1 PELICULA---------------------","\n"
#print "DIRECTORES",get_top_list(get_from_k_to_q_appearances_specific_second_category(CREDITS_CREW,NAME,JOB,DIRECTOR,rows,AT_LEAST_1,AT_LEAST_1))
print "DIRECTORES CON 1 PELICULA",number_of_appearances_over_total_from_k_to_q_appearances_in_category_specific_second_category(CREDITS_CREW,NAME,JOB,DIRECTOR,rows,AT_LEAST_1,AT_LEAST_1)


print "\n---------------------PRODUCTORES---------------------","\n"
print "PELICULAS CON PRODUCTORES ",number_of_appearances_over_total_from_k_to_q_appearances_in_category_specific_second_category(CREDITS_CREW,NAME,JOB,PRODUCER,rows,0,MAX)


print "\n---------------------PRODUCTORES EJECUTIVOS---------------------","\n"
print "PELICULAS CON PRODUCTORES EJECUTIVOS",number_of_appearances_over_total_from_k_to_q_appearances_in_category_specific_second_category(CREDITS_CREW,NAME,JOB,EX_PRODUCER,rows,0,MAX)

print "\n---------------------GUIONISTA---------------------","\n"
print "PELICULAS CON GUIONISTA",number_of_appearances_over_total_from_k_to_q_appearances_in_category_specific_second_category(CREDITS_CREW,NAME,JOB,WRITER,rows,0,MAX)
"""
rows_average=[  row   for row in rows[1:] if float(row[AVERAGE]) > 7.0]
print "\n \n TOP 10 \n"
print len(rows_average)
print "ACTORES",get_top_n(CREDITS_ACTOR,NAME,rows_average,TOP10)
print "GENEROS",get_top_n(MOVIES_GENRE,NAME,rows_average,TOP15)
print "LENGUAJE ORIGINAL",get_top_n_no_multiple_options(ORIGINAL_LANGUAGE,rows_average,TOP10)
print "PRODUCTORAS",get_top_n(PRODUCTION_COMPANIES,NAME,rows_average,TOP15)
print "PAISES PRODUCTORES",get_top_n(PRODUCTION_COUNTRIES,NAME,rows_average,TOP10)
print "DIRECTORS", get_top_n_specific_second_category(CREDITS_CREW,NAME,JOB,DIRECTOR,rows_average,TOP10)
print "PRODUCER", get_top_n_specific_second_category(CREDITS_CREW,NAME,JOB,PRODUCER,rows_average,TOP10)
print "EXECUTIVE PRODUCER", get_top_n_specific_second_category(CREDITS_CREW,NAME,JOB,EX_PRODUCER,rows_average,TOP10)
print "WRITER", get_top_n_specific_second_category(CREDITS_CREW,NAME,JOB,WRITER,rows_average,TOP10)
"""