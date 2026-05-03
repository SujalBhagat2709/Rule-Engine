def get_rules():
    
    rules = [
        {"min_age": 18, "max_age": 25, "risk": "High"},
        {"min_age": 26, "max_age": 40, "risk": "Medium"},
        {"min_age": 41, "max_age": 100, "risk": "Low"}
    ]
    
    return rules


if __name__ == "__main__":
    
    print(get_rules())