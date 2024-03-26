# Import Library
from cvzone import *
import Its_Hub 
Hub = Its_Hub.Its_Hub()

# __version__
print("__version__:")
Its_Hub.__version__()

# Faker
print("\nFaker:")
name = Its_Hub.Its_Hub.Faker(target="name")
print(name)

# Fake_profile.Create_profile
print("\n Fake_profile -> Create_profile")
profile = Hub.Fake_profile() 
profile_o = profile.Create_profile()
print(profile_o)

# Fake_profile.Create_result
print("\nFake Profile GUI:")
profile = Hub.Fake_profile() 
profile.Create_result(profile.Create_profile())

# SQL -> Create_database
print("\nSQL -> Create_database")
sql = Hub.SQL("Users", "'name', 'last_name', 'Email'")
sql.Create_database()

# SQL -> Create_Table
print("\nSQL -> Create_Table")
sql = Hub.SQL("Users", "'name', 'last_name', 'Email'")
sql.Create_Table()

# SQL -> Save_in_database
print("\nSQL -> Save_in_database")
sql = Hub.SQL("Users", "'name', 'last_name', 'Email'") 
sql.Save_in_database("'Farbod', 'Parkhooi', 'your@email.com'")

# SQL -> Read_database
print("\nSQL -> Read_database:")
sql = Hub.SQL("Users", "'name', 'last_name', 'Email'") 
search_result = sql.Read_database("Email", "name='Farbod'")
print(search_result)

# Computer_Vision
print("\nComputer_Vision")
cv = Hub.Computer_Vision()
cv.Start_video(VideoCapture=0, Show=True, exit_button="q", Detect_Faces=True, Detect_Hands=True, Detect_Pose=True)

# Voice -> Say
print("\nVoice -> Say")
voice = Hub.Voice("Hello World!", speed=125, gender="M") 
voice.Say(save_voice=True, File_name="voice.mp3")

# QR -> Create_QR
print("\nQR -> Create_QR")
qr = Hub.QR()
qr.Create_QR(link="https://example.com", name="qrcode.png")

# QR -> GUI
print("\nQR -> GUI")
qr = Hub.QR()
qr.GUI()

# Web -> Open_website
print("\nWeb -> Open_website")
Hub.Web.Open_website("https://example.com")

# OS -> Remove_file
print("\nOS -> Remove_file")
OS = Hub.OS()
OS.Remove_file("qrcode.png")

# OS -> Remove_dir
print("\nOS -> Remove_dir")
os = Hub.OS()
try:
    os.Remove_dir("Test_dir")
except: 
    pass

# OS -> Create_file
os = Hub.OS()
os.Create_file(File_name="text.txt")

# OS -> Get_code_address
print("\nOS -> Get_code_address:")
os = Hub.OS()
code_address = os.Get_code_address()
print(code_address)

# OS -> Read_file
print("\nOS -> Read_file:")
os = Hub.OS()
text = os.Read_file(File_name="database.db")
print(text)

# OS -> Check_exist
print("\nOS -> Check_exist:")
os = Hub.OS()
result = os.Check_exist(File_name="database.db")
print(result)

# Encryption_string -> Encode
print("\nEncryption_string -> Encode:")
Encryption = Hub.Encryption_string(text="Hello, How are you today?", shift=11)
result = Encryption.Encode()
print(result)

# Encryption_string -> Decode
print("\nEncryption_string -> Decode:")
Encryption = Hub.Encryption_string(text="spwwz, szh lcp jzf ezolj?", shift=11)
result = Encryption.Decode()
print(result)

# Digital_message -> Show_info
print("\nDigital_message -> Show_info")
digital_msg = Hub.Digital_message(title="This is title", text="This is text for message")
digital_msg.Show_info()

# Digital_message -> Show_warning
print("\nDigital_message -> Show_warning")
digital_msg = Hub.Digital_message(title="This is title", text="This is text for message")
digital_msg.Show_warning()

# Digital_message -> Show_error
print("\nDigital_message -> Show_error")
digital_msg = Hub.Digital_message(title="This is title", text="This is text for message")
digital_msg.Show_error()

# Hash -> Encode
print("\nHash -> Encode:")
Hash = Hub.Hash(text="Hello world")
Hashed = Hash.Encode()
print(Hashed)

# Hash_file -> Create
print("\nHash_file -> Create:")
Hash_file = Hub.Hash_file(file_name="image.png")
Hashed = Hash_file.Create()
print(Hashed)

# Mouse -> Listener
print("\nMouse -> Listener:")
Mouse = Hub.Mouse()
# mouse_click = Mouse.Listener()

# Mouse -> Disable_mouse
print("\nMouse -> Disable_mouse")
Mouse = Hub.Mouse()
Mouse.Disable_mouse()

# Mouse -> Enable_mouse
print("\nMouse -> Enable_mouse")
Mouse = Hub.Mouse()
Mouse.Enable_mouse()

# Keyboard -> Disable_keyboard
print("\nKeyboard -> Disable_keyboard")
Keyboard = Hub.Keyboard()
Keyboard.Disable_keyboard()

# Keyboard -> Enable_keyboard
print("\nKeyboard -> Enable_keyboard")
Keyboard = Hub.Keyboard()
Keyboard.Enable_keyboard()
