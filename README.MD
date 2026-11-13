install aws CLI
install terraform

#

terraform init # downloads providers
terraform plan # preview changes
terraform apply # type "yes" to confirm

# clean

terraform destroy

aws lambda invoke --function-name iaac-script --payload '{}' \
 --cli-binary-format raw-in-base64-out out.json && cat out.json


 aws lambda invoke --function-name iaac-script --payload '{"message" : "HelloWorld from Terraform"}' --cli-binary-format raw-in-base64-out response.json

aws lambda invoke \
  --function-name iaac-script \
  --cli-binary-format raw-in-base64-out \
  --payload '{"message": "Hello World From Terraform"}' \
  out.json && cat out.json


aws lambda invoke --function-name iaac-script --cli-binary-format raw-in-base64-out --payload "{\"message\": \"Hello World From Terraform\"}" out.json && type out.json

worked ---

C:\Ayesha\AI-projects-git-repo\iaac-terraform>aws lambda invoke --function-name iaac-script --cli-binary-format raw-in-base64-out --payload "{\"message\": \"Hello World From Terraform\"}" out.json && type out.json
{
    "StatusCode": 200,
    "ExecutedVersion": "$LATEST"
}

{"statusCode": 200, "body": "{\"message\": \"Running python script on lambda using Terraform\"}"}

terraform destroy



usage: aws [options] <command> <subcommand> [<subcommand> ...] [parameters]
To see help text, you can run:

  aws help
  aws <command> help
  aws <command> <subcommand> help

Unknown options: out.json, HelloWorld from Terraform}'


aws logs tail /aws/lambda/iaac-script --follow


echo "# iaac-terraform" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Ayesha2021/iaac-terraform.git
git push -u origin main

git remote add origin https://github.com/Ayesha2021/iaac-terraform.git
git branch -M main
git push -u origin main


git 
remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
remote: pre-receive hook declined
To https://github.com/Ayesha2021/iaac-terraform.git

git filter-branch --force --index-filter "git rm --cached -r --ignore-unmatch .terraform/" --prune-empty --tag-name-filter cat -- --all
git add .gitignore
git commit -m "Add .gitignore for Terraform"




