#Jenkins-Project: This project for Continuous Integration using tools like: 

->GIT

->Github

->Jenkins:Jenkins is an open source automation tool written in Java with plugins built for " Continuous Integration " purpose



**Steps to be followed for this project:

1.Clone this repository. 

2.Install Java JDK for before installing Jenkins (Note:Only Java JDK 8-11 are supported by Jenkins,so install any Java JDK between 8 to 11).Go to Jenkins website and download "jenkins.jar" file.   

3.After completion of Java installion,go to command prompt.Type "java -version" to check if java is completly installed and to verify your installed version is between 8 to 11.

4.Then type "java -jar 'drag and drop the jar file to command prompt' ". (Example: java -jar c:\system\downloads\jenkins.jar)

5.Jenkins runs in localhost:8080 by default. Go to this location.

6.Add or fill your credentials.

7.After that you're prompted to Jenkins enivronment. Go to Manage Jenkins that is displayed  in left side.

8.Go to Manage Plugins(here you can see all the jenkins plugins).Go to available and look for  HTML publisher in search.

**To Create first job:

9.Click on new item,Enter name of the job and choose Freestyle Project(which is useful for easy configuration for beginners),then click ok.

10.Click on Compile Job or the name of the job,click on configure,then source code management,choose GIT and it asks for GIT Repo.

11.Paste your git repo(make sure GIT is alredy installed to avoid errors during the building of triggers).

12.Go to build and choose "Invoke top level Maven Target" (Maven should be installed to avoid any errors during this part of build).

13.Then click on Apply,Save it,And go to  dashboard and Click on Build Now.

14.After the successful compliation,now its  time to Deploy the build on Test Server.

**For  Review Job: 

15.Click on new item,Enter name of the job and choose Freestyle Project(which is useful for easy configuration for beginners),then click ok.

16.Click on Review Job or the name of the job,click on configure,then source code management,choose GIT and it asks for GIT Repo.

17.Paste your git repo(make sure GIT is alredy installed to avoid errors during the building of triggers).

18.Go to build and choose "Invoke top level Maven Target" (Maven should be installed to avoid any errors during this part of build).

19.In order to review code type:"-P matrix omd:pmd" in goals.(This is used to produce all the warnings and erros present in the code. 

20.GO to post build actions and select Publish HTML reports.

21.Apply and save it.And go to dashboard and click on Build now

**For Test Job:

22.Click on new item,Enter name of the job and choose Freestyle Project(which is useful for easy configuration for beginners),then click ok.

23.Click on Review Job or the name of the job,click on configure,then source code management,choose GIT and it asks for GIT Repo.

24.Paste your git repo(make sure GIT is alredy installed to avoid errors during the building of triggers).

25.Go to build and choose "Invoke top level Maven Target" (Maven should be installed to avoid any errors during this part of build).

26.In order to test the code type:"test" in goals.

27.Apply and save it.And go to dashboard and click on Build now



**To build a Pipeline:

28.Go to Manage Jenkins,then Global Management Tools and install "Pipeline View".

29.Then click on '+' symbol which is present beside the "ALL"  in Jenkins Dashboard.

30.Choose the "Build Pipeline View".Select the initial job as your firest job.

31.Then Click  on "Ok".

32.To add more jobs to pipeline.Click on Review Job,configure and click on Build Triggers.Select "build after other projects are built".In projects to watch enter your Compile Job.

33.Click on Apply and Save.

34.Then Run the pipeline.



![jenkins-1](https://user-images.githubusercontent.com/59798427/130254976-e7e0bf89-30ed-4695-a5b6-59f859962d30.jpg)





