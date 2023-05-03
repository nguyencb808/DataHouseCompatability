import json

#open data.json
with open("data.json",'r') as f:
    data = json.load(f)

applicants = []
team = []
scoredApplicants = []

#imports applicant data to array
for obj in data["applicants"]:
    applicants.append({
    "name": obj["name"],
    "subjective": obj["subjective"],
    "objective": obj["objective"]
    })

#imports team data to array
for obj in data["team"]:
    team.append({
    "name": obj["name"],
    "subjective": obj["subjective"]
    })

#skeleton for an average team member's subjective attributes
total_subjective = {
        "integrity": 0,
        "respectfulness": 0,
        "humility": 0,
        "compassion": 0,
        "teamwork": 0
    }

#adds up the totals for each individual atribute across all team members
for member in team:
        for key, value in member['subjective'].items():
            total_subjective[key] += value

#finds the name of the lowest subjective atribute in the team
lowest_name = min(total_subjective, key=total_subjective.get)

# Ways the totalScore is applied:
# officeAB: .30 of the score - has value 1 if applicant can attend office in person
# interest: .15 of the score - values from 1-5, weighted
# gradPlan: .05 of the score - has value 1 if applicant is planning on graduating and staying on island 
# PI_Score: .2 of the score -  has values from 100-450, weighted accordingly 
# app_sub:  .15 of the score - subtotal of the subjective values of the applicant, the well-roundedness of applicant's attributes
# Lowest_value covering: .15 of total score - using the lowest_name, sees how good applicant is good at filling in weakest value in team attributes

for member in applicants:
    #reset variables
    totalScore = 0
    app_sub = 0

    #shows well-roundedness of applicant calculating app_sub by finding subtotal of all atributes
    for key, value in member['subjective'].items():
        app_sub += value
    totalScore += (app_sub/50)*.15

    #adds .3 to total score if applicant can attend office in person
    if member['objective']['officeAB'] == 1:
         totalScore += .3

    #adds .05 to total score if applicant is graduating and staying here (potentially looking for work here at datahouse)
    if member['objective']['gradPlan'] == 1:
         totalScore += .05

    #adds a score weighted by .15 by looking at the level of interest
    totalScore += (member['objective']['interest']/5)*.15
    
    #adds a score weighted by .2 by looking at PI test's results
    totalScore += (member['objective']['PI_Score']/450)*.2

    #adds a score weighted by .15 by looking to see how well applicant covers weakest team attribute  
    totalScore += (member['subjective'][lowest_name]/10)*.15

    #appends the name and totalScore of the applicant to the scoredApplicants array
    scoredApplicants.append({
    'name':member["name"], 'score': totalScore
    })
    
    

#opens results file and after converting to json array, writes the array into the file
jsonDump = json.dumps(scoredApplicants)
writingTo = open("results.json", "w")
writingTo.write(jsonDump)
writingTo.close()
