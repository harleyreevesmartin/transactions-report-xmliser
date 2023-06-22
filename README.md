# **Transaction Report XMLiser**

## **Demo**

![demonstration](https://github.com/harley-rm/transactions-report-xmliser/assets/50149947/78c086b8-0878-468f-8ed1-26c0ec8ef2ce)
## **Overview**
This is a showcase for a fictional scenario that could be encountered in the context of investment banking operations. 

The scenario is as follows: "The regulatory reporting team have to change their current reporting data format from CSV to XML and enrich their data with counterparty information. The volume is 5 transactions per day.".

This project showcases a potential solution to automate the process of converting a CSV of transaction(like) data into XML format, whilst intermittently enriching the data with additional information for each of the counterparties involved in the transaction, using publicly available information from the [GLEIF](https://www.gleif.org/en) API.

## **Usage**

### **Prerequisites**
 - Python 3.10 or higher
 - Poetry for Python (can be installed using pip: `pip install poetry`)

### **Getting Started**
Follow these steps to get the install the project.

1. Clone the repository
```
git clone git@github.com:harley-rm/transactions-report-xmliser.git
```

2. Navigate to the project directory
```
cd transactions-report-xmlilser
```

3. Install all dependencies using poetry (by default, poetry will create a venv)
```
poetry install
```

### **Running the XMLiser**
1. Prepare your input. Place your input csv in a suitable location, and choose where you would like your output to go.
2. Run the XMLiser Tool
```
poetry run xmlise --input-file-path <path/to/inputcsv.csv> --output-directory-path <path/to/outputdir>
```
