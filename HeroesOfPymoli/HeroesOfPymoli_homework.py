#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[46]:


# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_df = pd.read_csv(file_to_load)
purchase_df.head()


# ## Player Count

# * Display the total number of players
# 

# In[47]:


#Calculating total number of players using the len function
total_players=len(purchase_df["SN"].value_counts())
total_players


# In[48]:


#creating new dataframe with total_players
total_players_df=pd.DataFrame({"Total Players": [total_players]})
total_players_df


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[49]:


#calculating unique items in item ID using len function
unique_items=len(purchase_df["Item ID"].unique())
unique_items


# In[50]:


#calculating average price using mean fucntion
average_price=purchase_df["Price"].mean()
average_price
#formatting the output as to have $ sign and two decimal points
price_format= "${0:.2f}"
average_price_format=price_format.format(average_price)
average_price_format


# In[51]:


#calculating number of purchases using purchase ID with count function
purchase_number=purchase_df["Purchase ID"].count()
purchase_number


# In[52]:


#calculating total revenue using sum
total_revenue=purchase_df["Price"].sum()
total_revenue
#formatting the output as to have $ sign and two decimal points
revenue_format= "${0:.2f}"
total_revenue_format=revenue_format.format(total_revenue)
total_revenue_format


# In[53]:


#creating new dataframe for the purchase analysis
purchase_analysis_df=pd.DataFrame({"Number of Unique Items":[unique_items],
                                  "Average Price":  [average_price_format],
                                  "Number of Purchases":[purchase_number],
                                  "Total Revenue":  [total_revenue_format]})
purchase_analysis_df


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[54]:


#calculating male, female, other/ non-disclosed counts using groupby function
gender_df = purchase_df.groupby(['Gender'])
gender_df


gender_counts=gender_df.nunique()["SN"]
gender_counts_df=pd.DataFrame(gender_counts)
gender_counts_df


# In[55]:


#calculating male, female, other/ non-disclosed percentage using groupby function
player_percent=(gender_counts/total_players) * 100
player_percent

player_percent_df=pd.DataFrame(player_percent)
player_percent_df


# In[56]:


#merging counts and percentage dataframe based on gender
merge_df = pd.merge(gender_counts_df, player_percent_df, on="Gender")
merge_df


# In[57]:


#renaming the columns
gender_demo_df = merge_df.rename(columns={"SN_x":"Total Count", "SN_y":"Percentage of Players"})
#formatting the percentage
gender_demo_df["Percentage of Players"] = gender_demo_df["Percentage of Players"].astype(float).map("{:,.2f}%".format)
gender_demo_df


# In[ ]:





# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[58]:


#calculating purchase count using groupby function
gender_df = purchase_df.groupby(['Gender'])

purchase_count=gender_df["Purchase ID"].count()
purchase_count


# In[59]:


#calculating average purchase price
average_purchase=gender_df["Price"].mean()
average_purchase


# In[60]:


#calculating total purchase value
total_purchase=purchase_count * average_purchase
total_purchase


# In[61]:


#calculating average purchase total per person
person_purchase=total_purchase/gender_counts
person_purchase


# In[62]:


#creating a new dataframe with the calculated values
gender_analysis_df=pd.DataFrame({"Purchase Count": purchase_count,
                                "Average Purchase Price": average_purchase,
                                "Total Purchase Value": total_purchase,
                                "Avg Total Purchase per Person": person_purchase})
gender_analysis_df


# In[63]:


#data cleaner formatting and final analysis output
gender_analysis_df["Average Purchase Price"] = gender_analysis_df["Average Purchase Price"].astype(float).map("$ {:,.2f}".format)
gender_analysis_df["Total Purchase Value"] = gender_analysis_df["Total Purchase Value"].astype(float).map("$ {:,.2f}".format)
gender_analysis_df["Avg Total Purchase per Person"] = gender_analysis_df["Avg Total Purchase per Person"].astype(float).map("$ {:,.2f}".format)
gender_analysis_df


# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[64]:


purchase_df.head()


# In[65]:


# Create the bins in which Data will be held  
bins = [0,9,14,19,24,29,34,39,100]

