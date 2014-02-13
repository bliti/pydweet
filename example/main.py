#!/usr/bin/env python
from dweet import Dweet


if __name__ == "__main__":

    dweet = Dweet()
    
    #dweet an dweet without a thing name. Returns a a thing name in the response
    print dweet.dweet({"hello": "world"})
    
    #dweet with a thing name
    print dweet.dweet_by_name(name="test_thing", data={"hello": "world"})
    
    #get the latest dweet by thing name. Only returns one dweet.
    print dweet.latest_dweet(name="test_thing")
    
    #get all the dweets by dweet name.
    print dweet.all_dweets(name="test_thing")