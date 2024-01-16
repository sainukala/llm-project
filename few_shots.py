few_shots = [
    {
        'Question': "How many distinct account numbers are present in the bank_transaction_data table?",
        'SQLQuery': "SELECT COUNT(DISTINCT account_no) AS account_count FROM bank_transaction_data;",
        'SQLResult': "Result of the SQL query",
        'Answer': "10"
    },
    {
        'Question': "What is the most repeated transaction detail in the table?",
        'SQLQuery': "SELECT transaction_detail, count(transaction_detail) AS count FROM bank_transaction_data GROUP BY transaction_detail ORDER BY count DESC LIMIT 5;",
        'SQLResult': "Result of the SQL query",
        'Answer': "Final answer here"
    },
    {
        'Question': "Which transaction day has the highest withdrawal amount, and what is the account number associated with it?",
        'SQLQuery': "SELECT account_no, txn_date AS highest_withdrawl_date FROM bank_transaction_data ORDER BY withdrawl_amt DESC LIMIT 1;",
        'SQLResult': "Result of the SQL query",
        'Answer': "account_no: 1196711, highest_withdrawl_date: 2018-06-26"
    },
    {
        'Question': "Which year have the negative balance amount and associated account numbers give me the top 10?",
        'SQLQuery': "SELECT txn_date, account_no FROM bank_transaction_data WHERE balance_amt < 0 LIMIT 10;",
        'SQLResult': "Result of the SQL query",
        'Answer': "The years are 2018 and 2019. The account number associated is 409000425051"
    },
    {
        'Question': "Give me the year and number of unique accounts that has negative balance amount",
        'SQLQuery': "SELECT year(txn_date) as transaction_year, count(distinct account_no) as account_number FROM bank_transaction_data WHERE balance_amt < 0 GROUP BY year(txn_date);",
        'SQLResult': "Result of the SQL query",
        #'SQLResult': "[(2015, 3), (2016, 6), (2017, 6), (2018, 8), (2019, 8)]",
        'Answer': "The negative balance amount recorded for the year 2015 with a count of 3 unique bank accounts. Year is followed by 2016 with 6, year 2017 with 6, year 2018 with 8 and year 2019 with 8 occurrences."
    },
    {
        'Question': "Tell me or explain me about user info table",
        'SQLQuery': "SELECT * FROM user_info;",
        'SQLResult': "Result of the SQL query",
        'Answer': "The user info table contains account number and user name with total records of 10"
    },
    {
        'Question': "give me the unique or distinct account number and user names which has negative balance amount in the year 2018 and month in october.",
        'SQLQuery': "SELECT distinct a.account_no account_no, b.user_name user_name FROM (SELECT account_no FROM bank_transaction_data where balance_amt < 0 and year(txn_date) = 2018 and month(txn_date)=10 )a INNER JOIN(select user_name, account_no from user_info )b on a.account_no = b.account_no;",
        'SQLResult': "409000425051	user_3, 409000405747 user_4, 409000438611 user_5, 409000493210 user_6, 409000438620 user_7, 1196711	user_8, 1196428	user_9, 409000362497 user_10",
        'Answer': "here is the list of account numnbers and associated user name. For the account number 409000425051 user name is user_3, for the account number 409000405747 user name is user_4, 409000438611 user_5, 409000493210 user_6, 409000438620 user_7, 1196711	user_8, 1196428	user_9, 409000362497 user_10"
    },
    {
        'Question': "how many records are present in the table bank transaction data from llm_project database?",
        'SQLQuery': "SELECT COUNT(*) AS record_count FROM bank_transaction_data;",
        'SQLResult': "116201",
        'Answer': "116201 are the total number of records present in bank_transaction_data table"
    },
    {
        'Question': "how many records are present in the table bank transaction data with negative balance amount?",
        'SQLQuery': "SELECT COUNT(*) AS record_count FROM bank_transaction_data where balance_amt<0;",
        'SQLResult': "113276",
        'Answer': "113276 are the total number of negative balance amount records present in the bank_transaction_data table"
    },
    {
        'Question': "create table in llm_project database with name fraud_transaction_data and insert variable names (step int, paymentType varchar(10), amount float,nameOrig varchar(20),oldbalanceOrg float,newbalanceOrig float,nameDest varchar(20),oldbalanceDest float,newbalanceDest float,isFraud boolean,isFlaggedFraud boolean)",
        'SQLQuery': "create table llm_project.fraud_transaction_data( step int, paymentType varchar(10), amount float,nameOrig varchar(20),oldbalanceOrg float,newbalanceOrig float,nameDest varchar(20),oldbalanceDest float,newbalanceDest float,isFraud boolean,isFlaggedFraud boolean);",
        'SQLResult': "Result of the SQL query",
        'Answer': "Created table named fraud_transaction_data in llm_project database"
    }
]
