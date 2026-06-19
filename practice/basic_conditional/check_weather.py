def check_weather(temp: float) -> str:
    """Determine weather condition based on temperature."""
    if temp < 15:
        return "Cold"
    elif temp <= 35:
        return "Normal"
    else:
        return "Hot"

if __name__ == "__main__":
    try:
        user_temp = float(input("Enter temperature in Celsius: "))
        print(f"The weather is {check_weather(user_temp)}")
    except ValueError:
        print("Invalid input! Please enter a valid temperature.")
