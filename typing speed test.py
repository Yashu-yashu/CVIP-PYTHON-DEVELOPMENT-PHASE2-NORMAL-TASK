import time

def typing_speed_test():
    text = "The quick brown fox jumps over the lazy dog"  # Replace with your desired text
    print("Type the following text:")
    print(text)
    input("Press Enter to start...")

    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()

    elapsed_time = end_time - start_time
    words = len(text.split())
    typing_speed = words / (elapsed_time / 60)  # Calculate WPM

    print(f"\nYou typed {words} words in {elapsed_time:.2f} seconds.")
    print(f"Your typing speed is {typing_speed:.2f} WPM.")

if __name__ == "__main__":
    typing_speed_test()
