

def play_bowling_game():
    game_over = False
    max_rounds = 10
    loop = 0
    score_dict = {}
    while not game_over:
        loop += 1
        print("Max rounds is {0}".format(max_rounds))
        print("Enter the score for round {0}".format(loop))
        score_dict[loop] = input()
        if (loop == 9 and score_dict[loop] == "X") or (loop == 10 and score_dict[loop] == "/"):
            max_rounds = 11
            print("Max rounds is {0}".format(max_rounds))
        elif (loop == 10 and score_dict[loop] == "X"):
            max_rounds = 12
            print("Max rounds is {0}".format(max_rounds))
        print("Max rounds is {0}".format(max_rounds))
        if loop == max_rounds:
            game_over = True
            print("Game is found to be over")
    return score_dict

def calculate_final_score(round_result):
    results_list = []
    final_score = 0
    for bowling_round, score in round_result.items():
        if score == "X" and bowling_round <= 10:
            results_list.append([round_result[bowling_round], round_result[bowling_round + 1], round_result[bowling_round + 2]])     
        elif score == "/" and bowling_round <= 10:
            results_list.append([round_result[bowling_round], round_result[bowling_round + 1]])
        elif bowling_round <= 10:
            results_list.append([score])
    print(results_list)
    for item in results_list:
        for score in item:
            if score == "X" or score == "/":
                final_score = final_score + 10
            else:
                final_score = final_score + int(score)
        print("Score so far is {0}".format(final_score))
    return final_score
                
            

score = 0
round_result_dict = play_bowling_game()
final_score =  calculate_final_score(round_result_dict)



print("Final score is {0} at the end of the program.".format(final_score))
