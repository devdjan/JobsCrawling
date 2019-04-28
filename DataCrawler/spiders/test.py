import psycopg2

hostname = 'localhost'
username = 'manager'
password = 'hrforecast'
database = 'jobs_hrforecast'

# testing, does the DB works or not
def queryJobs( conn ) :
    cur = conn.cursor()
    cur.execute( """select * from jobs_data""" )
    rows = cur.fetchall()

    for row in rows :
        print (row)

conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
queryJobs( conn )
conn.close()