import sqlite3
from datetime import datetime

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('hospital_db.sqlite')
cursor = conn.cursor()

# Create table for healthcare facility location information
cursor.execute('''
CREATE TABLE IF NOT EXISTS info_lokasi_faskes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_rs TEXT UNIQUE,
    latitude REAL,
    longitude REAL,
    alamat TEXT,
    alamat2 TEXT
)
''')

# Create table for bed information
cursor.execute('''
CREATE TABLE IF NOT EXISTS info_tempat_tidur (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_rs TEXT,
    tipe_kamar TEXT,
    total_kamar INTEGER,
    ketersediaan INTEGER,
    pria INTEGER,
    wanita INTEGER,
    last_update DATETIME,
    FOREIGN KEY (nama_rs) REFERENCES info_lokasi_faskes(nama_rs) ON DELETE CASCADE
)
''')

# Create table for booking information
cursor.execute('''
CREATE TABLE IF NOT EXISTS booking (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_rumahsakit TEXT,
    nama_pasien TEXT,
    tipe_kamar TEXT,
    FOREIGN KEY (nama_rumahsakit) REFERENCES info_lokasi_faskes(nama_rs) ON DELETE CASCADE
)
''')

# Insert example data into info_lokasi_faskes
cursor.execute('''
INSERT OR IGNORE INTO info_lokasi_faskes (nama_rs, latitude, longitude, alamat, alamat2)
VALUES 
('RSUD Beriman Balikpapan', -1.265386, 116.831239, 'Jl. Mayjen Sutoyo', 'Balikpapan, East Borneo, Indonesia'),
('Siloam Hospitals Balikpapan', -1.265842, 116.839379, 'Jl. MT Haryono', 'Balikpapan, East Borneo, Indonesia')
''')

# Insert example data into info_tempat_tidur
cursor.executemany('''
INSERT INTO info_tempat_tidur (nama_rs, tipe_kamar, total_kamar, ketersediaan, pria, wanita, last_update)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', [
    ('RSUD Beriman Balikpapan', 'VIP', 10, 5, 3, 2, datetime.now()),
    ('RSUD Beriman Balikpapan', 'Kelas 1', 20, 8, 5, 3, datetime.now()),
    ('Siloam Hospitals Balikpapan', 'Suite', 5, 2, 1, 1, datetime.now()),
    ('Siloam Hospitals Balikpapan', 'Kelas 2', 15, 10, 6, 4, datetime.now())
])

# Insert example data into booking
cursor.executemany('''
INSERT INTO booking (nama_rumahsakit, nama_pasien, gender,tipe_kamar)
VALUES (?, ?, ?)
''', [
    ('RSUD Beriman Balikpapan', 'Samsul', "Pria" ,'VIP'),
    ('Siloam Hospitals Balikpapan', 'Lisa', "Wanita",'Suite'),
    ('RSUD Beriman Balikpapan', 'Rachel', "Wanita",'Kelas 1'),
    ('Siloam Hospitals Balikpapan', 'Bobi Kartanegara', "Pria",'Kelas 2')
])

# Commit changes and close the connection
conn.commit()
conn.close()

print("Data successfully inserted into SQLite database.")
