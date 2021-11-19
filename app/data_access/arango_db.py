import os
from typing import List
from arango import ArangoClient

db_host = os.environ.get('DB_HOST', '')
db_name = os.environ.get('DB_NAME', '')
db_username = os.environ.get('DB_USERNAME', '')
db_password = os.environ.get('DB_PASSWORD', '')

client = ArangoClient(hosts=db_host)
db = client.db(db_name, username=db_username, password=db_password)


def get_companies() -> List:
    try:
        cursor = db.aql.execute("""
            FOR m in CompanyDimension
                RETURN {
                    _key: m._key,
                    name: m.name,
                }
        """)
        res = [x for x in cursor]
        cursor.close(ignore_missing=True)
        return res
    except:
        return []
