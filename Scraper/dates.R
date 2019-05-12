setwd("C:/Code/traffic_analysis/scraper")

twitter <- read.csv("traffic_tweets_april.csv", stringsAsFactors = T) 


dates <- as.Date(twitter$created)

min(dates, na.rm = TRUE)
max(dates, na.rm = TRUE)
