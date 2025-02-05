resource aks 'Microsoft.ContainerService/managedClusters@2023-01-01' = {
  name: 'MyAksCluster'
  location: 'eastus'
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    dnsPrefix: 'myakscluster'
    enableRBAC: true
    agentPoolProfiles: [
      {
        name: 'systempool'
        count: 1
        enableAutoScaling: true
        minCount: 1
        maxCount: 3
        vmSize: 'Standard_DS2_v2'   
        osType: 'Linux'
        mode: 'System'
      }
    ]
  }
}
