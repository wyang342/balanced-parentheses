

def balance_parens(str):
    opening_parens_index_list = []  # keeps track of the indexes of "("
    balanced_str_initial = ""

    for i, char in enumerate(str):
        if (char == "("):  # if char is "(", keep track of it by adding its index to list
            opening_parens_index_list.append(len(balanced_str_initial))
        elif (char == ")"):
            # if no opening parens tracked in list, ignore the closing parens
            if (len(opening_parens_index_list) == 0):
                continue
            else:  # else remove the index of the latest tracked "(" from list
                opening_parens_index_list.pop()
        # adds all letters, "("'s, and matched ")"'s.
        balanced_str_initial += char

    balanced_str_final = ""
    if (len(opening_parens_index_list) > 0):  # if there are unmatched "("'s
        for i, char in enumerate(balanced_str_initial):
            # add char to balanced_str_final only if it's untracked in opening_parens_index_list (which means the char is "balanced")
            if i not in opening_parens_index_list:
                balanced_str_final += char
    else:  # if all chars are "balanced", add then balanced_str_initial is balanced_str_final
        balanced_str_final = balanced_str_initial

    return balanced_str_final


print(balance_parens(")c(b)c)("))
