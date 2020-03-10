import wbdata
import datetime
import pandas as pd

# IC.BUS.EASE.DFRN.DB1014            Global: Ease of doing business score (DB10-14 methodology)
# NY.GDP.PCAP.CD                GDP per capita (current US$)

# Gets the relevant data from wbdata
def getData():
    data_date = datetime.datetime(2010, 1, 1)
    x = wbdata.get_data("IC.BUS.EASE.DFRN.DB1014", data_date = data_date, pandas = True)
    y = wbdata.get_data("NY.GDP.PCAP.CD", data_date = data_date, pandas = True)
    data = pd.concat([x, y], axis = 1)

    # N/a values are dropped
    data = data.dropna(axis=0, how='any')
    data.columns = ["easeofbus", "gdp"]
    x = data["easeofbus"].tolist()
    y = data["gdp"].tolist()
    return (x, y)
