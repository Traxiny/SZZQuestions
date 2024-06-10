import argparse
from SZZQuestions import SZZQuestions

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                        prog="Getting specific questions",
                        description="Put question frequency, get questions",
                        epilog="I will finish this school!")
    
    parser.add_argument('-n', '--number')
    parser.add_argument('-gq', '--greater', action='store_true')
    parser.add_argument('-lq', '--lower', action='store_true')

    args = parser.parse_args()

    questions = SZZQuestions()

    if not args.greater and not args.lower:
        wanted_questions = questions.get_questions_by_frequency(args.number) 

        for wanted_question in wanted_questions:
            print(wanted_question) 

    elif args.greater:
        wanted_questions = questions.get_questions_greater_than_or_equal_frequency(args.number)

        for wanted_question in wanted_questions:
            print(wanted_question) 

    elif args.lower:
        wanted_questions = questions.get_questions_less_than_or_equal_frequency(args.number)
        
        for wanted_question in wanted_questions:
            print(wanted_question) 