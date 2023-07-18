from tkinter import *
from web3 import Web3#task1
root = Tk()

root.title("My Ethereum App")
root.geometry("600x200")
root.configure(background="white")

# Setting labels
block_name_label = Label(root, text="Ethereum gas fee in other currencies", font=("Helvetica", 18, 'bold'), bg="white")
block_name_label.place(relx=0.5, rely=0.15, anchor=CENTER)
# block_entry = Entry(root, text="This is Entry Widget", bd=2)
# #
# block_entry.place(relx=0.5, rely=0.35, anchor=CENTER)
value_in_ether = Label(root, bg="white", font=("bold", 14))
value_in_ether.place(relx=0.5, rely=0.28, anchor=CENTER)
value_in_dollar = Label(root, bg="white", font=("bold", 10))
value_in_dollar.place(relx=0.5, rely=0.48, anchor=CENTER)
value_in_rupees = Label(root, bg="white", font=("bold", 10))
value_in_rupees.place(relx=0.5, rely=0.58, anchor=CENTER)
value_in_pounds = Label(root, bg="white", font=("bold", 10))
value_in_pounds.place(relx=0.5, rely=0.68, anchor=CENTER)


url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 = Web3(Web3.HTTPProvider(url))
# main function
# Start code for Task 1 below
def ethereum_block():
	wei_price = web3.eth.gasPrice
	gwei_price = wei_price/10**9
	gas_price_in_ether = gwei_price/10**9

    gas_price_in_dollar = gas_price_in_ether*1894
    gas_price_in_rupees = gas_price_in_dollar*155433.76
    gas_price_in_pounds = gas_price_in_rupees*1453.21

 	value_in_ether["Value of gas in Ether: ETH" + str(gas_price_in_ether)]
 	value_in_dollar["Value of gas in Dollar: $ " + str(gas_price_in_dollar)]
 	value_in_rupees["Value of gas in Rupees: $ " + str(gas_price_in_rupees)]
 	value_in_pounds["Value of gas in Pounds: $ " + str(gas_price_in_pounds)]
    # Start code for Task 3 below
   


   
    search_btn.destroy()


search_btn = Button(root, text="Search currency fee", command=ethereum_block, relief=FLAT)
search_btn.place(relx=0.5, rely=0.48, anchor=CENTER)
root.mainloop()