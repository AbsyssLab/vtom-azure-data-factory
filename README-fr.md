# Connecteur Azure Data Factory
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE.md)&nbsp;
[![fr](https://img.shields.io/badge/lang-en-red.svg)](README.md)  

Cette intégration permet de déclencher et de surveiller les pipelines Azure Data Factory à partir de Visual TOM.

# Disclaimer
Aucun support ni garanties ne seront fournis par Absyss SAS pour ce projet et fichiers associés. L'utilisation est à vos propres risques.

Absyss SAS ne peut être tenu responsable des dommages causés par l'utilisation d'un des fichiers mis à disposition dans ce dépôt Github.

Il est possible de faire appel à des jours de consulting pour l'implémentation.

# Prérequis

  * Visual TOM 7.1.2 ou plus
  * Python 3.x ou plus
  * Azure Data Factory resource
  * Installer les packages python requis avec pip:
    ```bash
    pip install -r requirements.txt
    ```
  * Agent Unix (l'utilisation sous Windows sera disponible plus tard)

# Consignes

  * Créer une application Azure et définir les variables d'environnement suivantes dans config.py dans le même dossier (un template est disponible dans le dépôt):
    * `AZURE_SUBSCRIPTION_ID`: Subscription ID de votre Azure subscription
    * `AZURE_TENANT_ID`: Tenant ID de votre Azure Active Directory
    * `AZURE_CLIENT_ID`: Client ID de votre application Azure Active Directory
    * `AZURE_CLIENT_SECRET`: Secret client de votre application Azure Active Directory
    * `AZURE_DATA_FACTORY_RESOURCE_GROUP`: Resource group de votre Azure Data Factory
  * Créer dans Visual TOM une connexion "Custom Application" avec la définition suivante ou importer le fichier MyApplication-AzureDataFactory.xml:
  ```bash
  vtimport -x -f MyApplication-AzureDataFactory.xml
  ```
  ![Custom application screenshot](screenshots/Azure_DataFactory_CustomApplication.png?raw=true)
  * Créer la queue batch sur les Agents et mettre à jour le submitter avec le chemin réel de azureDataFactory.py

Description des paramètres:
  * Data Factory: Nom du Data Factory
  * Pipeline: Nom de la pipeline à déclencher
  * Parameters (optionnel): Fichier JSON ou chaîne JSON courte contenant les paramètres à passer à la pipeline
    * En cas de chaîne JSON, le paramètre doit commencer par "E<>|" pour éviter l'erreur "Ressource non trouvée"

L'intégration retourne des codes spécifiques pour les erreurs:
  * 90: Paramètres incorrects
  * 99: Activité au statut "failed" ou "cancelled"

# Licence
Ce projet est sous licence Apache 2.0. Voir le fichier [LICENCE](license) pour plus de détails.


# Code de conduite
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-v2.1%20adopted-ff69b4.svg)](code-of-conduct.md)  
Absyss SAS a adopté le [Contributor Covenant](CODE_OF_CONDUCT.md) en tant que Code de Conduite et s'attend à ce que les participants au projet y adhère également. Merci de lire [document complet](CODE_OF_CONDUCT.md) pour comprendre les actions qui seront ou ne seront pas tolérées.
