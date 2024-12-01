import sqlite3
import matplotlib.pyplot as plt

# Database setup
DB_NAME = "population_JM.db"

def create_database():
    """Create the database and the population table."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)
    connection.commit()
    connection.close()

def insert_initial_data():
    """Insert initial data for 10 cities in Florida for the year 2023."""
    cities_data = [
        ("Miami", 2023, 467963),
        ("Tampa", 2023, 399700),
        ("Orlando", 2023, 309154),
        ("Jacksonville", 2023, 902488),
        ("Tallahassee", 2023, 196169),
        ("St. Petersburg", 2023, 260999),
        ("Fort Lauderdale", 2023, 183109),
        ("Cape Coral", 2023, 204549),
        ("Hialeah", 2023, 224669),
        ("Gainesville", 2023, 141085)
    ]

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO population (city, year, population) VALUES (?, ?, ?)", cities_data)
    connection.commit()
    connection.close()

def simulate_population_growth():
    """Simulate a 2% population growth for the next 20 years."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    
    cursor.execute("SELECT DISTINCT city FROM population WHERE year = 2023")
    cities = [row[0] for row in cursor.fetchall()]

    for city in cities:
        cursor.execute("SELECT population FROM population WHERE city = ? AND year = 2023", (city,))
        initial_population = cursor.fetchone()[0]

        for year in range(2024, 2044):
            initial_population = int(initial_population * 1.02)
            cursor.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)", 
                           (city, year, initial_population))

    connection.commit()
    connection.close()

def plot_population_growth(city):
    """Plot the population growth for a given city."""
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT year, population FROM population WHERE city = ?", (city,))
    data = cursor.fetchall()
    connection.close()

    years, populations = zip(*data)
    plt.figure(figsize=(10, 6))
    plt.plot(years, populations, marker='o', label=city)
    plt.title(f"Population Growth in {city}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    create_database()
    insert_initial_data()
    simulate_population_growth()
    
    print("Population growth data has been generated for the following cities in Florida:")
    cities = ["Miami", "Tampa", "Orlando", "Jacksonville", "Tallahassee", 
              "St. Petersburg", "Fort Lauderdale", "Cape Coral", "Hialeah", "Gainesville"]
    print(", ".join(cities))

    while True:
        city = input("Enter the name of the city to view population growth (or type 'exit' to quit): ").strip()
        if city.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        elif city in cities:
            plot_population_growth(city)
        else:
            print("Invalid city. Please choose from the list provided.")


main()
