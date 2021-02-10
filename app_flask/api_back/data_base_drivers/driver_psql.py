import psycopg2
from psycopg2 import sql
from psycopg2.extras import DictCursor


def get_tables_from_database(ip, port, login, pswd, database, table_filter=None):
    """
    Получет схему метаданных для конкретной базы данных
    :param ip:
    :param port:
    :param login:
    :param pswd:
    :param database:
    :return:
    """

    sql_pattern = """
    SELECT * FROM
    information_schema.tables as tables
    LEFT
    JOIN
    INFORMATION_SCHEMA.COLUMNS as columns
    ON
    tables.table_name = columns.table_name
    WHERE
    tables.table_schema = 'public'
    <table_filter>
    """

    if table_filter:
        sql_filter_table = ""
        for table_name in table_filter:
            sql_filter_table = sql_filter_table + table_name + ','

        sql_filter_table = sql_filter_table[:-1]

        sql_pattern = sql_pattern.replace('<table_filter>', f'and tables.table_name IN ({sql_filter_table})')
    else:
        sql_pattern = sql_pattern.replace('<table_filter>', '')

    with psycopg2.connect(dbname=database, user=login, password=pswd, host=ip, port=port) as conn:
        with conn.cursor(cursor_factory=DictCursor) as cursor:
            cursor.execute(sql.SQL(sql_pattern))
            records = cursor.fetchall()
            return records