# Create the names for the bins
group_names = ["<10", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40+"]

#Categorizing the existing players using the age bins using pd.cut()
purchase_df["Age Group"] = pd.cut(purchase_df["Age"], bins, labels=group_names, include_lowest=True)
purchase_df.head()


# In[66]:


#grouopby age group for further analysis
age_group=purchase_df.groupby(["Age Group"])

age_group_df = purchase_df.set_index("Age Group")
age_group_df.head()


# In[67]:


#calculating number based on age groups
age_count=age_group["SN"].nunique()
age_count


# In[68]:


#calculating percentage based on age groups
age_percent=(age_count/total_players)*100
age_percent


# In[69]:


#Creating a summary data frame to hold the results and data cleaner formatting
age_demo_df=pd.DataFrame({"Total Count": age_count,
                         "Percentage of Players": age_percent})
age_demo_df
age_demo_df["Percentage of Players"] = age_demo_df["Percentage of Players"].astype(float).map("{:,.2f}%".format)
age_demo_df


# In[ ]:





# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[70]:


#calculating purchase count based on age group
purchaseage_count=age_group["Purchase ID"].count()
purchaseage_count


# In[71]:


#calculating average purchase price based on age group
averageage_purchase=age_group["Price"].mean()
averageage_purchase


# In[72]:


#calculating total purchase price based on age group
totalage_purchase=age_group["Price"].sum()
totalage_purchase


# In[73]:


#calculating avg. purchase total per person based on age group
avgage_purchase=totalage_purchase/age_count
avgage_purchase


# In[74]:


#Creating a summary data frame to hold the results and data cleaner formatting
age_analysis_df=pd.DataFrame({"Purchase Count": purchaseage_count,
                                "Average Purchase Price": averageage_purchase,
                                "Total Purchase Value": totalage_purchase,
                                "Avg Total Purchase per Person":avgage_purchase })
age_analysis_df
age_analysis_df["Average Purchase Price"] = age_analysis_df["Average Purchase Price"].astype(float).map("$ {:,.2f}".format)
age_analysis_df["Total Purchase Value"] = age_analysis_df["Total Purchase Value"].astype(float).map("$ {:,.2f}".format)
age_analysis_df["Avg Total Purchase per Person"] = age_analysis_df["Avg Total Purchase per Person"].astype(float).map("$ {:,.2f}".format)
age_analysis_df


# In[ ]:





# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[75]:


#Groupby main dataframe by SN
sn_df = purchase_df.groupby('SN')

sn_df.head()


# In[76]:


#calculating purchase count based on SN
snpurchase_counts=sn_df["Purchase ID"].count()
snpurchase_counts


# In[77]:


#calculating average purchase price based on SN
avg_purchase_price=sn_df["Price"].mean()
avg_purchase_price


# In[78]:


#calculating total purchase price based on SN
total_purchase_value=sn_df["Price"].sum()
total_purchase_value


# In[79]:


#Creating a summary data frame to hold the results 
sn_summary_df=pd.DataFrame({"Purchase Count": snpurchase_counts,
                           "Average Purchase Price": avg_purchase_price,
                           "Total Purchase Value": total_purchase_value})
#Sorting the total purchase value column in descending order
sn_summary_df=sn_summary_df.sort_values(by= ["Total Purchase Value"], ascending=False)

#data cleaner formatting
sn_summary_df["Average Purchase Price"] =sn_summary_df["Average Purchase Price"].astype(float).map("$ {:,.2f}".format)
sn_summary_df["Total Purchase Value"] = sn_summary_df["Total Purchase Value"].astype(float).map("$ {:,.2f}".format)
sn_summary_df.head()


# In[ ]:





# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, average item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[80]:


#Retrieving the Item ID, Item Name, and Item Price columns
popular_items=purchase_df[["Item ID", "Item Name", "Price"]]
popular_items.head()


# In[81]:


#Groupby Item ID and Item Name
popular_groups=popular_items.groupby(["Item ID", "Item Name"])
popular_groups.head()


# In[82]:


#calculating purchase count
item_count=popular_groups["Item ID"].count()
item_count


# In[83]:


#calculating purchase value
item_purchase_value=(popular_groups["Price"].sum())
item_purchase_value


# In[84]:


#calculating average item price
item_price=popular_groups["Price"].mean()
item_price


# In[85]:


#Creating a summary data frame to hold the results
item_summary_df=pd.DataFrame({"Purchase Count": item_count,
                           "Item Price": item_price,
                           "Total Purchase Value": item_purchase_value})
#Sorting the purchase count column in descending order
item_summary_df=item_summary_df.sort_values(by= ["Purchase Count"], ascending=False)
item_summary_df.head()


# In[86]:


#Sorting the total purchase value in descending order
profit_summary_df=item_summary_df.sort_values(by= ["Total Purchase Value"], ascending=False)
profit_summary_df.head()


# In[87]:


#data cleaner formatting and final analysis output
item_summary_df["Item Price"] =item_summary_df["Item Price"].astype(float).map("$ {:,.2f}".format)
item_summary_df["Total Purchase Value"] = item_summary_df["Total Purchase Value"].astype(float).map("$ {:,.2f}".format)
item_summary_df.head()


# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[88]:


#data cleaner formatting and final analysis output for most profitable items
profit_summary_df["Item Price"] =profit_summary_df["Item Price"].astype(float).map("$ {:,.2f}".format)
profit_summary_df["Total Purchase Value"] = profit_summary_df["Total Purchase Value"].astype(float).map("$ {:,.2f}".format)
profit_summary_df.head()


# In[ ]:




