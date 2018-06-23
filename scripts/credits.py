import csv
import json
from datetime import *
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

BUDGET=0
CREDITS_ID=20
CREDITS_TITLE=21
CREDITS_ACTOR=22
CREDITS_CREW=23
MOVIES_GENRE=1
ORIGINAL_LANGUAGE=5
PRODUCTION_COMPANIES=9
PRODUCTION_COUNTRIES=10
AVERAGE=18
COUNT=19
POPULARITY=8
RELEASE_DATE=11
REVENUE=12
RUNTIME=13

CATEGORY_RANGE=0
CATEGORY=1
DATA_MISSING=2

ROW_NUMBER=0
CATEGORY_NAME=1
TOP_LIST=2
EXCLUSION_LIST=3
ROW_NAME=4
SECOND_CATEGORY_NAME=5
SECOND_CATEGORY_VALUE=6
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

#----------------------------------------APPEAR IN LIST------------------------------------
def appear_in_list(row_number,category_name,row,top_list,exclution_list,second_category_name,second_category_value):
	if second_category_name is not None:
		category = json.loads(row[row_number])
		category_list = [str(cat[category_name].encode('utf-8')) for cat in category if
						 str(cat[second_category_name].encode('utf-8')) == second_category_value]
		return any([i for i in category_list if i in top_list])
	if category_name is None:
		categorizable = str(row[row_number].encode('utf-8'))
		return (categorizable in top_list)
	else:
		category = json.loads(row[row_number])
		category_list = [str(cat[category_name].encode('utf-8')) for cat in category]
		if exclution_list is None:
			return any([i for i in category_list if i in top_list])
		else:
			return  any([i for i in category_list if i in top_list]) and not ( any ([i for i in category_list if i in exclution_list]))

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

tamanio=len(rows)-1
rangos=[ [ tamanio*i/4  ,tamanio*(i+1)/4 ] for i in range(0,4)]

rangos[3][1]=rangos[3][1]-1

rangos3=[[(tamanio*i)/3  ,(tamanio*(i+1))/3 ] for i in range(0,3)]
rangos3[2][1]-=1
"""Arreglo de datos """
correct_rows=[]
for r in rows[1:]:
	if r[RELEASE_DATE]=="":
		r[RELEASE_DATE]="2015-3-1"
	if r[AVERAGE]=="0":
		print  "ojo"
ranges=[]
specific_category_lists=[]
specific_category_ranges=[]
class_range=[]

print  "\n","---------------------AVERAGE VOTE---------------------","\n"
average_list= sorted([ float(r[AVERAGE]) for r in rows[1:]])
#average_range_values=[ (average_list[x[0]],average_list[x[1]]) for x in rangos3]
average_range_values=[[0.0,6.0],[6.0,8.0],[8.0,10.0]]
print "rangos de valores",average_range_values
class_range.append([average_range_values,AVERAGE,False])

print  "\n","---------------------BUDGET---------------------","\n"
print "FALTA INFORMACION EN ALGUNAS PELICULAS"
budget_list= sorted([ float(r[BUDGET]) for r in rows[1:]])
budget_range_values=[ (budget_list[x[0]],budget_list[x[1]]) for x in rangos3]
print "rangos de valores",budget_range_values
ranges.append([budget_range_values,BUDGET,True])


print  "\n","---------------------POPULARIDAD---------------------","\n"
popularity_list= sorted([ float(r[POPULARITY]) for r in rows[1:]])
popularity_range_values=[ (popularity_list[x[0]],popularity_list[x[1]]) for x in rangos]
print "rangos de valores",popularity_range_values
ranges.append([popularity_range_values,POPULARITY,False])

print  "\n","---------------------FECHA DE ESTRENO---------------------","\n"
for r in rows[1:]:
	r[RELEASE_DATE]= date(int(str(r[RELEASE_DATE]).split("-")[0]),int(str(r[RELEASE_DATE]).split("-")[1]),int(str(r[RELEASE_DATE]).split("-")[2]))
release_date_list= sorted([r[RELEASE_DATE] for r in rows[1:] if r[RELEASE_DATE]!=""])
release_date_range_values=[ (release_date_list[x[0]],release_date_list[x[1]]) for x in rangos]
print "rangos de valores",release_date_range_values
ranges.append([release_date_range_values,RELEASE_DATE,False])

