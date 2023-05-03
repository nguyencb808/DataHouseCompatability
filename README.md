This program predicts the compatability of applicants applying to Datahouse by looking at both objective and subjective values, and how these subjective values fit in with the team. 

The scores are calculated and weighted based on the following variables: 
officeAB: .30 of the score - has value 1 if applicant can attend office in person
interest: .15 of the score - values from 1-5, weighted
gradPlan: .05 of the score - has value 1 if applicant is planning on graduating and staying on island 
PI_Score: .2 of the score -  has values from 100-450, weighted accordingly 
app_sub:  .15 of the score - subtotal of the subjective values of the applicant, the well-roundedness of applicant's attributes
Lowest_value covering: .15 of total score - using the lowest_name, sees how good applicant is good at filling in weakest value in team attributes

This program takes in the JSON file titled data.json and requires applicants and team members to have specific parameters. In this file is an example given to show proper syntax for the JSON file. 

The program outputs its array into results.json. 