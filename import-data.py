import fdb

# Paths (update as needed)
backup_path = "C:/store/DBCOPY.GBK"
restore_path = "C:/store/restored_database.fdb"
output_txt = "C:/store/database_tables.txt"  # Output file

# Firebird connection credentials
user = "SYSDBA"
password = "masterkey"

# Restore the database
service = fdb.services.connect(host='localhost', user=user, password=password)
service.restore(database=restore_path, backup=backup_path)
service.close()

# Connect to the restored database
conn = fdb.connect(dsn=restore_path, user=user, password=password)
cur = conn.cursor()

# List all tables in the database
cur.execute("SELECT RDB$RELATION_NAME FROM RDB$RELATIONS WHERE RDB$SYSTEM_FLAG=0;")
tables = [table[0].strip() for table in cur.fetchall()]

# Save table names to a text file
with open(output_txt, "w", encoding="utf-8") as f:
    for table in tables:
        f.write(table + "\n")

print(f"Table names saved to: {output_txt}")

conn.close()
