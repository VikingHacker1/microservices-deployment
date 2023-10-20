from sqlalchemy import create_engine, MetaData
import base64

######## Prevent exposing password in plaintext in fastapi application and in config files.

# # Récupérer le mot de passe du Secret
# password_base64 = "UHJvamVjdERldm9wczIwMjMh"  # Remplacez par la valeur réelle depuis votre Secret
# password = base64.b64decode(password_base64).decode("utf-8")

# engine = create_engine(f"postgresql://admin:{password}@db:5432/storedb")
# meta = MetaData()

# conn = engine.connect()

from sqlalchemy import create_engine, MetaData

engine = create_engine("postgresql://admin:password@db:5432/storedb")

meta = MetaData()

conn = engine.connect()