targetScope='subscription'


resource AKSResGroup 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  name: 'DeploymentRG'
  location: 'eastus'
}
