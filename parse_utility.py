'''

Search by parsed_data.get("CountryCode-Province").get("Date") to get list of data.
Example:    parsed_data.get("US-Washington").get("2020-04-14T00:00:00Z")

If you don't know the date, use list() to list all dates available.
Example:    list(parsed_data.get("US-Washington"))

If the province was not provided, use an empty string for the province.
Example:    parsed_data.get("ZA-").get("2020-04-14T00:00:00Z")

The list contains various data. You can simply refer them by specifying the index.
Example:    parsed_data.get("US-Washington").get("2020-04-14T00:00:00Z")[0]
            returns "United States of America"

index       data
0           Country
1           CountryCode
2           Province
3           City
4           CityCode
5           Lat
6           Lon
7           Confirmed
8           Deaths
9           Recovered
10          Active
11          Date
'''

def read_and_parse(jdata):
    data_dict = {}
    for jobject in jdata:
        parsed_object = []
        curr_prov = jobject["Province"]
        curr_cont_code = jobject["CountryCode"]
        curr_date = jobject["Date"]
        parsed_object.append(jobject["Country"])
        parsed_object.append(curr_cont_code)
        parsed_object.append(curr_prov)
        parsed_object.append(jobject["City"])
        parsed_object.append(jobject["CityCode"])
        parsed_object.append(jobject["Lat"])
        parsed_object.append(jobject["Lon"])
        parsed_object.append(jobject["Confirmed"])
        parsed_object.append(jobject["Deaths"])
        parsed_object.append(jobject["Recovered"])
        parsed_object.append(jobject["Active"])
        parsed_object.append(curr_date)

        name = curr_cont_code+"-"+curr_prov
        data_dict.setdefault(name, {})
        data_dict[name][curr_date] = parsed_object
    return data_dict


def output_to_string(parsed_data):
    string = ""
    string += "Country: "+str(parsed_data[0])
    if parsed_data[2] != "":
        string += "\nState: " + str(parsed_data[2])
    string += "\nConfirmed cases: "+str(parsed_data[7])
    string += "\nTotal death: "+str(parsed_data[8])
    string += "\nTotal recovered: "+str(parsed_data[9])
    string += "\nTotal active: "+str(parsed_data[10])
    string += "\n\nData date: +"+str(parsed_data[11])[:10]
    return string

## Output: string containing html formatted texts
## Input: list of parsed data
def output_to_html(parsed_data):
    string = "<p><strong>COVID-19: Daily case report</strong></p>"
    string += "\n<p>Country:</p>" + str(parsed_data[0])
    if str(parsed_data[2]) != "":
        string += "\n<p>Province:</p>" + str(parsed_data[2])
    string += "\n<p>Date:</p>" + str(parsed_data[11])[:10]
    string += "\n<p>Confirmed cases:</p>" + str(parsed_data[7])
    string += "\n<p>Deaths:</p>" + str(parsed_data[8])
    string += "\n<p>Recovered:</p>" + str(parsed_data[9])
    string += "\n<p>Active:</p>" + str(parsed_data[10])
    string += "\n<p>Data retrieved by <a href=\"https://documenter.getpostman.com/view/10808728/SzS8rjbc?version=latest#7934d316-f751-4914-9909-39f1901caeb8\">Postman</a></p>\n"
    return string