provider "aws" {
    region = "us-east-1"
}

resource "aws_lambda_function" "test_lambda" {
  filename      = "lambda_function.zip"
  function_name = "lambda_function"
  role          = "arn:aws:iam::713287746880:role/service-role/adsf"
  handler       = "exports.test"

  # The filebase64sha256() function is available in Terraform 0.11.12 and later
  # For Terraform 0.11.11 and earlier, use the base64sha256() function and the file() function:
  # source_code_hash = "${base64sha256(file("lambda_function_payload.zip"))}"
  source_code_hash = "${filebase64sha256("lambda_function.zip")}"

  runtime = "python2.7"

  environment {
    variables = {
      foo = "bar"
    }
  }
}