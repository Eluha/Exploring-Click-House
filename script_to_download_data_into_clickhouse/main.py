from clickhouse_driver import Client

client = Client(
    host='${HOST}',
    port='${PORT_CLICKHOUSE}',            # порт по умолчанию для native-протокола
    user='${CLICKHOUSE_USER}',
    password='${CLICKHOUSE_PASSWORD}',
    database='${DATABASE_NAME}',  # (опционально, если не 'default')
)




df = client.execute("SELECT * FROM orgs LIMIT 10")
print(df[0])