def nba_cup(results_, find):
    print(results_, find)
    
    
    
    
    
    # your code
    if not find: return ''

    MATCH = False
    results = results_.split(',')
#     print(results)
    W= D= L= S= C= P = 0

    for game in results:       
        game_ls = game.split(' ')
#         print(game, len(game))

        for idx, chr in enumerate(game_ls):
            if not chr.isalpha():
#                 print(idx, chr)
                break 

        T1 = ' '.join([x for x in game_ls[: idx]])
        S1 = game_ls[idx]
        T2 = ' '.join([x for x in game_ls[idx + 1 : len(game_ls) - 1]])
        S2 = game_ls[len(game_ls) - 1]
        
        # print()  
        # print(T1, T2)
        # print()

        # grab all relevant games 
        if T1 == find or T2 == find:

            # find is T1 or 2 Set True
            MATCH = True
            # see if teams match
            print('MATCH')

            # make sure no floats  _> s1 == float
            if S1 == float and S2 == float:
                pass
            else:
                return f"Error(float number):{T1} {S1} {T2} {S2}"

            # change S 1&2 to int
            S1 = int(S1)
            S2 = int(S2)
                    
            # make it so find is always T1 -> boston always comes first anyway
            if T2 == find:        
                place_holder = T1 
                place_holder_scores = S1
                T1 = T2
                S1 = S2
                T2 = place_holder
                S2 = place_holder_scores

#             print('\n')
#             print('\n', T1)
#             print('\n', S1)
#             print('\n', T2)
#             print('\n', S2)
#             print('\n')
            
            # Wins, Losses and Draws 
            # Points
            if S1 > S2:
                W += 1
                P += 3
            elif S1 < S2:
                L += 1
            else:
                D += 1
                P += 1

            # Score, Concessions
            S += S1
            C += S2

    if MATCH:        
        return f'{find}:W={W};D={D};L={L};Scored={S};Conceded={C};Points={P}'
    return f"{find}:This team didn't play!"


a = nba_cup('Los Angeles Clippers 104 Dallas Mavericks 88,New York Knicks 101.12 Atlanta Hawks 112,Indiana Pacers 103 Memphis Grizzlies 112,Los Angeles Clippers 100 Boston Celtics 120', 'Atlanta Hawks')
print(a)