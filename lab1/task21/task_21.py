import time

replacements = {"6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

def parse_cards(card_list):
    parsed_cards = []
    for card in card_list:
        parsed_cards.append((card[0], card[1]))
    return parsed_cards

def change_rank(lst):
    new_N_card = []
    for value, suit in lst:
        new_value = replacements.get(value)
        new_N_card.append((new_value, suit))
    return new_N_card


def simple_durak(N_card, M_card, trump):
    for i in M_card:
        can_defend = False
        for j in N_card:
            if i[1] == j[1]:
                if j[0] > i[0]:
                    can_defend = True
                    N_card.remove(j)
                    break
            elif i[1] != j[1]:
                if j[1] == trump:
                    if i[1] != trump or j[0] > i[0]:
                        can_defend = True
                        N_card.remove(j)
                        break
        if can_defend == False:
            return "NO"
    return "YES"

def main():
    start_time = time.time()
    with open("input.txt", "r") as file:
        lines = file.readlines()
        N, M, trump = lines[0].strip().split()
        N = int(N)
        M = int(M)
        N_card = parse_cards(lines[1].strip().split())
        M_card = parse_cards(lines[2].strip().split())

    N_card = change_rank(N_card)
    M_card = change_rank(M_card)

    result = simple_durak(N_card, M_card, trump)

    with open("output.txt", "w") as file:
        file.write(result)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения: {execution_time:.6f} секунд")


if __name__ == "__main__":
    main()