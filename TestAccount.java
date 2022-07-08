class TestAccount {
    public static void main(String[] args){
		BankAccount accountOne = new BankAccount();
		accountOne.deposit(100, "checking");
		accountOne.deposit(100, "savings");
		accountOne.withdraw(50, "checking");
		accountOne.withdraw(50, "savings");
        accountOne.withdraw(100, "savings");


		System.out.println(accountOne.getCheckingBalance());
        System.out.println(accountOne.getSavingsBalance());
    }
}