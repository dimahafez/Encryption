import tkinter as tk
import base64

class MessageEncoderDecoder:
    # Initialize the class
    def __init__(self, master):
        # Set the main window
        self.master = master
        # Set the window title
        self.master.title("Message Encoder/Decoder")
        # Create the dictionary to store messages
        self.messages = {}
        # Create the widgets
        self.create_widgets()

    # Define a function to create the widgets
    def create_widgets(self):
        # Create a label and entry for the message
        self.label_message = tk.Label(self.master, text="Enter message:")
        self.label_message.pack()
        self.entry_message = tk.Entry(self.master, width=50)
        self.entry_message.pack()

        # Create a label and entry for the password
        self.label_password = tk.Label(self.master, text="Enter password (optional):")
        self.label_password.pack()
        self.entry_password = tk.Entry(self.master, width=50, show="*")
        self.entry_password.pack()

        # Create a button to encode the message
        self.button_encode = tk.Button(self.master, text="Encode", command=self.encode_message)
        self.button_encode.pack()

        # Create a button to decode the message
        self.button_decode = tk.Button(self.master, text="Decode", command=self.decode_message)
        self.button_decode.pack()

        # Create a label and entry to display the result
        self.label_result = tk.Label(self.master, text="Result:")
        self.label_result.pack()
        self.entry_result = tk.Entry(self.master, width=50)
        self.entry_result.pack()

    # Define a function to encode the message
    def encode_message(self):
        # Get the message and password
        message = self.entry_message.get()
        password = self.entry_password.get()
        # If a password is provided, add it to the message
        if password:
            message = f"{password}:{message}"
        # Encode the message using base64
        encoded_message = base64.b64encode(message.encode('utf-8'))
        # Store the encoded message in the messages dictionary
        self.messages[encoded_message.decode('utf-8')] = password
        # Display the encoded message in the result entry field
        self.entry_result.delete(0, tk.END)
        self.entry_result.insert(0, encoded_message.decode('utf-8'))

    # Define a function to decode the message
    def decode_message(self):
        # Get the encoded message and password
        encoded_message = self.entry_result.get()
        password = self.entry_password.get()
        try:
            # Retrieve the password from the messages dictionary
            stored_password = self.messages[encoded_message]
            # If a password is provided, check if it matches the one used to encode the message
            if password and password != stored_password:
                raise ValueError("Incorrect password!")
            # Decode the message using base64
            decoded_message = base64.b64decode(encoded_message.encode('utf-8'))
            # If a password is provided, remove it from the decoded message
            if stored_password:
                decoded_message = decoded_message.decode('utf-8').split(':', 1)[1]
        except KeyError:
            decoded_message = "Invalid message!"
        except ValueError as error:
            decoded_message = f"Error: {error}"
        # Display the decoded message in the result entry field
        self.entry_result.delete(0, tk.END)
        self.entry_result.insert(0, decoded_message)


# Create the main window
root = tk.Tk()

# Create an instance of the MessageEncoderDecoder class
app = MessageEncoderDecoder(root)

# Start the main loop
root.mainloop()
