# How to demo Modernized Runtime Extension for Java End-to-End - DRAFT

The following guide should help to do a simple end-to-end demo.
Main steps:
1. Demonstrate the application in traditional WAS
2. Analyze the application using Application Modernization Accelerator (AMA) to identify issues when migrating to Liberty
3. Fix modernization issues using the Application Modernization Accelerator Development Tools
4. Create a Liberty cluster in MoRE and deploy the application

It is based on the MoRE TechZone environment:
https://techzone.ibm.com/collection/mo-re--ama-demos-and-environment-2q25-release


## Introduction

MoRE provides the capability to continue using traditional WebSphere Application Server (tWAS) Operational Model to manage Java 17 and Java 8 applications within the same traditional WebSphere administrative environment.

<kbd>![](./images/media/MoRE_Diagram.png)</kbd>

In this demo, you will show how to extend a WebSphere ND Cell, using the MoRE feature pak, for managed Liberty servers to manage and run Java 17 / Jakarta EE 10 (subset) applications using the familiar WebSphere administrative mode and admin console.

The demo first shows an example application “Mod  Resorts” running in WebSphere ND 9.0.23. The application is a simple Java 8 application using JEE 7 APIs. 

Included with the demo, is a new version of the Mod Reports application that is built using Java 17 and Jakarta 10 EE APIs, which are supported in the managed Liberty Servers (MoRE).  




## Preparation:


### Prepare and build the maven project

1. Create a working directory and download the project

		mkdir -p ~/Student/labs
		git clone https://github.com/LarsBesselmann/sampleProjects.git ~/Student/labs

2. Switch to the directory WhereAmI_MoRE_Demo and uzip the initial project

		cd ~/Student/labs/WhereAmI_MoRE_Demo
		unzip WhereAmI-2.0.0-Project.zip

3. Switch to the WhereAmI directory 

		cd WhereAmI

4. As the modresorts project depends on was_public.jar, you must make it visible to maven to avoid build failures. Run the following command 

   	    mvn install:install-file -Dfile=./was_dependency/was_public.jar -DpomFile=./was_dependency/was_public-9.0.0.pom

    You should see a success message.

5. Build the application with maven

		mvn clean
		mvn package

	The generated war file is: target/WhereAmI-2.0.0.war


### Prepare the MoRE cell and deploy the application

1. Start the Dmgr and the two Node agents

		~/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/startManager.sh 
		~/IBM/WebSphere/AppServer/profiles/AppSrv01/bin/startNode.sh
		~/IBM/WebSphere/AppServer/profiles/AppSrv02/bin/startNode.sh

2. Create a tWAS cluster called tWASCluster1 and two members (tWASMember1, tWASMember2), one on each node.

		~/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh -lang jython -user techzone -password IBMDem0s! -f ~/Student/labs/WhereAmI_MoRE_Demo/setupScripts/tWASCluster_create.py 

3. Install the generated application war to the tWAS cluster. During installation, adjust the context root to **/tWAS**.


		~/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh -lang jython -user techzone -password IBMDem0s! -f ~/Student/labs/WhereAmI_MoRE_Demo/setupScripts/tWASCluster_WhereAmI_install.py 


4. 	Access via browser the WebSphere Admin Console via URL: https://localhost:9043/ibm/console, User ID: techzone, password: **IBMDem0s!**

5. Enable the command assistance

From the Admin Console, set the console preferences to enable command assistance and log command assistance. This will allow to see the wsadmin commands for UI driven tasks.

	a. Navigation: System administration > Console preferences

	b. Select the following options:

			Enable command assistance notifications
			Log command assistance commands


6. Start the cluster tWASCluster1

	Use either the Admin Console or the following script:

		~/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh -lang jython -user techzone -password IBMDem0s! -f ~/Student/labs/WhereAmI_MoRE_Demo/setupScripts/tWASCluster_start.py 

7. Verify that the application has been started.

	<kbd>![](./images/media/WhereAmI_tWAS_started.png)</kbd>

	<kbd>![](./images/media/WhereAmI_tWAS_deployed.png)</kbd>

8. Start the IBM HTTP Server via command

		/home/techzone/IBM/HTTPServer/bin/apachectl start

9. Access the application via IHS: http://localhost:8080/tWAS/WhereAmI

	<kbd>![](./images/media/WhereAmI_tWAS1.png)</kbd>

10. Reload the page and you should see that the application switches between the two tWAS servers.

	<kbd>![](./images/media/WhereAmI_tWAS2.png)</kbd>


### Prepare AMA

