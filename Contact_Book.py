import streamlit as st
from datetime import datetime, timedelta
import random
import calendar
import time

# Initialize session state for contacts if it doesn't exist
if 'contacts' not in st.session_state:
    st.session_state.contacts = []
if 'selected_contact' not in st.session_state:
    st.session_state.selected_contact = None

# In-memory storage for notifications
notifications = []

# Function to add a contact
def add_contact(name, phone, email):
    st.session_state.contacts.append({"name": name, "phone": phone, "email": email})

# Function to delete a contact
def delete_contact(index):
    if 0 <= index < len(st.session_state.contacts):
        del st.session_state.contacts[index]

# Function to add a notification
def add_notification(message, reminder_time):
    notifications.append({"message": message, "reminder_time": reminder_time})

# Function to delete a notification
def delete_notification(index):
    if 0 <= index < len(notifications):
        del notifications[index]

# Function to determine the winner of Rock Paper Scissors
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a Tie!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You Win!"
    else:
        return "Computer Wins!"

# Function to roll a dice
def roll_dice():
    st.subheader("Roll the Dice")
    roll_button = st.button("Roll")

    if roll_button:
        dice_value = random.randint(1, 6)
        st.write(f"You rolled: {dice_value}")

# Function to display a calendar for the specified year
def display_calendar(year):
    st.header(f"Calendar for {year}")
    cal = calendar.TextCalendar(calendar.SUNDAY)
    st.text(cal.formatyear(year, 2, 1, 1, 3))


# Function to count words
def count_words(text):
    words = text.split()
    return len(words)

# Function to calculate typing speed in words per minute (WPM)
def calculate_wpm(start_time, end_time, text):
    time_diff = end_time - start_time
    time_diff_minutes = time_diff / 60
    word_count = count_words(text)
    wpm = word_count / time_diff_minutes
    return wpm

# Function to calculate accuracy
def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()
    correct_words = sum(1 for ow, tw in zip(original_words, typed_words) if ow == tw)
    total_words = len(original_words)
    accuracy = (correct_words / total_words) * 100
    return accuracy

# Function to check for a winner in Tic Tac Toe
def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]
    if ' ' not in board:
        return 'Tie'
    return None

# Function to reset the Tic Tac Toe game
def reset_game():
    st.session_state.board = [' '] * 9
    st.session_state.current_player = 'X'
    st.session_state.winner = None
    st.session_state.game_started = False

# Initialize session state variables for Tic Tac Toe
if 'board' not in st.session_state:
    reset_game()
if 'game_started' not in st.session_state:
    st.session_state.game_started = False

# Function to handle player move
def make_move(idx):
    if st.session_state.board[idx] == ' ' and not st.session_state.winner:
        st.session_state.board[idx] = st.session_state.current_player
        st.session_state.winner = check_winner(st.session_state.board)
        if not st.session_state.winner:
            st.session_state.current_player = 'O' if st.session_state.current_player == 'X' else 'X'

# Expanded list of Truth questions
truths = [
    "What's the most embarrassing thing you've ever done?",
    "What's a secret you've never told anyone?",
    "Who was your first crush?",
    "What's the biggest lie you've ever told?",
    "What's the most embarrassing thing you've ever worn?",
    "Have you ever cheated on a test?",
    "What's the weirdest dream you've ever had?",
    "Have you ever stolen something?",
    "What's your biggest fear?",
    "What's the most childish thing you still do?",
    "Who is your secret crush?",
    "What's your worst habit?",
    "What's the most embarrassing thing you've said to someone you like?",
    "What's the most embarrassing thing in your room?",
    "Have you ever lied to your best friend?",
    "What's the craziest thing you've done on a dare?",
    "Have you ever peed in a pool?",
    "What's the longest you've gone without showering?",
    "Have you ever pretended to be sick to get out of something?",
    "What's the grossest thing you've ever done?",
    "What's the most awkward date you've ever been on?",
    "Have you ever been caught picking your nose?",
    "What's the most embarrassing nickname you've ever had?",
    "What's the worst gift you've ever received?",
    "What's the weirdest food combination you've ever tried?",
    "Have you ever had a crush on a friend's sibling?",
    "What's the most embarrassing photo of you?",
    "What's the biggest rumor you've ever spread?",
    "What's the most embarrassing thing you've done in public?",
    "Have you ever farted in an elevator?",
    "What's the most awkward thing you've said in public?",
    "Have you ever snooped through someone's stuff?",
    "What's the most disgusting thing you've ever eaten?",
    "What's the most embarrassing thing you've done for attention?",
    "What's the weirdest thing you've ever done alone?",
    "Have you ever talked to yourself in the mirror?",
    "What's the worst thing you've ever smelled?",
    "Have you ever worn the same clothes for a week?",
    "What's the worst haircut you've ever had?",
    "Have you ever been caught singing in the shower?",
    "What's the most embarrassing thing you've done in front of a crowd?",
    "What's the worst thing you've ever tasted?",
    "What's the most embarrassing thing you've done on a date?",
    "What's the most childish thing you've done recently?",
    "What's the most embarrassing thing you've posted online?",
    "Have you ever lied about your age?",
    "What's the most embarrassing thing your parents have caught you doing?",
    "What's the most awkward text you've ever sent?",
    "What's the weirdest thing you've ever Googled?"
]

