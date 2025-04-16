from collections import Counter

def open_file(path: str) -> str:
    with open(path, 'r') as file:
        text: str = file.read()
        return text

def analyze(text: str) -> dict[str, int]:
    
    common_words : Counter = Counter(text.split())
    
    result: dict[str, int] = {
        'total_chars_incl_spaces': len(text),
        'total_chars_not_incl_spaces': len(text.replace(' ','')),
        'total_spaces': text.count(' '),
        'total_words': len(text.split()),
        'top_5_common_words':[word for word, count in common_words.most_common(n=5)]
    }

    return result


def main() -> None:
    # print(open_file(r"Ten_Mini_Projects\Project7_note.txt"))
    text: str = open_file(r"Ten_Mini_Projects\Project7_note.txt")
    analysis: dict[str, int] = analyze(text)
    
    print(f'"{text}"\n')
    # for key,value in analysis.items():
    #     print(f"{key} : {value}")

    print(f"""This text file contains {analysis['total_words']} words which consist of {analysis['total_chars_not_incl_spaces']} letters and {analysis['total_spaces']} spaces.
If we include spaces then there are {analysis['total_chars_incl_spaces']} characters.
The top 5 most common words in the text are: \n{analysis['top_5_common_words']}.""")

if __name__ == '__main__':
    main()