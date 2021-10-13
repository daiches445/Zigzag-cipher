def zigzag_enc(text, key):
    first_jump = (key - 1) * 2  # the first distance between letters
    second_jump = 0  # the second distance between letters
    length = len(text)
    segment = 0  # represents the "row"
    index = segment  # represents the letter index in the original text
    output = ""
    if key > length:   # if the key larger then the length of the text it cant be encoded
        return text

    while segment < key:  # when 'segment' will be larger then the key it means that we went through all the 'rows'
        index = segment  # the first index will always be same as the index off the current 'row' 
        output += text[index]  # adding the first letter in the 'row'

        if 0 < segment < key - 1:  # referring to the rows between the first and the last rows. different functionality.
            index += first_jump  # setting the next index by adding the distance between the letters.
            while index < length:  # as long as the index is in bounds of the text length.
                output += text[index]  # adding the the char in the current index in the text.
                index += second_jump  # adding the secondary distance between the letters.
                if index < length:  # check for exception
                    output += text[index]  # if in range adding the letter.
                index += first_jump
        else:  # refers to first and last lines only..one distance jump between characters.(no 'second jump')
            index += (key - 1) * 2
            while index < length:
                output += text[index]
                index += (key - 1) * 2  # adding the 'key' to index after char adding.

        segment += 1  # after finishing in the current segment(row),we will continue to the next segment by adding 1
        first_jump -= 2  # additionally we must reduce the first distance between the characters.
        second_jump += 2  # and also,increase the second distance between the letters.

    return output


def zigzag_dec(text, key):
    first_jump = (key - 1) * 2
    second_jump = 0
    length = len(text)
    t_i = 0  # the index of letter we want to assign in the coded text.
    segment = 0
    index = segment  # the location of letter in the encoded text.
    arr = [None] * length  # this will be the encoded text, at the end will be joined into 'output'.
    output = ""
    if key > length:   # if the key larger then the length of the text it cant be encoded
        return text

    while segment < key:
        index = segment
        arr[index] = text[t_i]  # adding the letter from the codded text into a specific location in the arr.
        t_i += 1  # moving to the next char in the coded text.
        if 0 < segment < key - 1:
            index += first_jump
            while index < length:
                arr[index] = text[t_i]  # adding the letter from the codded text into a specific location in the arr.
                t_i += 1  # after each char assignment moving to the next char in the coded text.
                index += second_jump
                if index < length:
                    arr[index] = text[t_i]
                    t_i += 1
                index += first_jump
        else:
            index += (key - 1) * 2
            while index < length:
                arr[index] = text[t_i]
                t_i += 1
                index += (key - 1) * 2

        segment += 1
        first_jump -= 2
        second_jump += 2
    return output.join(arr)


print(zigzag_dec("memymii aslns", 4))
print(zigzag_enc("my nameisslim", 4))