# Expanded list of Dare tasks
dares = [
    "Dance with no music for 1 minute.",
    "Let someone tickle you for 30 seconds.",
    "Try to lick your elbow.",
    "Do an impression of your favorite celebrity.",
    "Talk in an accent for the next 3 rounds.",
    "Do 20 pushups.",
    "Sing the chorus of your favorite song.",
    "Let someone draw on your face with a pen.",
    "Wear socks on your hands until your next turn.",
    "Do your best chicken dance outside on the lawn.",
    "Eat a spoonful of mustard.",
    "Run around the outside of the house three times.",
    "Let someone write a word on your forehead in a marker.",
    "Do your best impression of a baby being born.",
    "Try to walk on your knees until your next turn.",
    "Let someone give you a wedgie.",
    "Eat a raw onion slice.",
    "Imitate a monkey until your next turn.",
    "Let someone else do your hair however they want.",
    "Talk in an accent until your next turn.",
    "Pretend to be a waiter/waitress and take snack orders from everyone in the group.",
    "Try to juggle 3 items (they don’t have to be balls).",
    "Make a silly face and keep it that way until the next round.",
    "Let the person to your left draw on your face with a pen.",
    "Eat a raw egg.",
    "Dump a glass of cold water over your head.",
    "Hold your breath for 10 seconds.",
    "Speak in pig Latin for the next 3 rounds.",
    "Let someone pour ice down your shirt and pants.",
    "Imitate a celebrity of the group’s choosing every time you talk.",
    "Let someone give you a makeover.",
    "Talk without moving your lips until your next turn.",
    "Let someone tickle you for one minute.",
    "Go outside and shout as loud as you can, 'I believe in fairies!'",
    "Let the group give you a new hairstyle.",
    "Wear your clothes backward for the next hour.",
    "Try to lick your foot.",
    "Eat a spoonful of hot sauce.",
    "Act like a chicken until your next turn.",
    "Let someone in the group write a word on your forehead in a marker.",
    "Eat a raw clove of garlic.",
    "Wear socks on your hands until it's your turn again.",
    "Do 20 jumping jacks.",
    "Let someone else tickle you for 30 seconds.",
    "Put ice cubes down your back.",
    "Do your best impression of a baby being born.",
    "Imitate a monkey until it's your turn again.",
    "Speak in an accent chosen by the group until your next turn.",
    "Imitate a celebrity until it's your turn again."
]

# Main function to display the game
def truth_or_dare_game():
    st.title("Truth or Dare Game")

    st.write("***Welcome to the Truth or Dare game!***")
    st.write("**Press one of the buttons below to get a task.**")

    # Creating columns for side-by-side buttons
    col1, col2 = st.columns(2)

    button_style = """
        <style>
        .stButton button {
            width: 100%;
            height: 100px;
            font-size: 20px;
        }
        </style>
    """

    st.markdown(button_style, unsafe_allow_html=True)

    with col1:
        if st.button("***Truth***"):
            task = random.choice(truths)
            st.subheader("Truth Task")
            st.write(task)

    with col2:
        if st.button("***Dare***"):
            task = random.choice(dares)
            st.subheader("Dare Task")
            st.write(task)

