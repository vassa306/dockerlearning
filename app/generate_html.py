import mysql.connector
from mysql.connector import Error
import os
import time

def get_db_connection(retries=5, delay=5):
    for _ in range(retries):
        try:
            connection = mysql.connector.connect(
                host="db",
                user="root"
                password="rootpassword"
                database="mydatabase"
            )
            print("Successfully connected to the database")
            return connection
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            print(f"Retrying in {delay} seconds...")
            time.sleep(delay)
    raise Exception("Failed to connect to the database after multiple attempts")

def fetch_data():
    connection = get_db_connection()
    cursor = connection.cursor()
    query="SELECT * FROM USER"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)  # Replace 'your_table' with your actual table name
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows

def print_results(data):
    """Print the results from the query."""
    for row in data:
        print(row)

def generate_html(data):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>My Page</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">Navbar</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item active">
                        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Features</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Pricing</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Contact</a>
                    </li>
                </ul>
            </div>
        </nav>

        <!-- Hero Section -->
        <div class="jumbotron jumbotron-fluid">
            <div class="container">
                <h1 class="display-4">Hello</h1>
                <p class="lead">Welcome to my Page</p>
            </div>
        </div>

        <!-- Content Section -->
        <div class="container mb-4">
            <div class="row">
                <div class="col-md-4">
                    <h2>Heading</h2>
                    <p>Some example text. Some example text. Some example text. Some example text.</p>
                    <p><a class="btn btn-secondary" href="#" role="button">View details »</a></p>
                </div>
                <div class="col-md-4">
                    <h2>Heading</h2>
                    <p>Some example text. Some example text. Some example text. Some example text.</p>
                    <p><a class="btn btn-secondary" href="#" role="button">View details »</a></p>
                </div>
                <div class="col-md-4">
                    <h2>Heading</h2>
                    <p>Some example text. Some example text. Some example text. Some example text.</p>
                    <p><a class="btn btn-secondary" href="#" role="button">View details »</a></p>
                </div>
            </div>
            <div class="row mt-4">
                <div class="col-md-12">
                    <h2>Database Data</h2>
                    <div id="db-data" class="border p-3">
                        <ul>
    """
    for row in data:
        html_content += f"<li>{', '.join(map(str, row))}</li>"
    
    html_content += """
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    
    with open("/usr/share/nginx/html/index.html", "w") as file:
        file.write(html_content)

if __name__ == "__main__":
    data = fetch_data()
    print_results(data=data)
    generate_html(data=data)