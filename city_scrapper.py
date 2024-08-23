import requests
import psycopg2


def main():
    url = 'https://api-colombia.com/api/v1/City'
    database_conn = psycopg2.connect(
        host='ep-tight-rice-a5o1noq3.us-east-2.aws.neon.tech',
        dbname='eventdb',
        user='eventdb_owner',
        password='z6pfC1jDxJPO'
    )
    cursor = database_conn.cursor()
    cursor.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
    """)

    tablas = cursor.fetchall()

    print("Tablas en la base de datos:")
    for tabla in tablas:
        print(tabla[0])
    return
    response = requests.get(url)
    data = response.json()
    for city in data:
        cursor.execute(
            'INSERT INTO eventActorsApp_city (name) VALUES (%s)',
            (city['name'],)
        )
    database_conn.commit()
    cursor.close()
    database_conn.close()


if __name__ == '__main__':
    main()
