
def analyze_text(text: str, target_word: str):

    words = text.split()

    total_words = len(words)
    target_count = 0
    longest_word = ""
    
    for i in words:
        clean_word = i.strip(".,!?;:\"()")
        
     
        if clean_word.lower() == target_word.lower():
            target_count += 1
            
        
        if len(clean_word) > len(longest_word):
            longest_word = clean_word
            
    return total_words, target_count, longest_word

