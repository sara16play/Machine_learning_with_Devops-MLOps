# Machine_learning_with_Devops-MLOps

In this Project we have integrated the Machine Learning with the Devops as there are so many machine learning projects that never integrated due to the training time of the machine learning

# Task description

1.	Create container image that’s has Python3 and Keras or numpy  installed  using dockerfile 

2.	When we launch this image, it should automatically starts train the model in the container.

3.	Create a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins 

4.	 Job1 : Pull  the Github repo automatically when some developers push repo to Github.

5.	 Job2 : By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter install image container to deploy code  and start training( eg. If code uses CNN, then Jenkins should start the container that has already installed all the softwares required for the cnn processing).

6.	Job3 : Train your model and predict accuracy or metrics.

7.	Job4 : if metrics accuracy is less than 80%  , then tweak the machine learning model architecture.

8.	Job5: Retrain the model or notify that the best model is being created

9.	Create One extra job job6 for monitor : If container where app is running. fails due to any reason then this job should automatically start the container again from where the last trained model left

## My Solution for this problem is:
 

### Initial steps:

* Create the repository from where developer will push the code.

* Configure the hooks so that whenever the developer commit the code it will automaically puch the code to github.

### Step 1: Creating the tensorflow installed image:

![](ten.png)

* Here we are using the centos as the base os for the tensorflow.

### Step 2: Creating the sklearn installed image:

![](sk.png)

* Here we are using the centos as the base os for the sklearn.

### Step 3: Creating the Tensorflow and sklearn image from the Docker files:

![](d1.png)

![](d2.png)

### Step 4: Pushing from the Git by developers: 

![](1.png)

### Step 5: Creating the job chain using build pipeline:

![](2.png)

* Now let us discuss about all the jobs:

### Job 1: It will pull the files from the github whenever the developer push the code.

![](2.png)

```
sudo rm -rf  /mlops
sudo mkdir /mlops
sudo cp -vfr * /mlops
```

### Job 2: It is the main job of this task/project. It will train the model which is written by the coder and pushed in github, after this if the accuracy is not matched with the desired accuracy by the coder then it will execute the another file internelly (in my case it is print.py) actually it will tweak the program by changing the dense layers, it add the extra dense layer and check the accuracy, if the accuracy is not matched then it will add one more and it will continue and I have putted till to add 3 extra dense layers and if it don't get desired accuracy, then it will save the model with the higest accuracy it achived and also create a file with the message.

![](j2.png)

![](j2.2.png)

![](j2.3.png)

![](3.png)

![](3.1.png)

![](3.2.png)

![](3.3.png)

![](3.4.png)

* And if by some reason job 2 failed or there is any error in the program it will trigger the job 5 and this will again try to do the same and if it again fails then the job 3 will trigger and an email will sent to the programmer and the user that something had happened wrong.

![](3e.png)

![](j2.4.png)

* Code

```
sudo cd /mlops/
if cat /mlops/model.py | grep mnist
then
echo "finded"
if sudo docker ps -a | grep keras_mnist
then
sudo docker rm -f keras_mnist
sudo docker run -t -v /mlops/:/root/ --name keras_mnist tensorflow:cnn python2 /root/model.py
else
sudo docker run -t -v /mlops/:/root/ --name keras_mnist tensorflow:cnn python2 /root/model.py
fi
fi


if cat /mlops/model.py | grep from\ sklearn
then
echo "finded"
if sudo docker ps -a | grep sklearn
then
sudo docker rm -f sklearn
sudo docker run -t -v /mlops/:/root/ --name sklearn sklearn:lin python2 /root/model1.py
else
sudo docker run -t -v /mlops/:/root/ --name sklearn sklearn:lin python2 /root/model1.py
fi
fi
```

### Job 3: It's work is only to send the mail if the job 2 and 5 fails.

![](j3.png)

![](j3.1.png)

* Code

```
sudo python3 /mlops/failmail.py
```

### Job 4: This will trigger if the job 2 build successfully and this will send the mail regarding the accuracy and the model it created after training.

![](j4.png)

![](j4.1.png)

![](j4.2.png)

* Code

```
if cat /mlops/model.txt | grep model\ can
then
sudo python3 /mlops/semisuccessmail.py
sudo python3 /mlops/trainmodel.py
elif cat /mlops/model.txt | grep we\ have\ added
then
sudo python3 /mlops/successmail.py
sudo python3 /mlops/trainmodel.py
elif cat /mlops/model.txt | grep the\ model\ has 
then
sudo python3 /mlops/successmail.py
sudo python3 /mlops/trainmodel.py
fi
```

### Job 5: This will run only if the job 2 fails and it will launch the docker if by some reason docker stops or if it again fails then it will send the mail to the developer about failer using job 3.

![](j5.png)

![](j5.1.png)

![](j5.2.png)

* Code

```
sudo cd /mlops/
if cat /mlops/model.py | grep mnist
then
echo "finded"
if sudo docker ps -a | grep keras_mnist
then
sudo docker rm -f keras_mnist
sudo docker run -t -v /mlops/:/root/ --name keras_mnist tensorflow:cnn python2 /root/model.py
else
sudo docker run -t -v /mlops/:/root/ --name keras_mnist tensorflow:cnn python2 /root/model.py
fi
fi


if cat /mlops/model.py | grep from\ sklearn
then
echo "finded"
if sudo docker ps -a | grep sklearn
then
sudo docker rm -f sklearn
sudo docker run -t -v /mlops/:/root/ --name sklearn sklearn:lin python2 /root/model1.py
else
sudo docker run -t -v /mlops/:/root/ --name sklearn sklearn:lin python2 /root/model1.py
fi
fi
```

## Some Extra ScreenShots:

![](model.png)

![](twe.png)

![](mail.png)

## Built With

* RHEL-8 Running in Virtual Box
* Docker
* Dockerfile
* Git & GitHub
* Jenkins

## Author

[SAURAV PATEL](https://www.linkedin.com/in/saurav-patel-148539151/)
