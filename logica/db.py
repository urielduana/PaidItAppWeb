from sqlalchemy import create_engine

def connect_to_db(user, pass_, db="paidit", plugin_db="mysql+mysqldb"):
    string_db = f"{plugin_db}://{user}:{pass_}@paiditappweb-db-1:3306/{db}"
    engine = create_engine(string_db, echo=True)
    return engine
    
    