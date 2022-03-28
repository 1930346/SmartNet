from sqlalchemy import create_engine, MetaData
import databases

#Conexión a la base de datos
# engine = create_engine("mysql+pymysql://roberto:password@localhost:3306/storedb")
DATABASE_URL = "mysql+pymysql://roberto:password@localhost:3306/storedb"
database = databases.Database(DATABASE_URL)

meta = MetaData() #Sólo para guardar esta propiedad
engine = create_engine(DATABASE_URL)
conn = engine.connect()




