import requests

# total virus implementation:
class VirusAPI:
    indicators = [
        "d0e196a0c25d35dd0a84593cbae0f38333aa58529936444ea26453eab28dfc86"
    ]

    __API_KEY = "c4759908a9936bf945e73018b64b11c8c39bcad147221276a1e1b0ed8b83e2d1"
    __VT_URL = "https://www.virustotal.com/api/v3/urls/"

    def scanURL(self, resource):
        headers = {
            "Accept": "application/json",
            "x-apikey": self.__API_KEY
        }

        url = self.buildURLWithResource(resource)
        response = requests.request("GET", url, headers=headers)
        print(response.text)

    def buildURLWithResource(self, resource):
        return self.__VT_URL + resource
