def decode_from_list(lines):
    # Parse the lines
    number_word_dict = {}
    for line in lines:
        number, word = line.strip().split()
        number = int(number)
        number_word_dict[number] = word

    # Determine the end-of-level numbers in the pyramid
    end_of_level_numbers = []
    cumulative_count = 0
    level = 1
    while cumulative_count + level <= len(number_word_dict):
        cumulative_count += level
        end_of_level_numbers.append(cumulative_count)
        level += 1

    # Extract the words corresponding to the end-of-level numbers
    decoded_message = []
    for number in end_of_level_numbers:
        if number in number_word_dict:
            decoded_message.append(number_word_dict[number])
    
    # Join the words to form the final decoded message
    return ' '.join(decoded_message)

# Example usage with a list of input lines
input_lines = [
    "3 love",
    "6 computers",
    "2 dogs",
    "4 cats",
    "1 I",
    "5 you"
]

decoded_message = decode_from_list(input_lines)
print(decoded_message)  # Expected output: "I love computers"
