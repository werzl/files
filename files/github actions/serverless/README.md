# CD Pipeline for Serverless Lambda Functions
The Continuous Deployment workflow runs on a merge into master. 
The 'deploy' task uses Yarn to install modules, and then run the automated test script from a package.json file, and if all tests pass, the serverless framework is installed, and then used to deploy the Lambda Functions and API Gateway configurations to the AWS account specified from the repository's secrets.

## Prerequisites
Needs both "build" and "test" scripts present in the package.json file in your repo.
