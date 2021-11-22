from django.shortcuts import render
from graph.models import Stock
import pandas as pd 
import numpy as np 
import json

json_data= open("data.json")
json2dic = json.load(json_data)


def trial(request):
    sectors=["all"] 
    weeks=["all"]
    codes=["all"]



    sectors_all=[]
    start_dates_all=[]
    end_dates_all=[]
    codes_all=[]
    weeks_all=[]

    
    Week1_ROI_list=[]
    Week2_ROI_list=[]
    Week4_ROI_list=[]
    Week8_ROI_list=[]
    Week12_ROI_list=[]
    Week24_ROI_list=[]

    Week1_ROI_percent_list=[]
    Week2_ROI_percent_list=[]
    Week4_ROI_percent_list=[]
    Week8_ROI_percent_list=[]
    Week12_ROI_percent_list=[]
    Week24_ROI_percent_list=[]

    Week1PandL_list=[]
    Week2PandL_list=[]
    Week4PandL_list=[]
    Week8PandL_list=[]
    Week12PandL_list=[]
    Week24PandL_list=[]

    

    length= len(codes_all)
    range_array= range(0,length)

    for stock in json2dic:
        start_dates_all.append(stock["Date_StartDate"])
        end_dates_all.append(stock["End_date"])
        sectors_all.append(stock["scoring_category"]) 
        codes_all.append(stock["Code"])         
        
        #create unique sectors list
        if stock["scoring_category"] not in sectors:
            sectors.append(stock["scoring_category"])

        #create unique weeks list
        if stock["start_date"]+" to " + stock["End_date"] not in weeks:
            weeks.append(stock["start_date"]+" to " + stock["End_date"])
        #create unique sectors list
        if stock["Code"] not in codes:
            codes.append(stock["Code"])    


    #create week1 roi and roi% list
        if "Week1_ROI" in stock["ROI"]:
            Week1_ROI_list.append(stock["ROI"]["Week1_ROI"])  
            Week1PandL_list.append(stock["ROI"]["Week1PandL"])
        else:
            Week1_ROI_list.append(0)  
        
        if "Week1PecentGain" in stock["ROI"]:
            Week1_ROI_percent_list.append(stock["ROI"]["Week1PecentGain"])  
        else:
            Week1_ROI_percent_list.append(0)  

    #create week2 roi list
        if "Week2_ROI" in stock["ROI"]:
            Week2_ROI_list.append(stock["ROI"]["Week2_ROI"])
            Week2PandL_list.append(stock["ROI"]["Week2PandL"])
        else:
            Week2_ROI_list.append(0)  

        if "Week2PecentGain" in stock["ROI"]:
            Week2_ROI_percent_list.append(stock["ROI"]["Week2PecentGain"])  
        else:
            Week2_ROI_percent_list.append(0)  

    #create week4 roi list
        if "Week4_ROI" in stock["ROI"]:
            Week4_ROI_list.append(stock["ROI"]["Week4_ROI"])
            Week4PandL_list.append(stock["ROI"]["Week4PandL"])
        else:
            Week4_ROI_list.append(0)  
        
        if "Week4PecentGain" in stock["ROI"]:
            Week4_ROI_percent_list.append(stock["ROI"]["Week4PecentGain"])  
            
        else:
            Week4_ROI_percent_list.append(0)  

    #create week8 roi list        

        if "Week8_ROI" in stock["ROI"]:
            Week8_ROI_list.append(stock["ROI"]["Week8_ROI"])
            Week8PandL_list.append(stock["ROI"]["Week8PandL"])
        else:
            Week8_ROI_list.append(0)  
        
        if "Week8PecentGain" in stock["ROI"]:
            Week8_ROI_percent_list.append(stock["ROI"]["Week8PecentGain"])  
        else:
            Week8_ROI_percent_list.append(0)  

    #create week12 roi list

        if "Week12_ROI" in stock["ROI"]:
            Week12_ROI_list.append(stock["ROI"]["Week12_ROI"])
            Week12PandL_list.append(stock["ROI"]["Week8PandL"])
        else:
            Week12_ROI_list.append(0)  

        if "Week12PecentGain" in stock["ROI"]:
            Week12_ROI_percent_list.append(stock["ROI"]["Week12PecentGain"])  
        else:
            Week12_ROI_percent_list.append(0)  

    #create week24 roi list
        if "Week24_ROI" in stock["ROI"]:
            Week24_ROI_list.append(stock["ROI"]["Week24_ROI"])
            Week24PandL_list.append(stock["ROI"]["Week8PandL"])
        else:
            Week24_ROI_list.append(0)  
        
        if "Week24PecentGain" in stock["ROI"]:
            Week24_ROI_percent_list.append(stock["ROI"]["Week24PecentGain"])  
        else:
            Week24_ROI_percent_list.append(0)  

    #create weeks alll list
    for i in range(0,len(start_dates_all)):
        weeks_all.append(start_dates_all[i]+" to "+ end_dates_all[i])

   

 
    
    
    return render(request, "graph/trial.html",{"sectors":sectors,"weeks":weeks,"codes":codes,"sectors_all":sectors_all,"length":length,"range_array": range_array,"start_dates_all":start_dates_all,"end_dates_all":end_dates_all,"codes_all":codes_all,"weeks_all":weeks_all,"Week1_ROI_list":Week1_ROI_list,"Week2_ROI_list":Week2_ROI_list,"Week4_ROI_list":Week4_ROI_list,"Week8_ROI_list":Week8_ROI_list,"Week12_ROI_list":Week12_ROI_list,"Week24_ROI_list":Week24_ROI_list, "Week1_ROI_percent_list":Week1_ROI_percent_list,"Week2_ROI_percent_list":Week2_ROI_percent_list, "Week4_ROI_percent_list" :Week4_ROI_percent_list,   "Week8_ROI_percent_list":  Week8_ROI_percent_list,"Week12_ROI_percent_list":  Week12_ROI_percent_list, "Week24_ROI_percent_list": Week24_ROI_percent_list, "Week1PandL_list":Week1PandL_list,"Week2PandL_list":Week2PandL_list,"Week4PandL_list":Week4PandL_list,"Week8PandL_list":Week8PandL_list,"Week12PandL_list":Week12PandL_list,"Week24PandL_list":Week24PandL_list})


