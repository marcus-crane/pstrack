import json
import requests
from bs4 import BeautifulSoup

def importConfig():
  with open('config.json') as config:
    return json.load(config)

def fetchApp(storeID):
  r = requests.get(f"https://play.google.com/store/apps/details?id={storeID}")
  return r.text

def checkCurrentVersion():
  apps = importConfig()
  updateCount = 0

  for app in apps:
    appID = apps[app]['storeID']
    appVersion = apps[app]['currentVersion']

    data = fetchApp(appID)
    soup = BeautifulSoup(data, "html.parser")
    latestVersion = soup.find(itemprop="softwareVersion").get_text().strip()

    if latestVersion == appVersion:
      continue
    else:
      updateAlert(app, latestVersion)
      updateCount = updateCount + 1
      apps[app]['currentVersion'] = latestVersion

  if (updateCount > 0):
    writeUpdates(apps)
  else:
    print("Sorry pal, nothing yet. Check back tomorrow?")
    

def updateAlert(name, version):
  print(f'{name} has just been updated to v{version}!')

def writeUpdates(apps):
  with open('config.json', 'w') as config:
    config.write(json.dumps(apps, sort_keys=True, indent=2, separators=(',', ': ')))

  print('Changes saved. See ya next time!')

checkCurrentVersion()