from clickhouse_driver import Client

client = Client(
    host='45.8.230.101',
    port=9000,            # порт по умолчанию для native-протокола
    user='clickhouse',
    password='Xv7@Dm2!pRq9#LaB',
    database='train',  # (опционально, если не 'default')
)




df = client.execute("SELECT * FROM orgs LIMIT 10")
print(df[0])