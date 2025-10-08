import oracledb

# Replace with your Oracle credentials
username = "sys"
password = "Oracle@2021"

# Try default localhost and common ports
hosts = ["localhost"]
ports = [1521]

connected = False

for host in hosts:
    for port in ports:
        # Try connecting to default service names or SID
        for service_name in ["FREEPDB1"]:
            dsn = oracledb.makedsn(host, port, service_name=service_name)
            try:
                # Explicitly specify the SYSDBA role
                conn = oracledb.connect(user=username, password=password, dsn=dsn, mode=oracledb.SYSDBA)
                cur = conn.cursor()
                cur.execute("SELECT sysdate FROM dual")
                print(f"Connected to {service_name} on {host}:{port}, sysdate:", cur.fetchone()[0])
                conn.close()
                connected = True
                break
            except oracledb.DatabaseError as e:
                print(f"Failed to connect to {service_name} on {host}:{port}:", e)
        if connected:
            break
    if connected:
        break

if not connected:
    print("Could not connect. Check your username/password/service_name.")
