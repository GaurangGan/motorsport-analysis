import requests
import pandas as pd
import matplotlib.pyplot as plt

def fetch_formula1_data(season):
    api_url = f"https://ergast.com/api/f1/{season}.json"
    response = requests.get(api_url)
    data = response.json()
    return data

def process_data(data):
    # Extract relevant information from the API response
    drivers_df = pd.DataFrame(data['MRData']['DriverTable']['Drivers'])
    races_df = pd.DataFrame(data['MRData']['RaceTable']['Races'])
    
    return drivers_df, races_df

def analyze_data(drivers_df):
    # Analyze data (example: top 10 drivers)
    top_drivers = drivers_df.sort_values('points', ascending=False).head(10)
    return top_drivers

def visualize_data(top_drivers):
    # Visualize data (example: bar chart for top drivers)
    plt.bar(top_drivers['givenName'] + ' ' + top_drivers['familyName'], top_drivers['points'])
    plt.xlabel('Driver')
    plt.ylabel('Points')
    plt.title('Top 10 Drivers')
    plt.show()

def main():
    # Input the season you want to analyze
    season = input("Enter the Formula 1 season (e.g., 2022): ")
    
    # Fetch and process data
    data = fetch_formula1_data(season)
    drivers_df, races_df = process_data(data)
    
    # Analyze and visualize data
    top_drivers = analyze_data(drivers_df)
    visualize_data(top_drivers)

if __name__ == "__main__":
    main()
