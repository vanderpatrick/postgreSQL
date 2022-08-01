from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# Executing the instruction from our localhost "chinnok" db
db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# create variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# Create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
) 

# making connection
with db.connect() as connection:
    # QUery 1 - select all records from the "artist" table
    # select_query = artist_table.select()

    # Query 2 - select only the name column from the artist table
    # select_query = artist_table.select().with_only_columns([artist_table.c.Name])

    # Query 3 - select only "queen" from the artist table
    # select_query = artist_table.select().where(artist_table.c.Name == "Queen")

    # query 4 - select only by artistid from the artist table
    # select_query = artist_table.select().where(artist_table.c.ArtistId == 51)

    # query 5 - select only by albumid from the artist table
    # select_query = artist_table.select().where(album_table.c.AlbumId == 51)

    # query 6 -seleect all tracks where the composer is queen from track table
    select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)
