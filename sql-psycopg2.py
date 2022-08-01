import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

#  build a cursosr object of the database
cursor = connection.cursor()

# Query 1 - select all records from the "artits" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Quenn" from "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])

# QUery 4 - select only by "artistID" #51 from the "artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Fretwork"])

# Query 5 - select only the albums with "ArtistID" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 6 - select all tracks where the composer is "Queen" from the
#  "track"table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" =%s', ["test"])

# fetch the results (multiples)
results = cursor.fetchall()

# fetch the result (single)
# results = cursor.fetchone()

# close the connection
connection.close()

# print results
for result in results:
    print(result)