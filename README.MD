install aws CLI
install terraform

#

terraform init # downloads providers
terraform plan # preview changes
terraform apply # type "yes" to confirm

# clean

terraform destroy

testing lambda from CLI.

aws lambda invoke \
 --function-name iaac-script \
 --cli-binary-format raw-in-base64-out \
 --payload '{"message": "Hello World From Terraform"}' \
 out.json && cat out.json

aws lambda invoke --function-name iaac-script --cli-binary-format raw-in-base64-out --payload "{\"message\": \"Hello World From Terraform\"}" out.json && type out.json

worked ---

> aws lambda invoke --function-name iaac-script --cli-binary-format raw-in-base64-out --payload "{\"message\": \"Hello World From Terraform\"}" out.json && type out.json
> {
> "StatusCode": 200,
> "ExecutedVersion": "$LATEST"
> }

{"statusCode": 200, "body": "{\"message\": \"Running python script on lambda using Terraform\"}"}

terraform destroy
