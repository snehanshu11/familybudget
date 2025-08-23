from sqlalchemy import create_engine, URL, text
from sqlalchemy.orm import sessionmaker

# connection string format: driver+posstregsql://user:pass@host:port/dbname
URL = URL.create(
            drivername="postgresql+psycopg2",
            username = "postgres",
            password="password123",
            host="localhost",
            port=5432,
            database="testuser"

          )
engine = create_engine(URL, echo=True)
#engine = create_engine("postgresql+psycopg2://postgres:password123@localhost:5432/testuser", echo=True)

session_pool = sessionmaker(bind=engine, autoflush=False, autocommit=False)

#session = session_pool()
#session.execute()
#session.commit()
#session.close()

with session_pool() as session:
    result = session.execute(text("SELECT 1;"))
    print(result.scalar())  # prints 1