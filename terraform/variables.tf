variable "AWS_ACCESS_KEY" {
}

variable "AWS_SECRET_KEY" {
}

variable "MONGODB_URI" {
}

variable "region" {
    default = "ap-southeast-1"
}

variable "python37_layer_arn" {
    default = "arn:aws:lambda:ap-southeast-1:336392948345:layer:AWSSDKPandas-Python37:5"
}

variable "python_custom_layer_filepath" {
    default = "./python.zip"
}