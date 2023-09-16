data "archive_file" "geotrails_lambda_file" {
  type = "zip"

  source_dir  = "../scraper_function"
  output_path = "../scraper_function.zip"
}

