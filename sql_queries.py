# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (
                                songplay_id SERIAL PRIMARY KEY, 
                                start_time TIMESTAMP NOT NULL, 
                                user_id INT NOT NULL, 
                                level VARCHAR(4), 
                                song_id VARCHAR, 
                                artist_id VARCHAR, 
                                session_id INT NOT NULL, 
                                location TEXT, 
                                user_agent TEXT
                            )
                        """)
    
user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
                            user_id INT UNIQUE NOT NULL PRIMARY KEY, 
                            first_name TEXT, 
                            last_name TEXT, 
                            gender VARCHAR(1), 
                            level VARCHAR(4)
                        )
                    """)

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
                            song_id VARCHAR UNIQUE NOT NULL PRIMARY KEY, 
                            title TEXT, 
                            artist_id VARCHAR, 
                            year INT, 
                            duration NUMERIC
                        )
                    """)

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
                            artist_id VARCHAR UNIQUE NOT NULL PRIMARY KEY, 
                            name TEXT, 
                            location TEXT, 
                            latitude NUMERIC, 
                            longitude NUMERIC
                          )
                      """)

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
                            start_time TIME UNIQUE NOT NULL, 
                            hour INT, 
                            day INT, 
                            week INT, 
                            month VARCHAR(10), 
                            year INT, 
                            weekday VARCHAR(10)
                        )
                    """)

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (
                                start_time, 
                                user_id, 
                                level, 
                                song_id, 
                                artist_id, 
                                session_id, 
                                location, 
                                user_agent
                            ) 
                            VALUES (to_timestamp(%s), %s, %s, %s, %s, %s, %s, %s)
                        """)

user_table_insert = ("""INSERT INTO users (
                            user_id, 
                            first_name, 
                            last_name, 
                            gender, 
                            level
                        ) 
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (user_id) 
                            DO UPDATE SET level = EXCLUDED.level
                    """)

song_table_insert = ("""INSERT INTO songs (
                            song_id, 
                            title, 
                            artist_id, 
                            year, 
                            duration
                        ) 
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (song_id) 
                            DO NOTHING
                    """)

artist_table_insert = ("""INSERT INTO artists (
                              artist_id, 
                              name, 
                              location, 
                              latitude, 
                              longitude
                          ) 
                          VALUES (%s, %s, %s, %s, %s)
                          ON CONFLICT (artist_id) 
                              DO NOTHING
                      """)

time_table_insert = ("""INSERT INTO time (
                            start_time, 
                            hour, 
                            day, 
                            week, 
                            month, 
                            year, 
                            weekday
                        ) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s) 
                        ON CONFLICT (start_time) 
                            DO NOTHING
                    """)

# FIND SONGS

song_select = ("""SELECT songs.song_id, songs.artist_id 
                  FROM songs JOIN artists ON songs.artist_id = artists.artist_id 
                  WHERE songs.title = (%s) AND artists.name = (%s) AND songs.duration = (%s);
              """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]