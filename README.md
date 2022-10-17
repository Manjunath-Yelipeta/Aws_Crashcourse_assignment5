## 📌  AWS Crash Course


**Instructions to run the container**

The Docker image has been pused to the AWS Elastic Container Registry (ECR). 

- Image and tagname of the repo in AWS ECR:

```
public.ecr.aws/g2k0e8z5/aws-deployment-abhiram-team
```

- To run the container stored on the ECR and access the model as web app, run the below command

```
docker run -it -p 80:80 public.ecr.aws/g2k0e8z5/aws-deployment-abhiram-team
```
