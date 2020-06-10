import random

#Creating functions
#Calculates percentage of right answers
def calculate_Percentage(score, questions_Asked):
        percentage = 0
        percentage = (score/questions_Asked) * 100
        return percentage

#Reads the input file and appends data to lists
def read_File():
        for line in infile:
                #Reads for description of what the quiz is
                if line.startswith("Description:"):
                        print("\n" + line)
                if line.startswith("What") or line.startswith("When") or line.startswith("Where") or line.startswith("How"):
                        data = line.split(", ")
                        quiz_Questions.append(data[0].strip())
                        quiz_Answers.append(data[1].lower().strip())
                        
#Asking for file name, creating lists for quiz, and using the read_File function
print("Type the name of the quiz file below? Ex.V:\Python\Final Project\FinalProjectTestFile.txt\n(Sometimes need to put quotation marks between the file\'s name.)")
fname = input("")
infile = open(fname)
quiz_Questions = []
quiz_Answers = []
read_File()

#Creating quiz index and shuffling it                
question_Order = list(range(0, len(quiz_Questions)))
random.shuffle(question_Order)

#Creating user score and questions asked. Asking for amount of questions user wishes to have.
total_Questions = input("How many questions would you like? ")
score = 0
questions_Asked = 0

for i in range(int(total_Questions)):

        #Printing questions and asking for input
        question_Index = question_Order[i]
        print(quiz_Questions[question_Index])
        questions_Asked += 1
        user_Answer = input("Answer: ").lower()
    
        #Deciding whether question is right or wrong and responding accordingly  
        if user_Answer == quiz_Answers[question_Index]:
                print("Correct")
                score += 1      
        else:
                print("Incorrect!, the answer is " + quiz_Answers[question_Index])
                
        #Failsafe in case user asks more questions than on file.
        if i == len(quiz_Questions) - 1:
                print("Sorry, the file does not contain any more quesitons.")
                break

#Calculating percentage and printing score results
percentage = calculate_Percentage(score, questions_Asked)  
print("You got " + str(score) + " answers out of " + str(questions_Asked) + ", which is " + str(percentage) + "%")
