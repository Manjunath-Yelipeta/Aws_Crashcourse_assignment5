## 📌  AWS Crash Course

**DockerFile**

- The Dockerfile has been configured to use GRADIO SERVER. 
- This will enable to run the model inference ("demo_scripted.py") as a web application on the GRADIO app.

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
