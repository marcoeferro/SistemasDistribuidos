
"""
### Data Explantion

**vPv2**: Voltage from the second photovoltaic (solar panel) input.

**deviceType**: The type of device (e.g., 3 might correspond to a specific type of energy device or inverter).

**gridPower**: The amount of power being drawn from or supplied to the grid (in watts).

**loadPower**: The amount of power being consumed by the load (in watts).

**vPv1**: Voltage from the first photovoltaic (solar panel) input.

**fAcOutput**: Frequency of the AC output (in hertz).

**invStatus**: Status code of the inverter, which can indicate different operational states or errors.

**ppv2**: Power from the second photovoltaic (solar panel) input (in watts).

**vBat**: Voltage of the battery.

**loadPrecent**: Percentage of the load capacity being used.

**panelPower**: Total power being generated by the solar panels (in watts).

**batPower**: Power being charged to or discharged from the battery (in watts). A negative value typically indicates discharging.

**vAcOutput**: Voltage of the AC output.

**capacity**: Capacity of the battery (likely in percentage).

**ppv1**: Power from the first photovoltaic (solar panel) input (in watts).

**iPv1**: Current from the first photovoltaic (solar panel) input (in amperes).

**iPv2**: Current from the second photovoltaic (solar panel) input (in amperes).

**vAcInput**: Voltage of the AC input.

**fAcInput**: Frequency of the AC input (in hertz).

**iTotal**: Total current (in amperes).

**rateVA**: Apparent power (in volt-amperes).

**status**: General status code of the system, which can indicate different operational states or errors.
"""
def create_storage_status_table(connection):
    with connection as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS storage_status (
                timestamp TEXT PRIMARY KEY,
                batPower REAL,
                capacity REAL,
                deviceType INTEGER,
                fAcInput REAL,
                fAcOutput REAL,
                gridPower REAL,
                iPv1 REAL,
                iPv2 REAL,
                iTotal REAL,
                invStatus INTEGER,
                loadPower REAL,
                loadPrecent REAL,
                panelPower REAL,
                ppv1 REAL,
                ppv2 REAL,
                rateVA REAL,
                status REAL,
                vAcInput REAL,
                vAcOutput REAL,
                vBat REAL,
                vPv1 REAL,
                vPv2 REAL  

            )
        ''')
        conn.commit()

def insert_storage_status(connection,timestamp, batPower, capacity, deviceType, fAcInput, fAcOutput, gridPower, iPv1, iPv2, iTotal, invStatus, loadPower, loadPrecent, panelPower, ppv1, ppv2, rateVA, status, vAcInput, vAcOutput, vBat, vPv1, vPv2):
    with connection as conn:
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO storage_status (timestamp, batPower, capacity, deviceType, fAcInput, fAcOutput, gridPower, iPv1, iPv2, iTotal, invStatus, loadPower, loadPrecent, panelPower, ppv1, ppv2, rateVA, status, vAcInput, vAcOutput, vBat, vPv1, vPv2) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
            ''', (timestamp, batPower, capacity, deviceType, fAcInput, fAcOutput, gridPower, iPv1, iPv2, iTotal, invStatus, loadPower, loadPrecent, panelPower, ppv1, ppv2, rateVA, status, vAcInput, vAcOutput, vBat, vPv1, vPv2))
            conn.commit()
        except Exception as e:
            # Log the error or handle it in a specific way
            print(f"Error inserting Storage Status data: {e}")