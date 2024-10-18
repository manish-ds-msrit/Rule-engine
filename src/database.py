import psycopg2

def get_connection():
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_username",
        password="your_password",
        host="localhost",
        port="5432"
    )
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rules (
            id SERIAL PRIMARY KEY,
            rule_name VARCHAR(255),
            rule_ast JSONB
        );
    ''')
    conn.commit()
    cursor.close()
    conn.close()