print  "\n","---------------------REVENUE--------------------","\n"
print "FALTA INFORMACION EN ALGUNAS PELICULAS"
revenue_list= sorted([ float(r[REVENUE]) for r in rows[1:] ])
revenue_range_values=[ (revenue_list[x[0]],revenue_list[x[1]]) for x in rangos3]
print "rangos de valores",revenue_range_values
ranges.append([revenue_range_values,REVENUE,True])


def change(f):
	if (f==""):
		return float(0)
	else:
		return float(f)

print  "\n","---------------------RUNTIME--------------------","\n"
print "FALTA INFORMACION EN ALGUNAS PELICULAS"
for r in rows[1:]:
	r[RUNTIME]=change(r[RUNTIME])
runtime_list= sorted([ r[RUNTIME] for r in rows[1:] ])
runtime_range_values=[ (runtime_list[x[0]],runtime_list[x[1]]) for x in rangos3]
print "rangos de valores",runtime_range_values
ranges.append([runtime_range_values,RUNTIME,True])



print "\n","---------------------ACTORES TOP 100---------------------","\n"
#print "Lista de ACTORES",get_top_list(get_top_from_m_to_n(CREDITS_ACTOR,NAME,rows,FIRST,TOP100))
print "porcentaje de peliculas con ACTORES top 100",number_of_appearances_over_total_from_top_n_to_m_in_category(CREDITS_ACTOR,NAME,rows,FIRST,TOP100)
top_list_actor=get_top_list( get_top_from_m_to_n(CREDITS_ACTOR,NAME,rows,FIRST,TOP100))
specific_category_lists.append([CREDITS_ACTOR,NAME,top_list_actor,None,"TOP 100 ACTOR"])

print "\n---------------------GENEROS---------------------","\n"
DRAMA=get_top_list(get_top_from_m_to_n(MOVIES_GENRE,NAME,rows,FIRST,TOP1))
COMEDIA= get_top_list(get_top_from_m_to_n(MOVIES_GENRE,NAME,rows,1,2))
THRILLER= get_top_list(get_top_from_m_to_n(MOVIES_GENRE,NAME,rows,2,3))
GENRES=get_top_list(get_top_from_m_to_n(MOVIES_GENRE,NAME,rows,FIRST,TOP100))
print "PORCENTAJE GENEROS DRAMA",number_of_appearances_over_total_from_top_n_to_m_in_category(MOVIES_GENRE,NAME,rows,FIRST,TOP1)
print "PORCENTAJE GENEROS COMEDIA",number_of_appearances_over_total_from_top_n_to_m_in_category_with_exclusion(MOVIES_GENRE,NAME,rows,1,2,DRAMA)
print "PORCENTAJE GENEROS THRILLER",number_of_appearances_over_total_from_top_n_to_m_in_category_with_exclusion(MOVIES_GENRE,NAME,rows,2,3,DRAMA+COMEDIA)
for genre in GENRES:
	specific_category_lists.append([MOVIES_GENRE, NAME, genre, None, genre])


print "\n---------------------LENGUAJE ORIGINAL---------------------","\n"
top_language=get_top_list(get_top_n_no_multiple_options(ORIGINAL_LANGUAGE,rows,1))
print "TOP1 LENGUAJE ORIGINAL",top_language
print "PORCENTAJE LENGUAJE ORIGINAL",number_of_appearances_over_total_from_top_n_to_m_in_category_no_multiples_options(ORIGINAL_LANGUAGE,rows,FIRST,TOP1)
specific_category_lists.append([ORIGINAL_LANGUAGE,None,top_language,None,"English"])


print "\n---------------------PRODUCTORAS ---------------------","\n"
TOP10_PRODUCTORAS=get_top_list(get_top_from_m_to_n(PRODUCTION_COMPANIES,NAME,rows,FIRST,TOP10))
TOP11_100_PRODUCTORAS=get_top_list(get_top_from_m_to_n(PRODUCTION_COMPANIES,NAME,rows,11,TOP100))

print "PRODUCTORAS TOP 10",TOP10_PRODUCTORAS
print "PORCENTAJE  PRODUCTORAS TOP 10",number_of_appearances_over_total_from_top_n_to_m_in_category(PRODUCTION_COMPANIES,NAME,rows,FIRST,TOP10)

