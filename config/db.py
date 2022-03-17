from sqlalchemy import create_engine, MetaData

#Conexión a la base de datos
engine = create_engine("mysql+pymysql://roberto:password@localhost:3306/storedb")

meta = MetaData() #Sólo para guardar esta propiedad

conn = engine.connect()




