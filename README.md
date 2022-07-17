# tortoise_assignment

1. endpoint : base_url + /getcreateplan/
Provide all the available plans to the user on a Get request, and create a plan in db on post request.

Sample payload to create plan
{
  "planName" : "Testing Plan", -> string 
  "amountOptions" : "UPI", -> string
  "tenureOptions" : 100, ->  represents tenure in days should be integer
  "benefitPercentage" : 10.5, -> float,
  "benefitType" : "cashback" ->string
}


2. endpoint : base_url + /getcreatepromotion/
Provide all the available promotions to the user on a Get request, and create a promotion in db on post request.
Promotion are two types on the basis of number of user and duration, You need to paas promotionType(user/duration) and promotion data accordingly.
if promotionType is user then promotiondata will be number
if promotionType is duration then promotiondata will be a string in formate(22th May 2022 to 24th May 2022) representing start and end date.

Sample Payload to create Promotions
{
 "promotionType" :"user", -> str (user/duration)
 "promotionData": "400", -> str
 "planId" :1 -> int for which plan promotion is applied.
 }

 
 3. endpoint : bas_url + /getenrollusers/
 Provide all the enrolled plans on Get request, and enroll a user in plan on post request.
 
 Sample Payload to enroll in plan
 {
 "userId" : 4, -> int
 "planId" : 1, ->int 
 "selectedAmount":100000, ->int
 "selectedTenure":365, ->int
 "depositedAmount":10  ->int
 }
 
 
 
