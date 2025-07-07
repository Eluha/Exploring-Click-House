import os
from dotenv import load_dotenv
load_dotenv()
from clickhouse_driver import Client


client = Client(
    host=os.getenv('HOST'),
    port=os.getenv('PORT_CLICKHOUSE'),            # порт по умолчанию для native-протокола
    user=os.getenv('CLICKHOUSE_USER'),
    password=os.getenv('CLICKHOUSE_PASSWORD'),
    database=os.getenv('DATABASE_NAME')
)




df = client.execute("""SELECT * FROM "train"."orgs" LIMIT 10""")
print(df)