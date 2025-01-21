# Data Engineering Project: Building Automated Pipelines and Transforming Data with NiFi, Python, and ETL Processes

## Project Overview
This project demonstrates my experience as a Data Engineer, showcasing my skills in **NiFi, Python, SQL, and ETL** processes. With over `2.5` years of experience, I have successfully built automated data pipelines and performed data analysis using a variety of tools and technologies. 

This project simulates real-world data engineering workflows, integrating various data sources, performing data cleansing and enrichment, and managing master data and its variations. It involves building **scalable data pipelines** and **efficient database storage solutions**.

## Key Skills Demonstrated:
- **NiFi**: Design and implement automated data pipelines, manage data flows, and orchestrate ETL processes.
- **Python**: Data processing and transformation using Pandas, NumPy, and Levenshtein distance algorithms to solve data-related problems.
- **ETL Processes**: Building robust ETL pipelines for transforming data from various formats (CSV, JSON, EDI) into usable outputs.
- **Excel**: Data analysis and reporting, leveraging Excel to provide insights and streamline data processing.
- **Data Automation**: Automating workflows and integrating various data sources to improve efficiency and reduce manual intervention.

## 🚀 Key Features  
- **Data Ingestion:** Extracting data from multiple sources (APIS, Mails, CSV, JSON, Excel, XML. EDI Databases) using **Apache NiFi** and **Python**.  
- **Data Processing & Transformation:**  
  - Cleaning, enriching, and normalizing data with **Pandas** and **SQL**.  
  - Handling missing values, duplicates, and inconsistent data formats.  
  - Implementing **business rules** for data validation.  
- **Data Storage & Management:**  
  - Storing structured data in **SQL databases** (SqlServer).  
  - Using indexing and partitioning for optimized queries.  
- **Workflow Automation & Scheduling:**  
  - Automating ETL jobs with **Apache NiFi**.  
  - Implementing logging and error handling for pipeline monitoring.  
- **Performance Optimization:**  
  - Using **window functions and indexing** for efficient SQL queries.  
  - Optimizing **large-scale data processing** with **batch vs. stream processing**.  

## 🛠 Technologies Used  
- **Apache NiFi** – Data ingestion and workflow automation  
- **Python** – Data transformation using Pandas, NumPy  
- **SQL** – Querying and database management (PostgreSQL/MySQL)  
- **Boto3** – Interacting with AWS services (if applicable)  
- **Logging & Error Handling** – Ensuring data pipeline reliability  

## 📂 Project Structure  
This is the project directory structure for the Data Engineering project. It includes various folders for organizing different components of the project, such as data creation, input files, logs, and NiFi workflows.
### Directory Structure
```
DataEngineeringProject
│
├── DataCreationFiles
│   ├── sample_data_s3.csv        # Sample data file for AWS S3
│   ├── sample_data_local.json    # Sample data file for local processing
│   └── sample_data_sftp.xlsx     # Sample data file for SFTP
│
├── /DataCreationScripts
│   ├── data_creation_s3.py       # Python script for generating data for S3
│   ├── data_creation_local.py    # Python script for generating local/SFTP data
│   └── s3_bucket_creation.sh     # Script for creating the test S3 bucket
│
├── InputFiles
│   ├── input_data_1.csv          # Example input data file for processing
│   ├── input_data_2.json         # Example input data file for processing
│   └── input_data_3.xlsx         # Example input data file for processing
│
├── Logs
│   ├── pipeline_execution.log    # Log file for tracking pipeline executions
│   └── error_log.log             # Error log for troubleshooting issues
│
├── NiFi
│   ├── flowfile_generation.xml   # NiFi flow for generating flow files
│   ├── s3_data_pipeline.xml      # NiFi data pipeline for AWS S3 integration
│   └── local_sftp_pipeline.xml   # NiFi data pipeline for local/SFTP processing
│
└── README.md                     # Project overview and instructions

```
### Folder Descriptions:
- **DataCreationFiles**: Contains sample data files used for testing and data generation.
- **DataCreationScripts**: Includes Python and shell scripts for generating data and setting up resources like S3 buckets.
- **InputFiles**: Directory to store raw input data that will be processed by the pipeline.
- **Logs**: Stores logs for monitoring pipeline execution and troubleshooting errors.
- **NiFi**: Contains Apache NiFi flow files used to design and execute the data pipeline.

