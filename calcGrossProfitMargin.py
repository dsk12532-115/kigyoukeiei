class calcGrossProfitMargin:
    grossProfit = ""
    revenue = ""
    def calc(self):
        num = int(self.grossProfit)/int(self.revenue)*100
        result = round(num,2)
        print("粗利率は"+str(result)+"%です")

    def inputNum(self):
        self.grossProfit = input("売上総利益 ")
        self.revenue = input("売上高 ")
        self.grossProfit = self.grossProfit.replace(',','')
        self.revenue = self.revenue.replace(',','')



cal = calcGrossProfitMargin()
cal.inputNum()
cal.calc()