How to demo MoRE - DRAFT

## Preparation:

1. mkdir -p ~/Student/labs

		git clone https://github.com/LarsBesselmann/sampleProjects.git

2. Switch to the directory WhereAmI_MoRE_Demo and uzip the initial project

		cd WhereAmI_MoRE_Demo

		unzip WhereAmI-2.0.0-Project.zip

3. Switch to the WhereAmI directory 

	cd WhereAmI_JavaEE_Project/WhereAmI

4. Build the application with maven

		mvn clean
		mvn package

	The generated war file is: target/WhereAmI-2.0.0.war

5. Create a tWAS cluster called tWASCluster1 and 2 members, one on each node.

6. Deploy the war file to the tWAS cluster, set the context root to **/tWAS**

7. Start the application.

	<kbd>![](./images/media/WhereAmI_tWAS_started.png)</kbd>

	<kbd>![](./images/media/WhereAmI_tWAS_deployed.png)</kbd>

7. Start the IBM HTTP Server via 

		/home/techzone/IBM/HTTPServer/bin/apachectl start

8. Access the application via IHS: http://localhost:8080/tWAS/WhereAmI

	<kbd>![](./images/media/WhereAmI_tWAS1.png)</kbd>

9. Reload the page and you should see that the application switches between the two tWAS servers.

	<kbd>![](./images/media/WhereAmI_tWAS2.png)</kbd>

## Analysis using AMA

1. In AMA, create a workspace named **MoRE_Demo**

2. Download the data collector (tar -zxvf DiscoveryTool-Linux_MoRE_Demo.tgz )

3. run the data collector against the MoRE cell via command

		transformationadvisor-4.3.0/bin/transformationadvisor -w /home/techzone/IBM/WebSphere/AppServer/

4. Wait until the collection has been uploaded and is available in AMA

5. Show in the **Visualization** tab that there are no dependencies to other applications

	<kbd>![](./images/media/AMA_Visualization.png)</kbd>

6. Switch to the **Assessment** tab that the application can be migrated to MoRE but has some issues that must be fixed.

	<kbd>![](./images/media/AMA_Assessment.png)</kbd>

7. Get more insight about the issues

	<kbd>![](./images/media/AMA_WhereAmI_Assessment1.png)</kbd>

	<kbd>![](./images/media/AMA_WhereAmI_Assessment2.png)</kbd>

	<kbd>![](./images/media/AMA_WhereAmI_Assessment3.png)</kbd>

8. Generate and download the migrationplan so that you can re-use it in AMA Dev Tools

	<kbd>![](./images/media/AMA_WhereAmI_Migrationplan.png)</kbd>


## Use AMA Dev Tools to apply automated fixes

Create a managed Liberty cluster named managedLibertyCluster1, add two cluster members based on the default-managed-liberty-server template
Click on managedLibertyCluster1 and show the local topology