1. Start AMA

		cd ~/application-modernization-accelerator-local-4.3.0/
		scripts/startLocal.sh 

2. Open a browser and access AMA via the URL https://rhel9-base.gym.lan:3001

3. In AMA, create a workspace named **MoRE_Demo**

4. Run the data collector to create a data collection and upload it

	1. Download the data collector

	2. Extract the data collector

			cd ~/Downloads
			tar -zxvf DiscoveryTool-Linux_MoRE_Demo.tgz

	2. Start the data collector against the MoRE cell via command

			cd ~/Downloads
			transformationadvisor-4.3.0/bin/transformationadvisor -w /home/techzone/IBM/WebSphere/AppServer/
		Accept the license agreement when asked to do so.

	3. Wait until the collection has been uploaded and is available in AMA


5. Show in the **Visualization** tab that there are no dependencies to other applications

	<kbd>![](./images/media/AMA_Visualization.png)</kbd>

6. Switch to the **Assessment** tab that the application can be migrated to MoRE but has some issues that must be fixed.

	<kbd>![](./images/media/AMA_Assessment.png)</kbd>

7. Switch back to the **Visualization** tab.


## Demo the end-to-end flow


### Demo the application running in tWAS

1. 	Access via browser the WebSphere Admin Console via URL: https://localhost:9043/ibm/console, User ID: techzone, password: **IBMDem0s!**

2. Show that the application has been started.

	<kbd>![](./images/media/WhereAmI_tWAS_started.png)</kbd>

	<kbd>![](./images/media/WhereAmI_tWAS_deployed.png)</kbd>

3. Access the application via IHS: http://localhost:8080/tWAS/WhereAmI

	<kbd>![](./images/media/WhereAmI_tWAS1.png)</kbd>

4. Reload the page and you should see that the application switches between the two tWAS servers.

	<kbd>![](./images/media/WhereAmI_tWAS2.png)</kbd>


### Demo the assessment via AMA

1. Explain that the data colection has been created before to save time

2. Show in the **Visualization** tab that there are no dependencies to other applications

	<kbd>![](./images/media/AMA_Visualization.png)</kbd>

3. Switch to the **Assessment** tab that the application can be migrated to MoRE but has some issues that must be fixed.

	<kbd>![](./images/media/AMA_Assessment.png)</kbd>

4. Select MoRE as as target, then click on the WhereAmI application to get more insight about the issues

	<kbd>![](./images/media/AMA_WhereAmI_Assessment1.png)</kbd>

	<kbd>![](./images/media/AMA_WhereAmI_Assessment2.png)</kbd>

	<kbd>![](./images/media/AMA_WhereAmI_Assessment3.png)</kbd>

5. Generate and download the migrationplan so that you can re-use it in AMA Dev Tools

	<kbd>![](./images/media/AMA_WhereAmI_Migrationplan.png)</kbd>


## Demo how to use the AMA Dev Tools to apply automated fixes

1. In a terminal window, switch to the WhereAmI directory and open VS Code

		cd WhereAmI_JavaEE_Project/WhereAmI
		code .

2. Change in the pom.xml file the version from 2.0.0 to 2.0.1

3. Start the AMA Dev Tool modernization wizard for target Liberty

	<kbd>![](./images/media/AMADevTool_ModernizationWizard1.png)</kbd>


4. Upload the AMA generated migration plan into AMA Dev Tools

	<kbd>![](./images/media/AMADevTool_ModernizationWizard2.png)</kbd>

5. Add the generated server.xml file which was generated by AMA and helps to test the application in development on Liberty.

	<kbd>![](./images/media/AMADevTool_ModernizationWizard3.png)</kbd>

6. Take a look at the identified modernization issues which are mainly in the are ap automated fixes

	<kbd>![](./images/media/AMADevTool_ModernizationWizard4.png)</kbd>

	Click on **Run automated fixes** to fix those issues.

7. Click on Rebuild and refresh and you will see that also the self-directed issue has been resolved.

	<kbd>![](./images/media/AMADevTool_ModernizationWizard5.png)</kbd>



## Set up the managed Liberty cluster

1. Create a managed Liberty cluster named managedLibertyCluster1

	<kbd>![](./images/media/MoRE_createCluster1.png)</kbd>

	<kbd>![](./images/media/MoRE_createCluster2.png)</kbd>

2. Create the first cluster member on the first node based on the managed Liberty server template.
	
	<kbd>![](./images/media/MoRE_createCluster3.png)</kbd>

3. Add another cluster member, this time on the sevcond node.

	<kbd>![](./images/media/MoRE_createCluster4.png)</kbd>

	<kbd>![](./images/media/MoRE_createCluster5.png)</kbd>

