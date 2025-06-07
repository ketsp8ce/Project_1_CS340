from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'a18VILlA9G'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31580
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.animals = self.database[COL]

# Create method (C in CRUD)
#Inserts a document into the 'animals' collection, returns true on success
    def create(self, data):
        if data is not None:
            try:
                result = self.animals.insert_one(data) #data should be dictionary
                print(f"debug: inserted document with id: {result.inserted_id}")
                return result.acknowledged
            except Exception as e:
                print(f"Error: insert failed - {str(e)}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Read method (R in CRUD)
#Queries documents and returns a list of content or an empty list if fails
    def read(self, query):
        try:
            cursor=self.animals.find(query)
            return list(cursor) #convert cursor to list of documents
        except Exception as e:
            print(f"Query failed: {e}") #error message
            return[] #return empty list
