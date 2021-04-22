def primary():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close() #comment

  print(quotes)

if __name__== "__main__":
  primary()
 
