import sqlite3

def add_application(job_id, application):
    connection = sqlite3.connect('careers_db.db')
    cursor = connection.cursor()
    
    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_id INTEGER NOT NULL,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL,
            linkedin_url TEXT,
            education TEXT,
            experience TEXT
        )
    ''')
    
    # Insert the application into the table
    cursor.execute('''
        INSERT INTO applications (job_id, full_name, email, linkedin_url, education, experience)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        job_id,
        application.get('full_name'),
        application.get('email'),
        application.get('linkedin_url', ''),
        application.get('education', ''),
        application.get('experience', '')
    ))
    
    connection.commit()
    connection.close()