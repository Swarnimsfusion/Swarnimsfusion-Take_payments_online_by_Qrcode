import qrcode
#Taking UPI ID AS A INPUT
upi_id=input("Enter your UPI id = ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE
#pa= upi_id which we have to pay
#pr= Recipent Name
#am= Amount
#cu= Currency
#tn= Acknowledgment Msg

#Defining URL based on the upi id ( can be modified based on the payment apps you want to support)

phonepe_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
googlepay_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

# f= string formatting
# mc = merchant code

#Creating qr for each payment app

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
googlepay_qr = qrcode.make(googlepay_url)

# saving the qr_code to image file (optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
googlepay_qr .save('googlepay_qr .png')

# dispaying qr code (need to install PIL/Pillow Library)
phonepe_qr.show()
paytm_qr.show()
googlepay_qr.show()