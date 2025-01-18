import requests
from pathlib import Path

# Download the data
url = "https://www.rug.nl/ggdc/historicaldevelopment/maddison/data/mpd2018.xlsx"
output_file = "mpd2018.xlsx"

if not Path(output_file).exists():
    response = requests.get(url)
    with open(output_file, "wb") as f:
        f.write(response.content)
