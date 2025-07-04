# Administrative Scripting Commands to create a traditional cluster
AdminTask.createCluster('[-clusterConfig [-clusterName tWASCluster1 -preferLocal true -clusterType APPLICATION_SERVER]]')
AdminTask.createClusterMember('[-clusterName tWASCluster1 -memberConfig [-memberNode rhel9-baseNode01 -memberName tWASMember1 -memberWeight 2 -genUniquePorts true -replicatorEntry false] -firstMember [-templateName default -nodeGroup DefaultNodeGroup -coreGroup DefaultCoreGroup -resourcesScope cluster]]')
AdminTask.createClusterMember('[-clusterName tWASCluster1 -memberConfig [-memberNode rhel9-baseNode02 -memberName tWASMember2 -memberWeight 2 -genUniquePorts true -replicatorEntry false]]')
# Note that scripting list commands may generate more information than is displayed by the administrative console because the console generally filters with respect to scope, templates, and built-in entries.
AdminConfig.list('ServerCluster', AdminConfig.getid( '/Cell:rhel9-baseCell01/'))
AdminConfig.save()