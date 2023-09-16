# Geocaches Scraper
This repository contains the code for scraping Singapore geocaches data from www.geocaching.com, and seeding that into a MongoDB collection <br></br>
The `.github/workflows` directory contains a Github Action that conducts checks on code quality
using Pylint and ensures that all unit tests created can be executed successfully before a code
is merged back to main branch. <br></br>
The `scraper_function` directory contains the data cleaning scripts (and tests) packaged in a lambda function. <br></br>
The `terraform` directory contains code to automate the deployment of AWS resources for the scripts.

## Instructions to run the source code
Clone this repository to your local computer <br></br>
`git clone https://github.com/ongyongen/geocaches-scraper.git`

Navigate to the root directory and set up a virtual environment <br></br>
`python -m venv .venv`

Activate the virtual environment <br></br>
`source .venv/bin/activate`

Install the required libraries <br></br>
`pip install -r requirements.txt`

At the root directory, you can run tests on the codes using Pytest (make sure your venv is still activated) <br></br>
`python -m pytest`

At the scraper_function directory, you can run Pylint checks on the codes (make sure your venv is still activated) <br></br>
`pylint ./scripts`

Note : Ensure that Pylint's import strategy is set to `fromEnvironment` in your VSCode's Settings file <br></br>
<img width="863" alt="Screenshot 2023-09-10 at 8 27 49 PM" src="https://github.com/ongyongen/govtech-gds-data-engineering-assessment/assets/97529863/cc31a97b-0ca3-4ddf-885b-58249019ad1a">

## Instructions to deploy scripts to AWS
Ensure that you have installed terraform : https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli <br></br>
Navigate to the `terraform` directory <br></br>
Run `terraform init` to set up the terraform config files. <br></br>
Run `terraform plan` to preview the changes that Terraform plans to make to your infrastructure. <br></br>
Run `terraform apply` to execute the actions propose in Terraform plan. <br></br>
Run `terraform destroy` to remove all resources previously configured by Terraform. <br></br>

Along the way you may be promopted to provide your AWS Access Key and AWS Secret Key. <br></br>
<img width="893" alt="Screenshot 2023-09-10 at 6 31 57 PM" src="https://github.com/ongyongen/govtech-gds-data-engineering-assessment/assets/97529863/725551d3-86b5-44fc-a64a-0bb16cc35615">

## Contents in the .env file
`TF_VAR_MONGODB_URI= MONGBODB_URI` <br></br>
`TF_VAR_AWS_ACCESS_KEY= AWS_ACCESS_KEY` <br></br>
`TF_VAR_AWS_SECRET_KEY= AWS_SECRET_KEY`