4. Review the summary to make sure the servers are placed correctly

	<kbd>![](./images/media/MoRE_createCluster6.png)</kbd>


5. Before saving the cluster, take a look at the wsadmin script.

	<kbd>![](./images/media/MoRE_createCluster8.png)</kbd>

6. Save the settings

	<kbd>![](./images/media/MoRE_createCluster7.png)</kbd>

7. CLick on the cluster name

	<kbd>![](./images/media/MoRE_reviewCluster1.png)</kbd>


8. Review the configuration

	<kbd>![](./images/media/MoRE_reviewCluster2.png)</kbd>

9. Take a look at the local topology.

	<kbd>![](./images/media/MoRE_reviewCluster3.png)</kbd>


10. Review the ports and add missing HTTP ports to the virtual hosts

	<kbd>![](./images/media/MoRE_ports1.png)</kbd>

	<kbd>![](./images/media/MoRE_ports2.png)</kbd>

	<kbd>![](./images/media/MoRE_ports3.png)</kbd>


## Deploy the application

1. Select the updated WhereAmI application (which has the version 2.0.1) and select Liberty as target runtime

	<kbd>![](./images/media/MoRE_deployApp1.png)</kbd>

2. Choose the Fast Path deployment and leave the defaults for the name

	<kbd>![](./images/media/MoRE_deployApp2.png)</kbd>

	<kbd>![](./images/media/MoRE_deployApp3.png)</kbd>

3. Map the application to the Liberty cluster and the IBM HTTP Server

	<kbd>![](./images/media/MoRE_deployApp4.png)</kbd>


4. Leave the default host

	<kbd>![](./images/media/MoRE_deployApp5.png)</kbd>

5. Change the context root to **/liberty**

	<kbd>![](./images/media/MoRE_deployApp6.png)</kbd>

6. Review the summary

	<kbd>![](./images/media/MoRE_deployApp7.png)</kbd>


7. Take a look at the wsadmin script

	<kbd>![](./images/media/MoRE_deployApp8.png)</kbd>

8. Finally save the application. It should be listed as stopped.

	<kbd>![](./images/media/MoRE_deployApp9.png)</kbd>


## Start the cluster and test the application

1. Start the cluster

	<kbd>![](./images/media/MoRE_runApplication1.png)</kbd>


2. Review the wsadmin script

	<kbd>![](./images/media/MoRE_runApplication2.png)</kbd>


3. Access the application via IBM HTTP Server

	<kbd>![](./images/media/MoRE_runApplication3.png)</kbd>

4. Reload the page and you should see that it switches been both Liberty instances.

	<kbd>![](./images/media/MoRE_runApplication4.png)</kbd>


**This concludes the demo**
You should have seen how easy it can be to migrate an application from traditional WAS to managed Liberty and that you could use the same operational model in managed Liberty.


## Cleanup

### Clean up AMA

1. In AMA, delete the AMA workspace **MoRE_Demo**

2. Stop AMA

		cd ~/application-modernization-accelerator-local-4.3.0/
		scripts/stopLocal.sh 
		
3. Remove the data collector 

		rm -rf ~/Downloads/DiscoveryTool-Linux_MoRE_Demo.tgz
		rm -rf ~/Downloads/DiscoveryTool-Linux_MoRE_Demo
		rm -rf ~/Downloads/WhereAmI-2_0_0_war.ear_migrationPlan.zip

### Cleanup WebSphere

1. Uninstall the WhereAmI application

		~/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh -lang jython -user techzone -password IBMDem0s! -f ~/Student/labs/WhereAmI_MoRE_Demo/setupScripts/tWASCluster_WhereAmI_uninstall.py 

2. Delete the tWAS cluster called tWASCluster1 and the two members (tWASMember1, tWASMember2).

		~/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/wsadmin.sh -lang jython -user techzone -password IBMDem0s! -f ~/Student/labs/WhereAmI_MoRE_Demo/setupScripts/tWASCluster_delete.py 

3. Stop the IBM HTTP Server via command

		/home/techzone/IBM/HTTPServer/bin/apachectl stop


4. Stop the Dmgr and the two Node agents

		~/IBM/WebSphere/AppServer/profiles/AppSrv02/bin/stopNode.sh
		~/IBM/WebSphere/AppServer/profiles/AppSrv01/bin/stopNode.sh
		~/IBM/WebSphere/AppServer/profiles/Dmgr01/bin/stopManager.sh 

### Remove the lab assests
1. Close VS Code

2. Remove the project directory

		cd ~
		rm -rf ~/Student/labs


