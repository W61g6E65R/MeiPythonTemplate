# import.general
import logging

# import.project
from sqlalchemy import create_engine, text, url
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy.exc import SQLAlchemyError, OperationalError
import time

Base = declarative_base()

class DatabaseConnector:
    """
    _summary_
    """    
    def __init__(self, db_type: str, user: str = '', password: str = '', host: str = '', port: str = '', db_name: str = '', retries: int = 3, retry_delay: float = 2.0):
        """
        _summary_

        Arguments:
            db_type -- _description_

        Keyword Arguments:
            user -- _description_ (default: {''})
            password -- _description_ (default: {''})
            host -- _description_ (default: {''})
            port -- _description_ (default: {''})
            db_name -- _description_ (default: {''})
            retries -- _description_ (default: {3})
            retry_delay -- _description_ (default: {2.0})
        """        
        self.__log = logging.getLogger(__name__)
        self.db_type = db_type
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db_name = db_name
        self.engine = None
        self.SessionLocal = None
        self.retries = retries
        self.retry_delay = retry_delay

        self._build_engine_with_retries()

    def _build_engine(self):
        if self.db_type == "sqlite":
            connection_url = f"sqlite:///{self.db_name}"

        elif self.db_type == "postgresql":
            # psycopg v3!
            connection_url = f"postgresql+psycopg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"

        elif self.db_type == "mysql":
            connection_url = f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}"

        elif self.db_type == "mssql":
            connection_url = URL.create(
                "mssql+pyodbc",
                username=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.db_name,
                query={"driver": "ODBC Driver 17 for SQL Server"} 
            )

        else:
            raise ValueError(f"Unsupported database type: {self.db_type}")

        self.engine = create_engine(connection_url, echo=False, future=True)
        self.SessionLocal = sessionmaker(bind=self.engine, autoflush=False, autocommit=False, future=True)


    def _build_engine_with_retries(self):
        attempt = 0
        while attempt < self.retries:
            try:
                self._build_engine()
                with self.engine.connect() as conn:
                    conn.execute(text("SELECT 1"))
                return
            except OperationalError as e:
                attempt += 1
                self.__log.warning(f"Could not connect to database (Attempt {attempt}/{self.retries}): {e}")
                time.sleep(self.retry_delay)
        raise ConnectionError("Could not connect to database")

    def get_session(self) -> Session:
        return self.SessionLocal()

    def execute_raw(self, query: str, params: dict = None):
        try:
            with self.engine.connect() as conn:
                result = conn.execute(text(query), params or {})
                return result.fetchall()
        except SQLAlchemyError as e:
            self.__log.error(f"Query failed: {e}")
            return None

    def create_tables(self):
        Base.metadata.create_all(bind=self.engine)

    def drop_tables(self):
        Base.metadata.drop_all(bind=self.engine)
