from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#  executing the instruction from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# Create class-model based for the "games" table
class Video_games(base):
    __tablename__ = "Video_games"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    company = Column(String)
    genre = Column(String)


class skate_board(base):
    __tablename__ = "skate_board"
    skate_id = Column(Integer, primary_key=True)
    skate_company = Column(String)
    deck = Column(String)
    wheels = Column(String)
    trucks = Column(String)



#  instead of connection to the database directly we will ask for a session
#  create a new instancve of sessionmaker, then poit our engigne (the db)
Session = sessionmaker(db)


#  opens an actual session by calling the Session() subclass defined above
session = Session()

# create database using declarative base subclass
base.metadata.create_all(db)

# create skate record on our table
premitive = skate_board(
    skate_company="premitive",
    deck="8.5",
    wheels="spit fire",
    trucks="indy"
)


# creating games record on our table
call_of_duty = Video_games(
    name="Call of Duty",
    company="Activision",
    genre="Action"
)

crash = Video_games(
    name="Crash",
    company="naughtydog",
    genre="Adventure"
)

uncharted = Video_games(
    name="Uncharted",
    company="naughtydog",
    genre="Adventure"
)

the_last_of_us = Video_games(
    name="The Last Of Us",
    company="naughtydog",
    genre="Action"
)

# add each instance of games table to session
# session.add(call_of_duty)
# session.add(crash)
# session.add(uncharted)
# session.add(the_last_of_us)
# session.add(premitive)

# commit our session to the database
# session.commit()

# Updating a single record
# game = session.query(Video_games).filter_by(id=4)
# game.genre = "Action"


#  updatind multiple records
# gameName = session.query(Video_games)
# for gameType in gameName:
#     if gameType.genre == "Adventure":
#         gameType.genre = "Adventure/Action"
# session.commit()

# deleting a single record
fname = input("Enter game name: ")
theSkate = session.query(skate_board).filter_by(skate_company=fname).first()
# defensive programming
if theSkate is not None:
    print("skate found: ", theSkate.skate_company)
    confirmation = input("are you sure (y/n)")
    if confirmation == "y":
        session.delete(theSkate)
        session.commit()
        print("game deleted")
    else:
        print("game not deleted")


# deleting all
# games = session.query(Video_games)
# for game in games:
#     session.delete(game)
#     session.commit()


# query the database to find all games
skate = session.query(skate_board)
for skates in skate:
    print(
        skates.skate_id,
        skates.skate_company,
        skates.deck,
        skates.trucks,
        skates.wheels,
        sep=" | "
    )
