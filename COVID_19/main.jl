using CSV, DataFrames, Dates, Plots 
print("Input the country you wish to search for: \n(Put the first letter as capital)")
search = readline()
    
# Loading the data 
function load_data()
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    download(url, "COVID_Data.csv")   
    data = CSV.read("COVID_Data.csv")
    rename!(data, 1=>"Province", 2=>"Country")
    return data
end

function countrywise_data()
    data = load_data()
    countries = data[1:end,2];
    row = findfirst(countries .== search);
    country_data = convert(Vector, data[row, 5:end]);
    # Formatting the date to a particulaar format and parsing it.
    dates = String.(names(data))[5:end];
    format = Dates.DateFormat("m/d/Y");
    dates = parse.(Date, dates, format) .+ Year(2000)
    
    return country_data, data, dates
end

function graph()
    country_data, data, dates = countrywise_data()
    
    # Plotting a General Graph
    plot(dates, country_data, xticks=dates[1:30:end], xrotation=45, leg=:topleft, 
    label=search)
    savefig("$search Graph")
end

graph()
