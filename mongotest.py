import pymongo

client = pymongo.MongoClient("mongodb+srv://indapwaramarja:mongodb123@cluster0.ddhbgrl.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"sudhanshu",
    "email":"sudh@gmail.com",
    "surname":"kumar"
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)

