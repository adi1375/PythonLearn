import json

def load_rates(json_file: str) -> dict[str, dict]:
    with open(json_file, 'r') as file: 
        return json.load(file)
    
def convert(amount: float, base: str, to: str, rates: dict[str, dict])-> float:
    base: str = base.lower()
    to: str = to.lower()
    
    from_rates: dict | None = rates.get(base)
    to_rates: dict | None = rates.get(to)

    try:
        if base == 'eur':
            return amount * to_rates['rate']
        elif to == 'eur':
            return amount / from_rates['rate']
        else:
            return amount * (to_rates['rate'] / from_rates['rate'])
    except TypeError:
        print("Please enter a valid currency.")
        print("List of valid currencies:")
        for i in rates:
            print(f"{rates[i]['name']} : {rates[i]['code']}")
        return 0.0
    


def main() -> None:
    rates: dict[str, dict] = load_rates(r"Ten_Mini_Projects\Project6_Rates.json")
    result: float = convert(amount=1, base='usd', to='inr', rates=rates)
    print(result)



if __name__ == '__main__':
    main()