# Given a list of N coins, their values (V1, V2, … , VN), and the total sum S. Find the minimum
# number of coins the sum of which is S (we can use as many coins of one type as we want), or
# report that it’s not possible to select coins in such a way that they sum up to S.

def num_of_coins(v_list, S):
    num_of_coins = [0] + (S) * [float("+inf")]
    for i in range(1, S+1):
        for v in sorted(v_list):
            if v <= i and (num_of_coins[i-v]+1 < num_of_coins[i]):
                num_of_coins[i] = num_of_coins[i-v]+1
    result = num_of_coins[S]
    if result != float("+inf"):
        return result
    except IndexError:
        return "It's not possible to select coins in such a way that they sum up to S."

print(num_of_coins([1,3,5], 11))


    
