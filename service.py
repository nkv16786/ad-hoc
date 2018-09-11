{
"$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
  "contentVersion": "1.0.0.0",
  "parameters": {
    "ServerName": {
      "type": "string",
      "defaultValue": "yourservername2"
    },
    "DbUser": {
      "type": "string",
      "defaultValue": "VeryWiseAdmin",
      "minLength": 1
    },
    "DbPassword": {
      "type": "securestring",
      "defaultValue": "ReplaceWithTheMostSecurePasswordThatEverExisted&NeverShareLikeThisWithAnyone!"
    },
    "DbName": {
      "type": "string",
      "defaultValue": "dbname",
      "minLength": 1
    }
  },
  "variables": {
  },
  "resources": [
    {
      "name": "[parameters('ServerName')]",
      "type": "Microsoft.Sql/servers",
      "location": "West Europe",
      "apiVersion": "2014-04-01-preview",
      "properties": {
        "administratorLogin": "[parameters('DbUser')]",
        "administratorLoginPassword": "[parameters('DbPassword')]",
        "version": "12.0"
      },
      "resources": [

        {
          "name": "[concat(parameters('ServerName'),'/',parameters('DbName'))]",
          "type": "Microsoft.Sql/servers/databases",
          "location": "West Europe",
          "apiVersion": "2014-04-01-preview",
          "dependsOn": [
            "[resourceId('Microsoft.Sql/servers', parameters('ServerName'))]"
          ]
        }
      ]
    }
  ],
  "outputs": {
    "ServerName": {
      "type": "string",
      "value": "[parameters('ServerName')]"
    },
    "ServerResourceID": {
      "type": "string",
      "value": "[resourceId('Microsoft.Sql/servers', parameters('ServerName'))]"
    },
        "SqlServerURL": {
      "type": "string",
      "value": "[reference(parameters('ServerName')).fullyQualifiedDomainName]"
    },
    "DbResourceID": {
      "type": "string",
      "value": "[resourceId('Microsoft.Sql/servers/databases', parameters('ServerName'), parameters('DbName'))]"
    },

    "DbConnString": {
      "type": "string",
      "value": "[concat('Server=tcp:',reference(parameters('ServerName')).fullyQualifiedDomainName,',1433;Initial Catalog=',parameters('DbName'),';Persist Security Info=False;User ID=',reference(parameters('ServerName')).administratorLogin,';Password=',reference(parameters('ServerName')).administratorLoginPassword,';MultipleActiveResultSets=False;Encrypt=True;TrustServerCertificate=False;Connection Timeout=30;')]"
    }
  }

}
