def primary():
  #print("Keep it logically awesome.")
  print(quotes[0])

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close() 

  print(quotes)


if __name__== "__main__":
  primary()
 
