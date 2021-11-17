class Invoice:
    def __init__(self, invoiceNumber, invoiceDate, company, companyAddress, billToName, billToAddress, invoiceItemHeadNode):
        self.invoiceNumber = invoiceNumber
        self.invoiceDate = invoiceDate
        self.company = company
        self.companyAddress = companyAddress
        self.billToName = billToName
        self.billToAddress = billToAddress
        self.invoiceItemHeadNode = invoiceItemHeadNode
    
    def amountDue(self, taxes):
        currentNode = self.invoiceItemHeadNode
        total = 0
        while currentNode is not None:
            total += currentNode.product.price * currentNode.quantity
            currentNode = currentNode.next
        return total * 1.1 if taxes else total

    def printBuyingItems(self):
        print("Printing the Item List...")
        currentNode = self.invoiceItemHeadNode
        while currentNode is not None:
            print("item :" + currentNode.product.title + ", price :" + str(currentNode.product.price) + ", quantity :" + str(currentNode.quantity))
            currentNode = currentNode.next

    def printInvoice(self):
        print(
            "Invoice\n" +
            "No. :" + self.invoiceNumber + "\n" +
            "INVOICE DATE : " + self.invoiceDate + "\n" +
            "SHIP TO : " + self.company + "\n" +
            "ADDRESS : " + self.companyAddress + "\n" +

            "BILL TO : " + self.billToName + "\n" +
            "ADDRESS : " + self.billToAddress + "\n" 
        )
        currentNode = self.invoiceItemHeadNode
        while currentNode is not None:
            print(currentNode.product.title + "($" +str(currentNode.product.price) +")" + "--- " + str(currentNode.quantity) + " pcs. " + "--- AMOUNT: " + str(currentNode.product.price * currentNode.quantity)) 
            currentNode = currentNode.next

        print(
            "SUBTOTAL : " + str(self.amountDue(False)) + "\n" +
            "TAX : " + str(self.amountDue(True) - self.amountDue(False)) + "\n" +
            "TOTAL : " + str(self.amountDue(True))
        )

class InvoiceItemNode:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.next = None

    def getTotalPrice(self) :
        return self.quantity * self.product.price

class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price