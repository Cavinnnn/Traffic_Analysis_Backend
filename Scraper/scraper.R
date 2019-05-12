library(twitteR)
api_key <- "PDDIDmcoFGlaa7T24VkAT3K1T" 
api_secret <- "9W5Zpihebd9bmJCxIGf2F5xwYNGUSqpipHRUyMJBTNUdbTIedP" 
access_token <- "1072207016297402380-n4eFbKN51HoiYkQh8crjup3c2Tb5yI" 
access_token_secret <- "WJhoJedC7m8dSn5TkRXxT8J39PYRhMlCaJKwf1vevSOST"

setwd("C:/Code/traffic_analysis/scraper")

setup_twitter_oauth(api_key,api_secret,access_token,access_token_secret)

searchTerm <- c("#dublin+aaroadwatch", "aaroadwatch", "LiveDrive",
                "#dublin+LiveDrive")

terms_search <- paste(searchTerm, collapse = " OR ")

n <- 3000

tweets_before <- searchTwitter(terms_search, n, lang="en")
tweets_before <- do.call("rbind", lapply(tweets_before, as.data.frame))

#Filtering
tweets <- tweets_before[!tweets_before$isRetweet, ]

write.csv(file="traffic_tweets7.csv", tweets, row.names = F)
