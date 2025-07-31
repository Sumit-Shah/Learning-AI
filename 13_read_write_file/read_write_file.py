# f=open("book.txt", "r")
# s = f.read()
# print(s)


# import json
# book = json.loads(s)
# print(book)

# print(type(book))


# print(book['bob'])
# print(book['bob']['phone'])


# for person in book:
#     print(book[person])



#  r = read file , w = overwrite file, a = append the file.
# f = open("/home/shah/Documents/funny.txt", "a")
# f.write("\n I Love Riding Horse.")
# f.close()

# f = open("/home/shah/Documents/funny.txt", "r")
# print(f.read())
# f.close()


# f = open("/home/shah/Documents/funny.txt", "r")
# for line in f:
#     tokens = line.split(' ')
#     print(len(tokens))
# f.close()

# f = open("/home/shah/Documents/funny.txt", "r")
# f_out = open("/home/shah/Documents/funny_wc.txt", "w")
# for line in f:
#     tokens = line.split(' ')
#     f_out.write(" wordcount:"+str(len(tokens))+line)
# f.close()
# f_out.close()



# with open("/home/shah/Documents/funny.txt", "r") as f:
#     print(f.read())
# print(f.closed)



word_stats={}

with open("13_read_write_file/poem.txt","r") as f:
    for line in f:
      words=line.split(' ')
      for word in words:
        if word in word_stats:
          word_stats[word]+=1
        else:
          word_stats[word] = 1

print(word_stats)

word_occurances = list(word_stats.values())
max_count = max(word_occurances)
print("Max occurances of any word is:",max_count)

print("Words with max occurances are: ")
for word, count in word_stats.items():
    if count==max_count:
        print(word)