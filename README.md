![diagram-export-11-29-2023-8_00_52-PM](https://github.com/PranitRout07/Automated-EC2-Instance-Stop-Notifications-via-Email/assets/102309095/ea162d8f-cae1-4f62-8b97-b4cf6c406920)

# Steps followed

1. Create EC2 instance
2. Create SNS topic
3. Create IAM Role for Lambda to access SNS topic and CloudWatch logs
4. Create a Lambda function using Python
5. Create a CloudWatch event trigger



####

1. Created a ec2 instance
<img width="1267" alt="Screenshot 2023-11-30 160512" src="https://github.com/PranitRout07/Automated-EC2-Instance-Stop-Notifications-via-Email/assets/102309095/a0851f42-9ef1-4f8c-a208-55542cc471fc">

2.Created a SNS topic
<img width="1266" alt="Screenshot 2023-11-30 160411" src="https://github.com/PranitRout07/Automated-EC2-Instance-Stop-Notifications-via-Email/assets/102309095/a4fb1281-0c66-4ffd-80aa-00ba8643b21f">

3.Created a subscription fot the SNS topic . Here i used email as protocol . 
<img width="1265" alt="Screenshot 2023-11-30 160537" src="https://github.com/PranitRout07/Automated-EC2-Instance-Stop-Notifications-via-Email/assets/102309095/66d46d38-2693-4426-b0b1-03e3edfdd16b">

4.Confirmed the subscription. 
<img width="1034" alt="Screenshot 2023-11-30 160609" src="https://github.com/PranitRout07/Automated-EC2-Instance-Stop-Notifications-via-Email/assets/102309095/276b9227-aaa3-4a00-8898-382c81d1504f">

5.Created policy for SNS service and Cloudwatch logs
<img width="1268" alt="Screenshot 2023-11-30 160808" src="https://github.com/PranitRout07/Automated-EC2-Instance-Stop-Notifications-via-Email/assets/102309095/068da52a-a6c6-4505-9a91-534277b4f65d">

<img width="1264" alt="Screenshot 2023-11-30 160831" src="https://github.com/PranitRout07/Automated-EC2-Instance-Stop-Notifications-via-Email/assets/102309095/85a80c0e-ba1f-4ba8-a394-9d6ff54f3d5e">

6.Created a role for lambda service
<img width="1265" alt="Screenshot 2023-11-30 160939" src="https://github.com/PranitRout07/Automated-EC2-Instance-Stop-Notifications-via-Email/assets/102309095/a89705a5-cecc-4417-b9da-0907f133e9f0">

7.Attached policy to the role created
<img width="1267" alt="Screenshot 2023-11-30 160959" src="https://github.com/PranitRout07/Automated-EC2-Instance-Stop-Notifications-via-Email/assets/102309095/ec014bc2-463e-4549-81ee-e92aab5cf74f">