print "PRODUCTORAS 11-100",TOP11_100_PRODUCTORAS
print "PORCENTAJE  PRODUCTORAS TOP11-100",number_of_appearances_over_total_from_top_n_to_m_in_category_with_exclusion(PRODUCTION_COMPANIES,NAME,rows,11,TOP100,TOP10_PRODUCTORAS)

specific_category_ranges.append([PRODUCTION_COMPANIES,NAME,[TOP10_PRODUCTORAS,TOP11_100_PRODUCTORAS],None,"PRODUCTORAS"])


print "\n---------------------PAISES PRODUCTORES---------------------","\n"
top_country=get_top_list(get_top_from_m_to_n(PRODUCTION_COUNTRIES,NAME,rows,FIRST,TOP1))
print "PAISES PRODUCTORES",top_country
print "PAISES PRODUCTORES",number_of_appearances_over_total_from_top_n_to_m_in_category(PRODUCTION_COUNTRIES,NAME,rows,FIRST,TOP1)
specific_category_lists.append([PRODUCTION_COUNTRIES,NAME,top_country,None,"USA"])

print "\n---------------------DIRECTORES ---------------------","\n"
DIRECTOR_AL_MENOS_5=get_top_list(get_from_k_to_q_appearances_specific_second_category(CREDITS_CREW,NAME,JOB,DIRECTOR,rows,AT_LEAST_5,MAX))
print "DIRECTORES",DIRECTOR_AL_MENOS_5
print "DIRECTORES AL MENOS 5 PELICULAS",number_of_appearances_over_total_from_k_to_q_appearances_in_category_specific_second_category(CREDITS_CREW,NAME,JOB,DIRECTOR,rows,AT_LEAST_5,MAX)
print "\n---------------------DIRECTORES ENTRE 4 Y 2 PELICULAS---------------------","\n"


DIRECTOR_AL_MENOS_4_2=get_top_list(get_from_k_to_q_appearances_specific_second_category(CREDITS_CREW,NAME,JOB,DIRECTOR,rows,AT_LEAST_2,AT_LEAST_4))
print "DIRECTORES",DIRECTOR_AL_MENOS_4_2
print "DIRECTORES ENTRE 4 Y 2",number_of_appearances_over_total_from_k_to_q_appearances_in_category_specific_second_category(CREDITS_CREW,NAME,JOB,DIRECTOR,rows,AT_LEAST_2,AT_LEAST_4)
print "\n---------------------DIRECTORES CON 1 PELICULA---------------------","\n"

DIRECTOR_CON_1_PELICULA= get_top_list(get_from_k_to_q_appearances_specific_second_category(CREDITS_CREW,NAME,JOB,DIRECTOR,rows,AT_LEAST_1,AT_LEAST_1))
print "DIRECTORES",DIRECTOR_CON_1_PELICULA
print "DIRECTORES CON 1 PELICULA",number_of_appearances_over_total_from_k_to_q_appearances_in_category_specific_second_category(CREDITS_CREW,NAME,JOB,DIRECTOR,rows,AT_LEAST_1,AT_LEAST_1)

specific_category_ranges.append([CREDITS_CREW,NAME,[DIRECTOR_AL_MENOS_5,DIRECTOR_AL_MENOS_4_2,DIRECTOR_CON_1_PELICULA],None,"DIRECTORES",JOB,DIRECTOR])

print "\n---------------------PRODUCTORES---------------------","\n"
top_productores=get_top_list(get_from_k_to_q_appearances_specific_second_category(CREDITS_CREW,NAME,JOB,PRODUCER,rows,5,MAX))
print "PRODUCTORES CON AL MENOS 5 PELICULAS",top_productores
print "PELICULAS CON PRODUCTORES CON AL MENOS 5 PELICULAS ",number_of_appearances_over_total_from_k_to_q_appearances_in_category_specific_second_category(CREDITS_CREW,NAME,JOB,PRODUCER,rows,5,MAX)
specific_category_lists.append([CREDITS_CREW,NAME,top_productores,None,"Productores con al menos 5 peliculas",JOB,PRODUCER])



