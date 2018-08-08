import numpy as np
import pandas as pd
import gc
import psycopg2


def process_partD(path, year):
    '''
    Input: source path to raw file and year
    Process: import table as a pd.DatafFrame and add `year` column
    Output: pd.DatafFrame
    '''
    chunksize = 10 ** 6
    chunks_df = []
    for chunk in pd.read_csv(path, sep="\t", low_memory=False, chunksize=chunksize):
        # append a year column
        chunk['year'] = pd.Series([year] * len(chunk))
        chunks_df.append(chunk)
    df = pd.concat(chunks_df, axis=0)
    return df


def build_medicare_partD_table(user, host, dbname):
    # connect to the database
    from sqlalchemy import create_engine
    sql_string = 'postgresql+psycopg2://{}:@{}/{}'.format(user, host, dbname)
    engine = create_engine(sql_string, echo=True)
    connection = engine.connect()

    # create a `medicare_part_d` table
    from sqlalchemy.ext.declarative import declarative_base
    Base = declarative_base()

    from sqlalchemy import Column, Integer, String, Float
    class medicare_part_d(Base):
        __tablename__ = 'medicare_part_d'

        id = Column(Integer, primary_key=True, autoincrement=True)
        npi = Column(String(10))
        nppes_provider_last_org_name = Column(String(128))
        nppes_provider_first_name = Column(String(32))
        nppes_provider_city = Column(String(32))
        nppes_provider_state = Column(String(2))
        specialty_description = Column(String(128))
        description_flag = Column(String(1))
        drug_name = Column(String(32))
        generic_name = Column(String(32))
        bene_count = Column(Float)
        total_claim_count = Column(Float)
        total_30_day_fill_count = Column(Float)
        total_day_supply = Column(Float)
        total_drug_cost = Column(Float)
        bene_count_ge65 = Column(Float)
        bene_count_ge65_suppress_flag = Column(String(1))
        total_claim_count_ge65 = Column(Float)
        ge65_suppress_flag = Column(String(1))
        total_30_day_fill_count_ge65 = Column(Float)
        total_day_supply_ge65 = Column(Float)
        total_drug_cost_ge65 = Column(Float)
        year = Column(Float)

    # create a schema
    Base.metadata.create_all(engine)
    connection.close()

def csv2sql(host, port, dbname, user, fpath, table_name):
    '''
    This function uploads a csv file to a target table in the database
    '''
    conn_string = "host='{}' port='{}' dbname='{}' user='{}'" \
        .format(host, port, dbname, user)
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    f = open(r'{}'.format(fpath), 'r')
    # Truncate the table first
    # cur.execute("Truncate {} Cascade;".format(table_name))
    # Load table from the file with header
    cur.copy_expert("copy {} from STDIN CSV HEADER QUOTE '\"'".format(table_name), f)
    cur.execute("commit;")
    f.close()
    conn.close()


def sql_query(host, port, dbname, user, query_str):
    '''
    This function creates a pd.DataFrame from a SQL query
    '''
    conn_string = "host='{}' port='{}' dbname='{}' user='{}'" \
        .format(host, port, dbname, user)
    conn = psycopg2.connect(conn_string)
    df = pd.read_sql(query_str, conn)
    conn.close()
    return df

