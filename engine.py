from rules import get_rules

def evaluate(age):
    
    rules = get_rules()
    
    for rule in rules:
        
        if rule["min_age"] <= age <= rule["max_age"]:
            return rule["risk"]
    
    return "Unknown"


if __name__ == "__main__":
    
    print("Age 22:", evaluate(22))
    print("Age 35:", evaluate(35))