"""
print "\n---------------------PRODUCTORES EJECUTIVOS---------------------","\n"
print "PELICULAS CON PRODUCTORES EJECUTIVOS",number_of_appearances_over_total_from_k_to_q_appearances_in_category_specific_second_category(CREDITS_CREW,NAME,JOB,EX_PRODUCER,rows,0,MAX)

print "\n---------------------GUIONISTA---------------------","\n"
print "PELICULAS CON GUIONISTA",number_of_appearances_over_total_from_k_to_q_appearances_in_category_specific_second_category(CREDITS_CREW,NAME,JOB,WRITER,rows,0,MAX)


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
def change_bool_for_int(bool):
    if bool==True:
        return 1
    else:
        return 0

new_rows=[ [r[CREDITS_ID]] for r in rows]
for i in range(0, len(new_rows)):
    row = rows[i]
    new_row = new_rows[i]
    for rango in ranges:
        range_category = rango[CATEGORY_RANGE]
        name_category = rango[CATEGORY]
        data_missing = rango[DATA_MISSING]
        if (i == 0):
            new_row.append(row[name_category])
            continue
        for j in range(0, len(range_category)):
            low_limit = range_category[j][0]
            high_limit = range_category[j][1]

            value = row[name_category]
            if name_category != RELEASE_DATE:
                value = float(row[name_category])
                if j == len(range_category) - 1:
                    high_limit+=1.0
            else:
                if j == len(range_category) - 1:
                    high_limit+=timedelta(days=1)
            if value == 0 and data_missing:
                new_row.append(3)
                break

            if (low_limit <= value) and (high_limit > value):
                new_row.append(j)
                break
    for specific_category_list in specific_category_lists:
        row_number = specific_category_list[ROW_NUMBER]
        category_name = specific_category_list[CATEGORY_NAME]
        top_list = specific_category_list[TOP_LIST]
        exclusion_list = specific_category_list[EXCLUSION_LIST]
        second_category_name = None
        second_category_value = None
        if (len(specific_category_list) == 7):
            second_category_name = specific_category_list[SECOND_CATEGORY_NAME]
            second_category_value = specific_category_list[SECOND_CATEGORY_VALUE]
        if (i == 0):
            new_row.append(specific_category_list[ROW_NAME])
            continue
        new_row.append(change_bool_for_int(appear_in_list(row_number, category_name, row, top_list, None, None, None)))

    for specific_category_range in specific_category_ranges:
        row_number = specific_category_range[ROW_NUMBER]
        category_name = specific_category_range[CATEGORY_NAME]
        lists = specific_category_range[TOP_LIST]
        second_category_name = None
        second_category_value = None
        if (len(specific_category_range) == 7):
            second_category_name = specific_category_range[SECOND_CATEGORY_NAME]
            second_category_value = specific_category_range[SECOND_CATEGORY_VALUE]
        if (i == 0):
            new_row.append(specific_category_range[ROW_NAME])
            continue
        selected = False
        for j in range(len(lists)):
            category_list = lists[j]
            other_categories = [x for x in lists if x != category_list]
            exclusion_list = lists[:j - 1]
            if appear_in_list(row_number, category_name, row, category_list, exclusion_list, second_category_name,
                              second_category_value):
                selected = True
                new_row.append(j)
                break
        if not selected:
            new_row.append(len(lists))

    for rango in class_range:
        range_category = rango[CATEGORY_RANGE]
        name_category = rango[CATEGORY]
        data_missing = rango[DATA_MISSING]
        if (i == 0):
            new_row.append(row[name_category])
            continue
        for j in range(0, len(range_category)):
            low_limit = range_category[j][0]
            high_limit = range_category[j][1]
            value = float(row[name_category])
            if j == len(range_category) - 1:
	            high_limit+=1.0

            if (low_limit <= value) and (high_limit > value):
                new_row.append("Clase"+str(j))
                break


largo=len(new_rows[0])
errores=0
for row in new_rows:
    if len(row)!=largo:

        print "ERROR" ,row
        print len(row), largo
        errores= errores+1
print "ERRORES",errores

resultFile = open("processed_data.csv",'wb')
wr = csv.writer(resultFile, dialect='excel')
for item in new_rows:
    wr.writerow(item)