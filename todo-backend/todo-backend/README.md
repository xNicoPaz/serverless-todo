# TO-DO Serverless Protect Backend

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml`.

## Create an environment for the project

### Install [Conda](https://docs.conda.io/en/latest/). 

1 . Download the installer:

2 . In your terminal window, run:

```bash
bash Miniconda3-latest-Linux-x86_64.sh
```
Follow the prompts on the installer screens.


### Install [poetry](https://python-poetry.org/docs/).
1 . In your terminal window, run:
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```
2 . In your terminal window, run:
```bash
todo-backend$ poetry install
```
this will download and install AWS CLI & SAM CLI
## Deploy the sample application

The Serverless Application Model Command Line Interface (SAM CLI) is an extension of the AWS CLI that adds functionality for building and testing Lambda applications. It uses Docker to run your functions in an Amazon Linux environment that matches Lambda. It can also emulate your application's build environment and API.

To use the SAM CLI, you need the following tools.

* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)   **--> Already done by Poetry**
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

To build and deploy your application for the first time, run the following in your shell:

```bash
todo-backend$ aws configure
```
enter IAM user credentials
```bash
todo-backend$ sam deploy --guided
```

This command will package and deploy your application to AWS, with a series of prompts:

* **Stack Name**: The name of the stack to deploy to CloudFormation. This should be unique to your account and region, and a good starting point would be something matching your project name.
* **AWS Region**: The AWS region you want to deploy your app to.
* **Confirm changes before deploy**: If set to yes, any change sets will be shown to you before execution for manual review. If set to no, the AWS SAM CLI will automatically deploy application changes.
* **Allow SAM CLI IAM role creation**: Many AWS SAM templates, including this example, create AWS IAM roles required for the AWS Lambda function(s) included to access AWS services. By default, these are scoped down to minimum required permissions. To deploy an AWS CloudFormation stack which creates or modifies IAM roles, the `CAPABILITY_IAM` value for `capabilities` must be provided. If permission isn't provided through this prompt, to deploy this example you must explicitly pass `--capabilities CAPABILITY_IAM` to the `sam deploy` command.
* **Save arguments to samconfig.toml**: If set to yes, your choices will be saved to a configuration file inside the project, so that in the future you can just re-run `sam deploy` without parameters to deploy changes to your application.

You can find your API Gateway Endpoint URL in the output values displayed after deployment.

## Creat DB instace

In **[THIS](https://www.youtube.com/watch?v=RerDL93sBdY)** video, there a good tutorial for instantiating de DB, and creating a security group needed to allow any or some IP addresses to access de DB. It's important to have an IAM user with EC2 full access permission tu create de security group.

## Resources

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

Next, you can use AWS Serverless Application Repository to deploy ready to use Apps that go beyond hello world samples and learn how authors developed their applications: [AWS Serverless Application Repository main page](https://aws.amazon.com/serverless/serverlessrepo/)
