install.packages("RMySQL")
library(RMySQL)

mydb = dbConnect(MySQL(), user='b826ca87717300', password='ac19e8f2', dbname='heroku_4987635dc15f293', host='eu-cdbr-west-02.cleardb.net')

dbListTables(mydb)

setwd("C:/Code/Traffic_Analysis/Backend")

tweets <- read.csv("traffic_tweets1.csv", stringsAsFactors = T) 

dbWriteTable(mydb, name = tweets, value = tweets, row.names = FALSE)