while(wrong != True):
     
    ques_no += 1
    ran = random.randint(0, len(questions)-1)
    print("\n\nQ.", ques_no, ":-", end="")
    print(questions[ran])
 
    for num, option in enumerate(options):
        print(str(num+1)+"."+option[ran])
 
    print("Would you like to take lifeline, if yes, press 9\n\
    Choose any option:  or you can quit by pressing 0 \t\t")
    give_answer = int(input())
 
    if give_answer == 9:
       
      # condition variable is to count lifelines
      # used
      if condition <= 4:
 
            condition += 1
            great = lifeline(ran, opts, op)
 
            if great == 0:
               
                if total_amt < 10000:
                    total_amt = 0
                elif total_amt < 320000:
                    total_amt = 10000
                elif total_amt < 70000000:
                    total_amt = 320000
                break
 
            elif great == -1:
                ques_no -= 1
                pass
 
            elif great == None:
                print("Choose any option or press 0 to quit\t")
                give_ansr = int(input())
 
                if answer[ran] == give_ansr:
                    print("Correct answer, great")
                    correct += 1
 
            elif great == -2:
                break
 
            else:
                correct += 1
                print("You have won Rs=", end="")
                total_amt = amount(correct)
 
        else:
          print("You have used your all lifelines\t\n Choose any option: \
                or you can quit by pressing 0\t\t")
 
            give_ans = int(input())
            key = answer[ran]
 
            if give_ans == 0:
                total_amt = amount(correct)
                break
 
            elif key == give_ans:
                print("Correct, You have won Rs. =", end="")
                correct += 1
                total_amt = amount(correct)
 
            else:
                print("Wrong Answer....")
                print("Correct Answer is : ", options[answer[ran]-1][ran])
 
                if total_amt < 10000:
                    total_amt = 0
                elif total_amt < 320000:
                    total_amt = 10000
                elif total_amt < 70000000:
                    total_amt = 32000
 
                wrong = True
    else:
        key = answer[ran]
 
        if give_answer == 0:
            if correct != 0:
                total_amt = amount(correct)
            break
 
        elif key == give_answer:
            print("Correct answer.., You have won Rs.=", end="")
            correct += 1
            total_amt = amount(correct)
 
        else:
            print("Wrong Answer...Better luck next time...")
            print("Correct Answer is :", options[answer[ran]-1][ran])
 
            if total_amt < 10000:
                total_amt = 0
            elif total_amt < 320000:
                total_amt = 10000
            elif total_amt < 70000000:
                total_amt = 320000
            wrong = True
 
    # total questions are 16
    if correct == 16:
        break
 
    # delete previous question and its options from list
    del questions[ran]
    del option1[ran]
    del option2[ran]
    del option3[ran]
    del option4[ran]
    del answer[ran]
    del opts[0][ran]
    del opts[1][ran]
    del opts[2][ran]
    del opts[3][ran]
    del op[0][ran]
    del op[1][ran]
    del op[2][ran]
    del op[3][ran]
    options = [option1, option2, option3, option4]
 
print("Your winning amount is Rs. ", total_amt)