# Main function to display the multi-app interface
def main():
    st.sidebar.title("Multi-App Navigation")
    app_choice = st.sidebar.selectbox("Choose an app", ["Truth or Dare", "Calculator", "Contact Diary", "Notification App", "Rock Paper Scissors", "Dice Rolling Simulator",
                                                        "Yearly Calendar", "Typing Speed Test", "Tic Tac Toe"])

    if app_choice == "Calculator":
        st.header("Simple Calculator")
        num1 = st.number_input("Enter first number", format="%.2f")
        num2 = st.number_input("Enter second number", format="%.2f")
        operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])
        if st.button("Calculate"):
            if operation == "Add":
                result = num1 + num2
            elif operation == "Subtract":
                result = num1 - num2
            elif operation == "Multiply":
                result = num1 * num2
            elif operation == "Divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error! Division by zero."
            st.write(f"The result is: {result}")

    elif app_choice == "Contact Diary":
        st.header("Contact Book Application")
        name = st.text_input("Name")
        phone = st.text_input("Phone")
        email = st.text_input("Email")
        if st.button("Add Contact"):
            if name and phone and email:
                add_contact(name, phone, email)
                st.success("Contact added successfully!")
            else:
                st.error("Please fill in all fields.")

        st.sidebar.header("Saved Contacts")
        if st.session_state.contacts:
            for index, contact in enumerate(st.session_state.contacts):
                if st.sidebar.button(contact['name'], key=f"sidebar_{index}"):
                    st.session_state.selected_contact = index

            if st.session_state.selected_contact is not None:
                contact = st.session_state.contacts[st.session_state.selected_contact]
                st.header("Contact Details")
                st.text(f"Name: {contact['name']}")
                st.text(f"Phone: {contact['phone']}")
                st.text(f"Email: {contact['email']}")
                if st.button("Delete Contact", key="delete"):
                    delete_contact(st.session_state.selected_contact)
                    st.success("Contact deleted successfully!")
                    st.session_state.selected_contact = None
                    st.experimental_rerun()
        else:
            st.sidebar.text("No contacts available.")

    elif app_choice == "Notification App":
        st.header("Notification App")
        message = st.text_input("Enter your notification message")
        reminder_date = st.date_input("Select reminder date")
        reminder_time = st.time_input("Select reminder time")

        if st.button("Set Reminder"):
            if message and reminder_date and reminder_time:
                reminder_datetime = datetime.combine(reminder_date, reminder_time)
                add_notification(message, reminder_datetime)
                st.success("Reminder set successfully!")
            else:
                st.error("Please fill in all fields.")

        st.header("Notifications")
        if notifications:
            for index, notification in enumerate(notifications):
                st.write(f"Message: {notification['message']}")
                st.write(f"Reminder Time: {notification['reminder_time'].strftime('%Y-%m-%d %H:%M:%S')}")
                if st.button(f"Delete Notification {index + 1}", key=index):
                    delete_notification(index)
                    st.success("Notification deleted successfully!")
        else:
            st.write("No notifications set.")

    elif app_choice == "Rock Paper Scissors":
        st.title("Rock Paper Scissors")
        st.write("Play Rock Paper Scissors against the computer!")
        
        player_choice = st.selectbox("Choose your move", ["Rock", "Paper", "Scissors"])
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        if st.button("Play"):
            winner = determine_winner(player_choice, computer_choice)
            st.write(f"You chose: {player_choice}")
            st.write(f"Computer chose: {computer_choice}")
            st.write(f"Result: {winner}")

    elif app_choice == "Dice Rolling Simulator":
        st.title("Dice Rolling Simulator")
        roll_dice()

    elif app_choice == "Yearly Calendar":
        st.header("Yearly Calendar")
        year = st.number_input("Enter the year", min_value=1900, max_value=2100, step=1, value=datetime.now().year)
        display_calendar(year)

    elif app_choice == "Typing Speed Test":
        st.header("Typing Speed Test")
        sample_texts = ['''
        Streamlit is an open-source app framework for Machine Learning and Data Science teams.\n
        It is incredibly easy to build beautiful, custom web apps using Streamlit.\n
        Streamlit is the fastest way to build and share data apps.\n
        With Streamlit, you can turn data scripts into shareable web apps in minutes.\n
        Streamlit apps are Python scripts that run as web applications.
        ''']
        original_text = random.choice(sample_texts)

        st.write("Type the following text as quickly and accurately as you can:")
        st.write(original_text)

        if 'start_time' not in st.session_state:
            st.session_state.start_time = None
        if 'typed_text' not in st.session_state:
            st.session_state.typed_text = ''

        start_button = st.button("Start Test")
        if start_button:
            st.session_state.start_time = time.time()
            st.session_state.typed_text = ''

        if st.session_state.start_time:
            elapsed_time = time.time() - st.session_state.start_time
            remaining_time = max(60 - elapsed_time, 0)  # 60 seconds countdown

            st.write(f"Time remaining: {remaining_time:.2f} seconds")

            if remaining_time <= 0:
                st.write("Time is up!")
                end_time = time.time()
                wpm = calculate_wpm(st.session_state.start_time, end_time, st.session_state.typed_text)
                accuracy = calculate_accuracy(original_text, st.session_state.typed_text)

                st.write(f"Your typing speed: {wpm:.2f} words per minute")
                st.write(f"Your typing accuracy: {accuracy:.2f}%")

                st.session_state.start_time = None  # Reset start time
            else:
                st.session_state.typed_text = st.text_area("Start typing here:", value=st.session_state.typed_text)
                st.button("Submit")

    elif app_choice == "Tic Tac Toe":
        st.title("Tic Tac Toe")
        st.markdown(
            """
            <style>
            .tic-tac-toe-button {
                background-color: #f0f0f0;
                border: 2px solid #333;
                color: #333;
                font-size: 24px;
                font-weight: bold;
                padding: 20px;
                margin: 5px;
                width: 100%;
                height: 100%;
                text-align: center;
                cursor: pointer;
            }
            .tic-tac-toe-button:hover {
                background-color: #ddd;
            }
            .tic-tac-toe-button:disabled {
                background-color: #fff;
                color: #000;
            }
            .tic-tac-toe-button-x {
                background-color: #4CAF50 !important;
                color: black !important;
            }
            .tic-tac-toe-button-o {
                background-color: #2196F3 !important;
                color: black !important;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        if not st.session_state.game_started:
            st.header("Enter Player Names")
            st.session_state.player_X = st.text_input("Player X")
            st.session_state.player_O = st.text_input("Player O")

            if st.button("Start Game"):
                if st.session_state.player_X and st.session_state.player_O:
                    st.session_state.game_started = True
                    st.experimental_rerun()
                else:
                    st.error("Please enter names for both players.")

        if st.session_state.game_started:
            st.header(f"{st.session_state.player_X} (X) vs {st.session_state.player_O} (O)")

            col1, col2, col3 = st.columns(3)
            for i, col in enumerate([col1, col2, col3]):
                for j in range(3):
                    idx = i * 3 + j
                    button_text = st.session_state.board[idx]
                    if button_text == ' ':
                        button_text = ''
                    if st.session_state.board[idx] == ' ':
                        if col.button(button_text, key=idx):
                            make_move(idx)
                            st.experimental_rerun()
                    else:
                        html = f'<button class="tic-tac-toe-button tic-tac-toe-button-{st.session_state.board[idx].lower()}" disabled>{st.session_state.board[idx]}</button>'
                        col.markdown(html, unsafe_allow_html=True)

            if st.session_state.winner:
                if st.session_state.winner == 'Tie':
                    st.subheader("It's a Tie!")
                else:
                    winner_name = st.session_state.player_X if st.session_state.winner == 'X' else st.session_state.player_O
                    st.subheader(f"{winner_name} ({st.session_state.winner}) wins!")
                if st.button("Reset Game"):
                    reset_game()
                    st.experimental_rerun()
            
    elif app_choice == "Truth or Dare":
        truth_or_dare_game()

if __name__ == "__main__":
    main()
