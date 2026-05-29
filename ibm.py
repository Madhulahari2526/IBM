# 💰 AI Agent for Digital Financial Literacy – Python Code


# 💰 Digital Financial Literacy AI Agent
# Python Mini AI Project

print("======================================")
print(" 💰 AI Financial Literacy Assistant ")
print("======================================")

while True:

    print("\nAsk your financial question:")
    print("1. UPI Payment")
    print("2. Online Scam Protection")
    print("3. Loan Interest Rate")
    print("4. Monthly Budget Tips")
    print("5. Savings Advice")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    # ------------------------------------
    # UPI Payment
    # ------------------------------------
    if choice == "1":

        print("\n📱 UPI Payment Guide")
        print("----------------------")
        print("1. Open any UPI app like PhonePe, Google Pay, or Paytm.")
        print("2. Select 'Send Money'.")
        print("3. Enter UPI ID or scan QR code.")
        print("4. Enter amount.")
        print("5. Verify receiver details.")
        print("6. Enter UPI PIN securely.")
        print("✅ Payment Successful!")

    # ------------------------------------
    # Scam Protection
    # ------------------------------------
    elif choice == "2":

        print("\n🛡️ Online Scam Protection Tips")
        print("--------------------------------")
        print("✔ Never share OTP or UPI PIN.")
        print("✔ Avoid clicking unknown links.")
        print("✔ Verify caller identity before payment.")
        print("✔ Use official banking apps only.")
        print("✔ Enable two-factor authentication.")

    # ------------------------------------
    # Loan Interest
    # ------------------------------------
    elif choice == "3":

        principal = float(input("\nEnter Loan Amount: "))
        rate = float(input("Enter Interest Rate (%): "))
        time = float(input("Enter Time (Years): "))

        # Simple Interest Formula
        interest = (principal * rate * time) / 100
        total = principal + interest

        print("\n💳 Loan Calculation")
        print("----------------------")
        print("Interest Amount:", interest)
        print("Total Amount to Pay:", total)

        if rate <= 10:
            print("✅ This is generally considered a safe interest rate.")
        else:
            print("⚠ Interest rate is high. Compare with other banks.")

    # ------------------------------------
    # Budget Tips
    # ------------------------------------
    elif choice == "4":

        income = float(input("\nEnter Monthly Income: "))
        expenses = float(input("Enter Monthly Expenses: "))

        savings = income - expenses

        print("\n📊 Budget Analysis")
        print("---------------------")
        print("Monthly Savings:", savings)

        if savings > 0:
            print("✅ Good job! You are saving money.")
        else:
            print("⚠ Your expenses are higher than income.")

    # ------------------------------------
    # Savings Advice
    # ------------------------------------
    elif choice == "5":

        print("\n🏦 Smart Savings Tips")
        print("-----------------------")
        print("✔ Save at least 20% of your income.")
        print("✔ Maintain emergency funds.")
        print("✔ Avoid unnecessary loans.")
        print("✔ Track daily expenses.")
        print("✔ Invest wisely after research.")

    # ------------------------------------
    # Exit
    # ------------------------------------
    elif choice == "6":

        print("\n👋 Thank you for using AI Financial Assistant!")
        break

    # ------------------------------------
    # Invalid Input
    # ------------------------------------
    else:
        print("\n❌ Invalid choice. Please enter between 1 and 6.")


