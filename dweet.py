import requests


class Dweet(object):
    
    #dweet root domain and endpoints
    BASE_URL = "http://dweet.io/"

    #creates a name for the thing dweeting.
    #for anonymous or first time use.
    #assigns a random dweet name to the thing.
    DWEET = "{0}{1}".format(BASE_URL , "dweet?")

    #dweet by thing name.
    DWEET_BY_NAME = "{0}{1}".format(BASE_URL, "dweet/for/{name}?")

    #get latest dweets by name.
    LATEST_DWEET = "{0}{1}".format(BASE_URL, "get/latest/dweet/for/{name}")

    #get all dweets by name.
    ALL_DWEETS = "{0}{1}".format(BASE_URL, "get/dweets/for/{name}")
    

    def dweet(self, data):
        """
        Make a dweet without a thing name.
        Assigns a random thing name which is returned
        in the response body.
        Returns a dict type.
        
        Parameter name is a string type.
        Parameter data is a dict type.
        Usage:
        
        data = {"foo": "bar"}
        
        is turned into:
        /dweet?foo=bar 
        """
        return requests.get(self.DWEET, params=data).json()


    def dweet_by_name(self, name, data):
        """
        Make a dweet with a named thing.
        Returns a dict type.
        
        Parameter name is a string type.
        Parameter data is a dict type.
        
        Usage:
        
        data = {"foo": "bar"}
        
        is turned into:
        /{name}?foo=bar
        
        """
        return requests.get(self.DWEET_BY_NAME.format(name=name),
                        params=data).json()


    def latest_dweet(self, name):
        """
        Get the latest dweet by thing name.
        Only returns one dweet as response.
        Returns dict type.
        Parameter name is a string type.
        """
        return requests.get(self.LATEST_DWEET.format(name=name)).json()
    
    
    def all_dweets(self, name):
       """
       Get dweets in last 24 hours by thing name.
       Dweet limit currently is 500 dweets.
       Returns dict type.
       Parameter name is a string type.
       """ 
       return requests.get(self.ALL_DWEETS.format(name=name)).json()