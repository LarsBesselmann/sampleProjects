How to demo MoRE - DRAFT

Preparation:
1. mkdir -p ~/Student/labs
git clone https://github.com/LarsBesselmann/sampleProjects.git

1. Unzip WhereAmI_JavaEE_Project.zip
2. Switch to the WhereAmI directory 
	cd WhereAmI_JavaEE_Project/WhereAmI
2. Build the application with maven
	mvn clean
	mvn package
3. The generated war file is: target/WhereAmI-2.0.0.war
4. Deploy the war file to a tWAS cluster named tWASCluster1 within the MoRE cell
	Context root: demo
5. Start the IBM HTTP Server via /home/techzone/IBM/HTTPServer/bin/apachectl start
6. Access the application via IHS: http://localhost:8080/demo/WhereAmI
7. Reload the page and you should see that the server switches between the two tWAS servers

Analysis using AMA
1. In AMA, create a workspace
2. Download the data collector (tar -zxvf DiscoveryTool-Linux_MoRE_Demo.tgz )
3. run the data collector against the MoRE cell (transformationadvisor-4.3.0/bin/transformationadvisor -w /home/techzone/IBM/WebSphere/AppServer/)
4. Wait until the collection has been uploaded and is available in AMA
5. Show in the Visualization tab that there are no dependencies to other applications
6. Show in AMA Assessment tab that the application can be migrated to MoRE but has some issues

Use AMA Dev Tools to apply automated fixes

Create a managed Liberty cluster named managedLibertyCluster1, add two cluster members based on the default-managed-liberty-server template
Click on managedLibertyCluster1 and show the local topology




