import requests
import json

url = "https://api.imeicheck.net/v1/checks"

payload = json.dumps({
  "deviceId": "356735111052198",
  "serviceId": 1
})
headers = {
  'Authorization': 'Bearer sy5woSxuac7xKalljXFjgbB2hCRw7GQLueRtGp1974d8fe72',
  'Accept-Language': 'en',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
{
  "id": 1,
  "title": "Apple Basic Info",
  "price": "0.06",
  "description": "The basic report for Apple devices, which includes: Full Model Description, Warranty Details, Find My status, iCloud Status, Blacklist Status, US Block Status, Purchase Date and SIM-Lock Status",
  "properties": {
    "deviceName": "iPhone 7 128GB Black [A1778] [iPhone9,3]",
    "imei": "356303485329443",
    "imei2": "356303488390046",
    "serial": "ASPNAC5RHYK9",
    "meid": "356303480463429",
    "estPurchaseDate": 1481155200,
    "modelDesc": "IPHONE 7 BLACK 128GB-GBR",
    "replacement": False,
    "demoUnit": False,
    "refurbished": False,
    "purchaseCountry": "United Kingdom",
    "apple/region": "United Kingdom",
    "gsmaBlacklisted": False,
    "simLock": False,
    "fmiOn": True,
    "replaced": False,
    "warrantyStatus": "Out Of Warranty",
    "repairCoverage": False,
    "technicalSupport": False,
    "apple/modelName": "iPhone 7",
    "loaner": False,
    "lostMode": False,
    "usaBlockStatus": "Clean",
    "network": "AT&T/T-Mobile/Global"
  }
}

{
  "id": "UrQ93R5NBaADsQPj",
  "type": "api",
  "status": "successful",
  "orderId": null,
  "service": {
    "id": 1,
    "title": "Apple Basic Info"
  },
  "amount": "0.06",
  "deviceId": "356735111052198",
  "processedAt": 1737642989,
  "properties": {
    "deviceName": "iPhone 12 Pro Max 512GB Gold [A2412] [iPhone13,4]",
    "image": "https://sources.imeicheck.net/images/face55f8067fbf4c42ba0d5a22cfd9a5.png",
    "imei": "356735111052198",
    "imei2": "356735111256724",
    "serial": "G6TDN2RS0D5Q",
    "meid": "35673511105219",
    "estPurchaseDate": 1605225600,
    "modelDesc": "IPHONE 12 PRO MAX GOLD 512GB-ITS",
    "replacement": false,
    "demoUnit": false,
    "refurbished": false,
    "apple/region": "ITS",
    "simLock": false,
    "fmiOn": true,
    "replaced": false,
    "warrantyStatus": "Out Of Warranty",
    "repairCoverage": false,
    "technicalSupport": false,
    "apple/modelName": "iPhone 12 Pro Max",
    "loaner": false,
    "lostMode": false,
    "usaBlockStatus": "Clean",
    "network": "China"
  }
}

{
  "id": "Tn8Qu8ySminsLd9-",
  "type": "api",
  "status": "unsuccessful",
  "orderId": null,
  "service": {
    "id": 1,
    "title": "Apple Basic Info"
  },
  "amount": "0.00",
  "deviceId": "123124124124",
  "processedAt": 1737643205,
  "properties": []
}


set_1 = {
    "deviceName"
"imei"
"imei2"
"serial"
"meid"
"estPurchaseDate"
"modelDesc"
"replacement"
"demoUnit"
"refurbished"
"purchaseCountry"
"apple/region"
"gsmaBlacklisted"
"simLock"
"fmiOn"
"replaced"
"warrantyStatus"
"repairCoverage"
"technicalSupport"
apple/m
"loaner"
"lostMode"
"usaBlockStatus"
"network"
}
