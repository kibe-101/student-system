import mysql.connector

# Function to insert a record into the database
def insert_record(fullname, course, city):
    try:
        # Establishing a connection to the database
        connection = mysql.connector.connect(
            host='localhost',
            user='Kibet',
            password='Password',
            database='student'
        )
        cursor = connection.cursor()

        # Constructing the SQL INSERT query
        insert_query = """
        INSERT INTO admission (Fullname, Course, City)
        VALUES (%s, %s, %s)
        """
        
        # Values for the new record
        new_record_values = (fullname, course, city)

        # Executing the SQL INSERT query
        cursor.execute(insert_query, new_record_values)

        # Committing the transaction
        connection.commit()
        print("Record inserted successfully!")

    except mysql.connector.Error as error:
        print("Failed to connect to MySQL database:", error)

    finally:
        # Closing the cursor and connection
        if 'connection' in locals() or 'connection' in globals():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")
