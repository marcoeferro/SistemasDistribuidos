from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Función para conectarse a la base de datos SQLite
def get_db_connection():
    conn = sqlite3.connect('./../scrapped_data.db')
    conn.row_factory = sqlite3.Row  # Permite acceder a las filas como diccionarios
    return conn

# Ruta para obtener datos de la tabla "device_data"
@app.route('/DeviceData', methods=['GET'])
def get_device_data():
    conn = get_db_connection()
    device_data = conn.execute('SELECT * FROM device_data').fetchall()
    conn.close()
    return jsonify([dict(row) for row in device_data])

# Ruta para obtener datos de la tabla "anergy_area_chart"
@app.route('/EnergyAreaChart', methods=['GET'])
def get_energy_area_chart():
    conn = get_db_connection()
    energy_area_chart = conn.execute('SELECT * FROM anergy_area_chart').fetchall()
    conn.close()
    return jsonify([dict(row) for row in energy_area_chart])

# Ruta para obtener datos de la tabla "energy_storage_day"
@app.route('/EnergyStorageDay', methods=['GET'])
def get_energy_storage_day():
    conn = get_db_connection()
    energy_storage_day = conn.execute('SELECT * FROM energy_storage_day').fetchall()
    conn.close()
    return jsonify([dict(row) for row in energy_storage_day])

# Ruta para obtener datos de la tabla "plant"
@app.route('/Plant', methods=['GET'])
def get_plant():
    conn = get_db_connection()
    plant = conn.execute('SELECT * FROM plant').fetchall()
    conn.close()
    return jsonify([dict(row) for row in plant])

# Ruta para obtener datos de la tabla "storage_status"
@app.route('/StorageStatus', methods=['GET'])
def get_storage_status():
    conn = get_db_connection()
    storage_status = conn.execute('SELECT * FROM storage_status').fetchall()
    conn.close()
    return jsonify([dict(row) for row in storage_status])

# Ruta para obtener datos de la tabla "storage_total"
@app.route('/StorageTotal', methods=['GET'])
def get_storage_total():
    conn = get_db_connection()
    storage_total = conn.execute('SELECT * FROM storage_total').fetchall()
    conn.close()
    return jsonify([dict(row) for row in storage_total])

# Ruta para obtener datos de la tabla "wheater"
@app.route('/Wheater', methods=['GET'])
def get_wheater():
    conn = get_db_connection()
    wheater = conn.execute('SELECT * FROM wheater').fetchall()
    conn.close()
    return jsonify([dict(row) for row in wheater])

# Ruta para obtener datos de la tabla "battery_charge_discharge"
@app.route('/BatteryCharge', methods=['GET'])
def get_battery_charge():
    conn = get_db_connection()
    battery_charge = conn.execute('SELECT * FROM battery_charge_discharge').fetchall()
    conn.close()
    return jsonify([dict(row) for row in battery_charge])

# Ruta para obtener datos de la tabla "battery_soc_info"
@app.route('/BatterySoc', methods=['GET'])
def get_battery_soc():
    conn = get_db_connection()
    battery_soc = conn.execute('SELECT * FROM battery_soc_info').fetchall()
    conn.close()
    return jsonify([dict(row) for row in battery_soc])

if __name__ == '__main__':
    app.run(debug=True)
