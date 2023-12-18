# Version: 0.0.9

<h1>Intro </h1>
<p>
Its_Hub library. <br />
This is a library with Other Libraries! (; <br />
U Can Use This Library For Use Few Other Libraries. 4 Example:
<b>
<ul>
    <li>Faker</li>
    <li>Tkinter</li>
    <li>CV2</li>
    <li>Tkhtmlview</li>
    <li>sqlite3 </li>
    <li>...</li>
</ul>
</b>

My name is Farbod Parkhooi(Or you can call me Tik Ten) <br />
This is my Github link: <a href="https://www.github.com/tik-ten/">`https://www.github.com/tik-ten/`</a> <br />
Thanks for use.<br />
</p>

# How to install
For download this library:
```git
>>> git clone https://github.com/Tik-Ten/Its_Hub.git
>>> cd Its_Hub
>>> pip install -r requirements.txt
>>> python setup.py <Your python libraries address>
```
example for python libraries address: <b>"C:/Users/Farbod Parkhooi/AppData/Local/Programs/Python/Python311/Lib" </b>

# How to remove
To remove this app:
```git
>>> cd Its_Hub
>>> python remove.py <Your python libraries address>
```
example for python libraries address: <b>"C:/Users/Farbod Parkhooi/AppData/Local/Programs/Python/Python311/Lib" </b>

# Check
```Python
import Its_Hub
Its_Hub.__version__()
# Output:
Its_Hub Library version is 0.0.9
```

# How to use ... library
<ul>
    <li><a href="#Faker">Faker</a></li>
    <li><a href="#Fake_profile">Fake_profile</a></li>
    <li><a href="#Mini">Mini</a></li>
    <li><a href="#SQL">SQL </a></li>
</ul>

<h2>Use Libraries </h2>
    For use Its_Hub you can use This:

```Python
from Its_Hub import Its_Hub
hub = Its_Hub()
````

# Faker
For use Faker:
```Python
Its_Hub.Faker(target="") # "first_name" or "last_name" or "name" or "phone_number" or "address" or "profile" or "job" or "company" or "website" or "blood_group"

# You can print that:
print(Its_Hub.Faker(target="name"))
# and you can save taht in a value
name = Its_Hub.Faker(target="name") 
```

# Fake_profile 
### Show a digital fake profile
```Python
profile = hub.Fake_profile() # You can customize job, company, name, and ...
profile.Create_result(profile.Create_profile()) 
```
output:

<img src="Files\out1.png">

### Create list of a fake profile
```Python
profile = hub.Fake_profile()
Profile_list = profile.Create_profile()
print(Profile_list)
```
# Mini
### Plus
You can use this function for num1 + num2 (:
```python
result = hub.Mini.Plus(number=8, plus=10)
print(ans)
```
### Count
You can count and plus with this function.
```Python
count_ans = hub.Mini.Count(0, 5)
print(count_ans)
```

# SQL
### Create_database
```Python
sql = hub.SQL("Users", "'Name', 'Email', 'Password'") # You most write Table_name and Table_Attributes and you can write the Database_address, and Database_name
sql.Create_database()
```

### Create_Table
```Python
sql = hub.SQL("Users", "'Name', 'Email', 'Password'") # You most write Table_name and Table_Attributes and you can write the Database_address, and Database_name
sql.Create_Table()
```

### Save_in_database
```Python
sql = hub.SQL("Users", "'Name', 'Email', 'Password'") # You most write Table_name and Table_Attributes and you can write the Database_address, and Database_name
sql.Save_in_database("'Farbod Parkhooi', 'your@email.com', 'Example@2023'")
```
