# Create S3 bucket to store the lambda zip file
resource "aws_s3_bucket" "geotrails_scraper_bucket" {
  bucket = "geotrails-scraper-bucket"
}

resource "aws_s3_object" "geotrails_lambda_object" {
  bucket = aws_s3_bucket.geotrails_scraper_bucket.id

  key    = "scraper_function.zip"
  source = data.archive_file.geotrails_lambda_file.output_path

  etag = filemd5(data.archive_file.geotrails_lambda_file.output_path)
}

# Create an IAM role for the scraper lambda function 
resource "aws_iam_role" "geotrails_lambda_role" {
  name = "lambda-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

# Create an AWS Lambda Layer using the ZIP file
resource "aws_lambda_layer_version" "geotrails_lambda_layer" {
  layer_name          = "restaurants_lambda_layer" # Name for your Lambda Layer
  compatible_runtimes = ["python3.8"]              # List of compatible runtimes

  # Specify the ZIP file for your layer
  filename = var.python_custom_layer_filepath
}

# Create the lambda function to scrape the geocaches
resource "aws_lambda_function" "geotrails_scraper_lambda_function" {
  function_name = "geotrails-scraper-lambda-function"

  s3_bucket = aws_s3_bucket.geotrails_scraper_bucket.id
  s3_key    = aws_s3_object.geotrails_lambda_object.key

  role    = aws_iam_role.geotrails_lambda_role.arn
  handler = "lambda_function.lambda_handler"

  runtime          = "python3.7"
  source_code_hash = data.archive_file.geotrails_lambda_file.output_base64sha256

  timeout = 100

  environment {
    variables = {
      MONGODB_URI = var.MONGODB_URI,
    }
  }

  layers = [
    var.python37_layer_arn,
    aws_lambda_layer_version.geotrails_lambda_layer.arn
  ]
}

# Connect lambda function to an EventBridge (run lambda function Mon to Fri 5pm)
resource "aws_cloudwatch_event_rule" "geotrails_scraper_lambda_event_rule" {
  name                = "geotrails-scraper-lambda-event-rule"
  description         = "retry scheduled every 2 min"
  schedule_expression = "cron(0 17 ? * MON-FRI *)"
}

resource "aws_cloudwatch_event_target" "profile_generator_lambda_target" {
  arn  = aws_lambda_function.geotrails_scraper_lambda_function.arn
  rule = aws_cloudwatch_event_rule.geotrails_scraper_lambda_event_rule.name
}

resource "aws_lambda_permission" "allow_cloudwatch_to_call_rw_fallout_retry_step_deletion_lambda" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.geotrails_scraper_lambda_function.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.geotrails_scraper_lambda_event_rule.arn
}
