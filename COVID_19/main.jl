using CSV, DataFrames, Dates, Plots

function main()
    print("Input the country you wish to search for: \n(Put the first letter as capital)")
    search = readline()
    
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
        return country_data, data
    end

    function graph()
        country_data, data = countrywise_data()
        # Formatting the date to a particulaar format and parsing it.
        dates = String.(names(data))[5:end];
        format = Dates.DateFormat("m/d/Y");
        dates = parse.(Date, dates, format) .+ Year(2000)
    
        # Plotting a General Graph
        plot(dates, country_data, xticks=dates[1:30:end], xrotation=45, leg=:topleft, 
        label="General")
        
        # Plotting Logarithmic Graph
        plot(dates, country_data, #=xticks=dates[1:30:end],=# xrotation=45, leg=:topleft, 
        label="Log", yscale=:log10)
        xlabel!("date")
        ylabel!("confirmed cases in $search")
        title!("Graph for $search confirmed COVID-19 cases")
        
        savefig("$search graph")
    end
    load_data()
    countrywise_data()
    graph()
end

main()
