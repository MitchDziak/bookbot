def text_split(text):               # Simply splits text when called.
    split_text = text.split()
    return split_text

def count_words(text):              
    words = text_split(text)        # Calls text_split
    word_count = len(words)         # Finds word count in list of split text
    return word_count
    
def count_characters(text):
    character_dict = {}
    for character in text.lower():
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1

    return character_dict

def list_characters(character_dict):                                        
    character_list = []                                                    
    for character in character_dict:                                                
        if character.isalpha():
            individual_dict = {}
            individual_dict["char"] = character
            individual_dict["num"] = character_dict[character]
            character_list.append(individual_dict)
    return character_list