## Prerequisites  
### 📦 Python Installation  
Ensure Python 3.x is installed on your system. If not, download and install the latest version from [Python's official website](https://www.python.org/downloads/).

Once Python is installed, verify the installation by running:
``python --version``
#### 🔧 Install Required Python Packages  
You can install the necessary packages by running the following command:
``pip install -r requirements.txt``
The `requirements.txt` should contain the following packages:
- **moto**: For simulating AWS services like S3.
- **boto3**: For interacting with AWS services using Python.
- **pandas**: For data manipulation and analysis.
- **numpy**: For numerical computations.
- **requests**: For making HTTP requests (if working with APIs).
- **pyyaml**: For reading/writing YAML files.

### 🌐 NiFi Installation  
1. Download and install **Apache NiFi** from [here](https://nifi.apache.org/download.html).
2. After downloading, extract the contents of the zip file and navigate to the NiFi folder.
3. To start NiFi, open a terminal or command prompt and run the following command:
``./bin/nifi.sh start `` *For Linux/MacOS*
``.\bin\nifi.bat start`` *For Windows*
4. Once NiFi starts, open the NiFi UI by navigating to `http://localhost:8080/nifi` in your web browser.
#### 🔧 NiFi Processor Configuration
Ensure that the necessary NiFi processors are configured for your data flow, such as:
- **GetFile**
- **PutFile**
- **ExecuteScript**
- **PutS3Object**

You can use NiFi to orchestrate data pipelines and integrate various systems, such as AWS S3, local files, and APIs.

### ⚙️ Java Installation for NiFi  
NiFi requires **Java 8** or later. You can download it from [here](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) or use an open-source version such as [AdoptOpenJDK](https://adoptopenjdk.net/).

To verify Java installation, run:
``java -version``
### 📊 Excel  
Ensure you have **Microsoft Excel** installed for data analysis and reporting. Alternatively, **LibreOffice Calc** can be used as an open-source option.

### 💻 Git Installation  
If you're using Git for version control, ensure it's installed on your system. You can download it from [Git's official website](https://git-scm.com/).

Verify Git installation:
``git --version``
### 📥 AWS Account Setup  
If you're planning to use AWS services (e.g., S3, EC2), ensure you have an **AWS account** set up. Create an account at [AWS](https://aws.amazon.com/).

You’ll also need to configure your AWS CLI with the following command:
Enter your **AWS Access Key ID**, **Secret Access Key**, and **Region** when prompted.
### 🚀 MotoServer Installation  
To simulate AWS services locally, you can use **MotoServer**. To install **MotoServer**, follow these steps:
1. **Install Python**  
   Make sure Python 3.x is installed on your machine. You can download it from the official [Python website](https://www.python.org/downloads/).

2. **Install Moto**  
   You can install **Moto** via `pip` (Python package installer). Open **Command Prompt** or **PowerShell** and run:

   ```bash
   pip install moto
   ```
3. **Start MotoServer**
    
    Once Moto is installed, you can start MotoServer by running the following command in Command Prompt or PowerShell:   
    ```bash 
    moto_server -p 10001
    ```
By default motoserv will have the below credentails for s3:
-  endpoint_url = ``http://127.0.0.1:10001``  *MotoServer URL*
- aws_access_key_id = ``fakeAccessKey`` *Fake credentials for MotoServer*
- aws_secret_access_key = ``fakeSecretKey`` *Fake credentials for MotoServer*
- region_name = ``us-west-1`` *Region for the bucket*
> **Note:** If you already have an AWS account, you can skip the **MotoServer** installation as it is an alternative to AWS S3 used for simulating AWS services locally. It is added so you can simulate S3 without the need for an actual AWS account. If you prefer to use AWS services directly, you can configure your project to use your actual AWS credentials and services.

## 📌 Data Creation Stage
This pipeline supports data generation for Local (including SFTP), AWS S3, and Email.
- *SFTP/Local*: Randomized generation of either Excel or JSON files.
- *AWS S3*: Generates CSV files.
- *Email*: Randomized generation of either EDI or XML files.

## 📂 Data Creation Pipeline for AWS S3
### 1️⃣ **GenerateFlowFile**
Initiates the flow (to be scheduled later).
### 2️⃣ **ExecuteStreamCommand (Bucket Creation)**
Creates a test S3 bucket: `my-test-bucket`.  
Configured for both AWS S3 (Production) and MotoServer (Local S3 Emulation).  
MotoServer replicates AWS S3 locally but may have limitations.
### 3️⃣ **ExecuteStreamCommand (S3 Data Creation)** 
Generates a CSV file with 10 million records.  
The row count can be increased, but it may take longer to generate.
### 4️⃣ **ExtractText**
Extracts the filename from the S3DataCreation processor output.  
Uses regex to capture all characters after `AwsS3OriginalFilename`.
### 5️⃣ UpdateAttribute
The Filename changes with a UUID generated by nifi while using fetchfile. So to update the filename, i have used updateattribute and updated filename property

filename : ${AwsS3OriginalFilename}
Here AwsS3OriginalFilename is the property in which i had stored the original filename from the source.

### 6️⃣ FetchFile
This processor fetches the file created by the previous processor.

File to Fetch:
The attribute AwsS3OriginalFilename contains the filename, which is used to fetch the file. The filename is displayed in the console, and ExtractText saves it to the AwsS3OriginalFilename attribute.
Completion Strategy:
Set to Delete file to ensure the file is fetched and deleted from the directory. Alternatively, you can choose None to keep the file in the directory.
The Move Conflict Strategy is set to Rename in case files with the same name appear and cause conflicts. Based on the use case, you could also use Replace File to retain only the latest file received.
### 7️⃣ **PutS3Object**
This processor is used to push the generated data file to the S3 bucket. In the flow, I have configured it to push the file to MotoServer with the below credentials.  
*(Note: For AWS S3 production, **Endpoint Override URL**: `http://127.0.0.1:10001` would not be required.)*
### Credentials Configuration for MotoServer (Local S3 Emulation):
- **AWS Access Key ID**: `fakeAccessKey` (MotoServer fake credentials).  
  For S3 production, provide the Access Key ID of the required bucket.
- **AWS Secret Access Key**: `fakeSecretKey` (MotoServer fake credentials).  
  For S3 production, provide the Secret Access Key of the required bucket.
- **Region**: `US West (N. California)` (This is the region required for the MotoServer bucket. For production, the bucket might be in a global configuration or a specific region, so configure it accordingly based on your setup.)
- **Object Key**: `AwsS3OriginalFilename` is the property which contains the filename.  For production, you can use the same attribute.
## 📂 Data Creation Pipeline for Local/SFTP
### 1️⃣ **GenerateFlowFile**
Processor to generate a flow file to initiate or start the flow (will be scheduled later).
### 2️⃣ **ExecuteStreamCommand (DataCreation_Local_Sftp)**
- Script to Create Sample Data for Local or SFTP. This script is used to create sample data for local storage or SFTP transfer. It generates both **JSON** and **Excel** files, providing functionality for handling buffer rows and columns.
- ### Key Features:
    - **Buffer Rows and Columns**: Some files may contain metadata in these rows, and there may be instances where the data breaks and resumes after a few lines.
    - **Handling Buffer Rows**: For simplification, buffer rows and columns are skipped using the `pd.dropna(thresh=10)` attribute in **Pandas**. This helps omit these lines.
        - **Threshold=10** was chosen arbitrarily; the number can be adjusted based on the pattern of the files received.
        - In this project, the largest value between the number of columns and rows mentioned in the creation of the Excel file is considered.
- ### Considerations:
    - Each file or data source with metadata or data breaks needs to be handled separately to ensure accurate processing.

### 3️⃣ **ExtractText**
This processor is used to extract the filename from the previous script. The **DataCreation_Local_Sftp** processor prints the filename in the console, and the **ExtractText** processor extracts and saves the filename in an attribute called `sftp_local_Filename`.
The expression `sftp_local_Filename\s*(.*)` in NiFi's **ExtractText** processor is a regular expression (regex) used to extract a portion of text based on a pattern. In this case, it considers all characters after `sftp_local_Filename`.

### 4️⃣ FetchFile
This processor fetches the file created by the previous processor.
### File to Fetch:
- The attribute `SFTP_LOCAL_Filename` contains the full file path and filename, which is used to fetch the file. The filename is displayed in the console, and **ExtractText** saves it to the `SFTP_LOCAL_Filename` attribute.

### Completion Strategy:
- Set to **Delete file** to ensure the file is fetched and deleted from the directory. Alternatively, you can choose **None** to keep the file in the directory.
- The **Move Conflict Strategy** is set to **Rename** in case files with the same name appear and cause conflicts. Based on the use case, you could also use **Replace File** to retain only the latest file received.

### 5️⃣ **UpdateAttribute**
The Filename changes with a `UUID` 
generated by nifi while using fetchfile. 
So to update the filename, i have used 
updateattribute and updated `filename` property
``` bash
filename : ${SFTP_LOCAL_Filename}
```
Here `SFTP_LOCAL_Filename` is the property in which i had stored the original filename from the source.
### 6️⃣ **FetchFile**

This processor fetches the file created by the previous processor.




### 7️⃣ **PutFile**
This processor is used to move the file to the destination folder.
### Directory:
- This attribute defines the folder path where the file will be moved.

### Conflict Resolution Strategy:
- Set to **replace** to replace the file if a file with the same name exists.

### Create Missing Directories:
- Set to **true** to create the folder if it does not exist. You can also use this to create subfolders with a date timestamp, which can be provided using Apache NiFi **Expression Language**.
``` bash
Now if you wanted to configure for sftp, instead of `putfile` processor, replace with `putsfpt` processor.
```
## 📂 Data Creation Pipeline for Mail
### 1️⃣ **GenerateFlowFile**
Processor to generate a flow file to initiate or start the flow (will be scheduled later).
### 2️⃣ **ExecuteStreamCommand (DataCreationMail)**
Script to Create Sample Data for Mail. It generates both **EDI** and **XML** files.
### 3️⃣ **ExtractText**
This processor is used to extract the filename from the previous script. The **DataCreationMail** processor prints the filename in the console, and the **ExtractText** processor extracts and saves the filename in an attribute called `MailOriginalFilename`.
The expression `MailOriginalFilename\s*(.*)` in NiFi's **ExtractText** processor is a regular expression (regex) used to extract a portion of text based on a pattern. In this case, it considers all characters after `MailOriginalFilename`.
### 4️⃣ **UpdateAttribute**
The Filename changes with a `UUID` 
generated by nifi while using fetchfile. 
So to update the filename, i have used 
updateattribute and updated `filename` property
``` bash
filename : ${MailOriginalFilename}
```
Here `MailOriginalFilename` is the property in which i had stored the original filename from the source.
### 5️⃣ **FetchFile**

This processor fetches the file created by the previous processor.

### File to Fetch:
- The attribute `MailOriginalFilename` contains the filename, which is used to fetch the file. The filename is displayed in the console, and **ExtractText** saves it to the `SFTP_LOCAL_Filename` attribute.

### Completion Strategy:
- Set to **Delete file** to ensure the file is fetched and deleted from the directory. Alternatively, you can choose **None** to keep the file in the directory.
- The **Move Conflict Strategy** is set to **Rename** in case files with the same name appear and cause conflicts. Based on the use case, you could also use **Replace File** to retain only the latest file received.

### 6️⃣ **PutEmail**
# 📧 PutEmail Processor Configuration

This section details the configuration required for setting up the **PutEmail** processor in Apache NiFi to send emails using **Yahoo SMTP**.

#### ✉️ SMTP Configuration

| Property           | Value                          |
|-------------------|--------------------------------|
| **SMTP Hostname** | i have provided the details below        |
| **SMTP Port**     | `587`                          |
| **SMTP Username** | provide your username(emailid)        |
| **SMTP Password** | `Provide your password`        |
| **SMTP Auth**     | `true`                         |
| **SMTP STARTTLS** | `true`                         |
** Tip:** The above values can be stored as global variables.  
To do this:  
1️⃣ Right-click on the **NiFi Canvas** and select **Variables**.  
2️⃣ Create a new variable by providing a name and assigning the corresponding value.  
3️⃣ These variables can then be referenced in the configurations above.  

#### 📧 SMTP Server List for Popular Email Providers  

| Email Provider    | SMTP Server Address        |
|------------------|---------------------------|
| **Yahoo Mail**   | `smtp.mail.yahoo.com`     |
| **Gmail**        | `smtp.gmail.com`          |
| **Outlook**      | `smtp.office365.com`      |
| **Hotmail**      | `smtp.live.com`           |
| **Zoho Mail**    | `smtp.zoho.com`           |
| **ProtonMail**   | `smtp.protonmail.com`     |
| **AOL Mail**     | `smtp.aol.com`            |
| **iCloud Mail**  | `smtp.mail.me.com`        |
| **Yandex Mail**  | `smtp.yandex.com`         |
| **Mail.com**     | `smtp.mail.com`           |

*For each provider, the SMTP port is typically `587` for TLS, `465` for SSL, and `25` for non-secure connections.*  

---
*Other SMTP settings can be kept as default.*

## 📤 Email Details

| Property   | Value                           |
|-----------|---------------------------------|
| **From**  | `test_akhil@yahoo.com`         |
| **To**    | `test.akhilharold@gmail.com`   |
| **Subject** | `Message from NiFi`         |

## 📜 Email Message Content
```bash
provide your message here
```
## Example
``` bash
Hi Akhil,

I have attached this week's file. Kindly process it.

Thanks,
Sarah
```
### 📎 Additional Settings

| Property       | Value  |
|--------------|--------|
| **Attach File** | `true` |

*All other settings can remain as default.*

---

This configuration enables **NiFi to send automated emails with attachments via chosen SMTP(Here its Yahoo).** 🚀  


## 📌 Data Ingestion Stage
This stage involves ingesting data from various sources. To keep this project simple, I have limited the data sources to local, email, S3, and web scraping. I will provide sample scripts to pull data from GCP.

## 📂 Data Ingestion for AWS S3
1. **ListS3**: This processor is used to check the S3 bucket and list the files present in it based on timestamps. Credentials for MotoServer are provided below.
    - **Listing Strategy**: `Tracking Timestamps` – *This property will be the same for both MotoServer and AWS S3. I have chosen the listing strategy as timestamp so only the latest files are considered.*
    - **Bucket**: `my-test-bucket` – *This property will be the same for both MotoServer and AWS S3. `my-test-bucket` is the bucket I will be using, but this can change according to the need.*
    - **Region**: `US West (N. California)` – *This is the region required for MotoServer. Ideally, the region will be global, but please do check your individual console configuration.*
    - **Endpoint Override URL**: `http://127.0.0.1:10001` – *This is currently used to configure MotoServer. Ideally, this can be ignored for AWS S3.*
    - The other properties can be kept as default.

2. **FetchS3Object**: This processor is used to fetch the files listed by the previous processor.

## 📂 Data Ingestion for Local
## 📂 Data Ingestion for SFTP
## 📂 Data Ingestion for MaIl

This stage of the process is in...



## 📌 Data Transformation Stage

### 1. **ExecuteStreamCommand (Preprocessing)**
The script is designed to clean and format data according to a predefined template. This ensures that data can be easily extracted and reviewed at any stage of the pipeline.  

While the current preprocessing step is simplified, a more complex scenario may involve multiple groups of files with different formats, requiring distinct processing workflows. To manage this efficiently, a **tracker file** and **consistent metadata** are essential. These components allow the implementation of individual functions tailored to each file type, ensuring the correct processing logic is applied dynamically.  

#### **Example Scenario**
Suppose the pipeline ingests three different file types:

- **Sales Data (`sales_YYYYMMDD.csv`)**  
  - Requires currency conversion and tax calculations.  

- **Customer Data (`customers_YYYYMMDD.json`)**  
  - Needs data validation and duplicate removal.  

- **Product Data (`products_YYYYMMDD.xml`)**  
  - Requires category mapping and handling of missing attributes.  

Each file type follows a different format and requires specific preprocessing steps. Instead of managing all transformations in a single script, a **tracker file** (e.g., a metadata table or a control file) can store key details such as:

- **File type**
- **Expected columns/attributes**
- **Required transformations**
- **Processing status**

Based on this metadata, the script dynamically calls the appropriate functions for each file type, ensuring **modular, scalable, and efficient data processing**.

### 2. ****

## 📌Data Loading Stage