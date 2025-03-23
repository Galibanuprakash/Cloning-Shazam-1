import sqlite3
import zlib
import pandas as pd

def extract_subtitles(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Get the actual table name dynamically
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' LIMIT 1;")
    table_name = cursor.fetchone()[0]
    print(f"Using table: {table_name}")
    
    query = f"SELECT num, name, content FROM {table_name};"
    subtitle_data = cursor.execute(query).fetchall()
    conn.close()
    
    subtitle_list = []
    for num, name, content in subtitle_data:
        try:
            decompressed_content = zlib.decompress(content).decode('latin-1')
        except zlib.error:
            decompressed_content = content.decode('latin-1')
        subtitle_list.append((num, name, decompressed_content))
    
    df = pd.DataFrame(subtitle_list, columns=["ID", "File Name", "Content"])
    df.to_csv("data/subtitle_data.csv", index=False)
    print("Data extraction complete!")

extract_subtitles("data/eng_subtitles_database.db")