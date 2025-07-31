# Exercise: Python Read Write File
# poem.txt contains famous poem "Road not taken" by poet Robert Frost.
#  You have to read this file in your python program and 
# find out words with maximum occurance.
# Solution


# word_stats={}

# with open("13_read_write_file/poem.txt","r") as f:
#     for line in f:
#       words=line.split(' ')
#       for word in words:
#         if word in word_stats:
#           word_stats[word]+=1
#         else:
#           word_stats[word] = 1

# print(word_stats)

# word_occurances = list(word_stats.values())
# max_count = max(word_occurances)
# print("Max occurances of any word is:",max_count)

# print("Words with max occurances are: ")
# for word, count in word_stats.items():
#     if count==max_count:
#         print(word)






# stocks.csv contains stock price, earnings per share and book value.
#  You are writing a stock market application that will process this file and 
# create a new file with financial metrics such as pe ratio and price to book ratio.
#  These are calculated as,
# pe ratio = price / earnings per share
# price to book ratio = price / book value
# Your input format (stocks.csv) is,

def pe_ratio(price, earning_per_share):
   pe_ratio = price / earning_per_share
   return pe_ratio

def price_to_book_ratio(price, book_value):
   price_to_book_ratio = price / book_value
   return price_to_book_ratio


# import csv, sys
input = '13_read_write_file/stocks.csv'
output = '13_read_write_file/stocks_final.csv'

# with open(filename, "r") as f:
#    for row in filename:
#       print(row['']) 
   

with open(input, "r") as f, open(output, "w") as out:
   out.write("Company Name, PE Ratio, PB Ratio\n")
   next(f)  #exclude header
   for line in f:
      tokens = line.split(",")
      stock = tokens[0]
      price = float(tokens[1])
      eps = float(tokens[2])
      book = float(tokens[3])
      pe = round(price /eps, 2)
      pb = round(price / book, 2)
      out.write(f"{stock},{pe}, {pb}\n")





   




# Company Name	Price	Earnings Per Share	Book Value
# Reliance	1467	66	653
# Tata Steel	391	89	572
# Output.csv should look like this,

# Company Name	PE Ratio	PB Ratio
# Reliance	22.23	2.25
# Tata Steel	4.39	0.68
# Solution