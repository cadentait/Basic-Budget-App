class Category:

    #Instantiate Object
  def __init__(self, name):
      self.name = name
      self.balance = 0.0
      self.ledger = list()
        
    #Defining __str__
  def __str__(self):
    title = f"{self.name:*^30}\n"
    items = ""
    for i in range(len(self.ledger)):
        items += f"{self.ledger[i]['description']:<23}" + f"{self.ledger[i]['amount']:>7.2f}" "\n"
        output = title + items + "Total: ".rjust(22) + f"{self.balance:>8.2f}"
        return output
    
    #Deposit method
  def deposit(self, amount, description = ''):
      self.ledger.append({"amount": amount, "description": description})
      self.balance += float(amount)
      print("balance is currently", self.balance)
    
    #Withdrawl method
  def withdraw(self, amount, description = ''):
    print("amount is", amount)
    if amount <= self.balance:
        self.ledger.append({"amount": amount, "description": description})
        self.balance -= amount
        print(f"{'Withdrawl of ' + str(amount) + ' was Successful':-^40}")
        return True
    else: 
      print("Insufficient Funds")   
      return False
    
    #Current balance method
    
  def get_balance(self):
    return self.balance
    
    #Money transfer method
  def transfer(self, amount, category):
    if self.check_funds(amount) == False:
      print("\n***Cannot Complete Transfer***\n***Insufficient Funds***\n")
      return False
    else:
      self.withdraw(amount, ("Tranferred to " + category.name))
      category.deposit(amount, ("Transferred from " + self.name))
      return True
    
    #Check if funds are available
  def check_funds(self, amount):
    if float(amount) > self.balance:
      print(f"{str(amount)+' dollars is available':-^40}")
      return False
    else:
      print(f"{str(amount)+' dollars is available':-^40}")
      True
            
  def create_spend_chart(self, categories):
    length = list()
    name = list()
    withdrawls = list()
    percentage = list()
    for category in categories:
      t = 0
      length.append(len(category.name))
      name.append(category.name)
      for items in category.ledger:
        item = list(items.values())
        if item[0]>=0:
          continue
        else:
          t = t+(-(item[0]))
        withdrawls.append(t)
        
        #Get pecentages
    total = sum(withdrawls)
    for i in range(len(withdrawls)):
      each = withdrawls[i] / total
      each = int(round(each, 2)*100)
      percentage.append(each)
        
        #Output
    output = "percentaage spent by category\n"
    t = 100
    while t >= 0:
      output = output.rstrip(" ") + str(t).rjust(3) + "| "
      for i in range(len(percentage)):
        if t <= percentage[i]:
          output = output + "o" + "  "
        else:
          output = output + "  "
      t = t - 10
      output = f"{output}'\n'"
    output = output.rstrip(" ")+"    -"
        
        #Dashes
    for i in range(len(percentage)):
      output = output.rstrip(" ") + "---"
    output = f"{output}'\n'"
        
        #Getting names
    for i in range(max(length)):
      output = output.rstrip(" ") + "     "
      for x in range(len(name)):
        try:
          output = output + name[x][i] + "  "
        except:
          output = output + "   "
        if not i == (max(length) - 1):
          output = f"{output}'\n'"
    length.clear()
    name.clear()
    withdrawls.clear()
    percentage.clear()
    return output
            